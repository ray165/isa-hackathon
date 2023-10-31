from flask import Flask, request
from transformers import pipeline
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/api')
def analyse():
    sentence = request.args.get('sentence')
    result = sentiment_pipeline(sentence)
    return(result)

app.run()