

def get_summarizer():
    from transformers import pipeline
    # https://huggingface.co/facebook/bart-large-cnn
    # summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # default model (smaller model)
    summarizer = pipeline("summarization")
    return summarizer
