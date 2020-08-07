#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/temp')
def temp_check():
    return "temprature is 27C"

if __name__ == '__main__':
    app.run(host='172.20.10.08', port=80, debug=True)