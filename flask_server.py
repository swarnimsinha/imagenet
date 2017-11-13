#!/usr/bin/env python
from flask import Flask, render_template, request
app = Flask(__name__)
import subprocess

@app.route("/")
def upload_files():
    return render_template('tensor.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        output = subprocess.run("python classify.py --image_file " + f.filename, shell=True)
        return 'file uploaded successfully'


def hello():
    return "Hello World!sfaj laka"


if __name__ == "__main__":
    app.run(debug=True)
