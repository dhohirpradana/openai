from flask import Flask, jsonify, request
import openai_question
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Get


@app.route('/')
def home():
    return "Hello world!"


@app.route('/openai-question', methods=['POST'])
def openai_questions():
    return openai_question.handler(request, jsonify)


# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)