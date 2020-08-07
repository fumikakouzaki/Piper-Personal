#!/usr/bin/env python
from flask import Flask
from temperature import ds18b20-line.py
app = Flask(__name__)

@app.route('/temp')
def temp_check():
    return temp_start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)