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
    print(request)
    sentence = request.args.get('setence')
    print(sentence)
    result = json.dumps(sentiment_pipeline(sentence))  # Use json.dumps() to convert to JSON string
    print(result)
    return result, 200, {'Content-Type': 'application/json'}  # Set content type to JSON

app.run()