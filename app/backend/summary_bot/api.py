from flask import jsonify, request, Blueprint

from backend.database.connector import SummaryDBConnector
from backend.summary_bot.models.summarizers import get_summarizer

import ast


summary_api = Blueprint('summary_api', __name__)
TEXT_MIN_LENGTH = 5
TEXT_MAX_LENGTH = 30


@summary_api.route('/api/v1/summarize', methods=['POST', 'GET'])
def summarize():

    text_data = request.get_data()
    text_data = text_data.decode("utf-8")[5:].replace('+', ' ').replace('%2C', ',')

    # estimate number of words
    n_words = len(text_data.split(' '))

    # avoid running summarizer if n_words less than min length
    if n_words < TEXT_MAX_LENGTH or n_words < TEXT_MIN_LENGTH:
        text_summary = text_data
    else:
        # avoid loading tensorflow unless needed.
        summarizer = get_summarizer()
        text_summary = summarizer(f"""{text_data}""",
                                  min_length=TEXT_MAX_LENGTH,
                                  max_length=TEXT_MAX_LENGTH)[0]['summary_text']

    print(f'\n'
          f'======= [RESULT INFO] ==========\n'
          f'text_data: \n'
          f'{text_data}\n'
          f'\n'
          f'text_summary: \n'
          f'{text_summary}')

    db = SummaryDBConnector()
    summary_id = db.insert(text=text_data, text_summary=text_summary)
    db.close()
    return jsonify(summary_id=summary_id, summary=text_summary)


@summary_api.route('/api/v1/get_summary', methods=['POST', 'GET'])
def get_summary():
    data = request.data
    data = data.decode('utf-8')
    data = ast.literal_eval(data)  # to Dict[str, str]
    summary_id = data['summary_id']
    summary_id = int(summary_id)
    print(f'text_id = {summary_id}')

    db = SummaryDBConnector()
    res = db.query(text_id=summary_id)
    db.close()

    if not res:
        long_text = 'ID not found. Please try a different ID value.'
        text_summary = ''
    else:
        long_text, text_summary = res[0]
    return jsonify(long_text=long_text, text_summary=text_summary)
