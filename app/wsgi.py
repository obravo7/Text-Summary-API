from flask import Flask, render_template
from flask_cors import CORS

from backend.summary_bot.api import summary_api

app = Flask(__name__)
app.register_blueprint(summary_api)

#
cors = CORS()
cors.init_app(app=app, supports_credentials=True)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
