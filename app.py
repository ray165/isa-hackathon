from flask import Flask, request, jsonify
from transformers import pipeline
import json

sentiment_pipeline = pipeline("sentiment-analysis")
app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/api')
def analyse():
    sentence = request.args.get('sentence')
    result = sentiment_pipeline(sentence)  # Use json.dumps() to convert to JSON string
    print(result)
    return result # Set content type to JSON

app.run()