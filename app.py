from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "Hello, this is a GET request!"
    elif request.method == 'POST':
        return "Hello, this is a POST request!"

if __name__ == '__main__':
    app.run(debug=True)
