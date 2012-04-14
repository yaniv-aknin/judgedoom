#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('parent.html', args=request.args)

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
