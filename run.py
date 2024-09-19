#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Change the host and port here
    app.run(host='0.0.0.0', port=5000)
