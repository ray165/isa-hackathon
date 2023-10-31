from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)


@app.route('/api')
def analyse():
    # sentence = request.args.get('sentence')
    # sentiment_pipeline = pipeline("sentiment-analysis")
    # data = ["I love you", "I hate you"]
    # sentiment_pipeline(data)
    return(sentence)

app.run()