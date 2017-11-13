#!/usr/bin/env python
from flask import Flask, render_template, request
app = Flask(__name__)
import subprocess
import os

#import classify


@app.route("/")
# def runprogram():
#     # coll_run = subprocess.run(
#     #     [program, *args],
#     #     input=inputstr.encode(),
#     #     stdout=subprocess.PIPE,
#     #     stderr=subprocess.PIPE)
#     coll_run = subprocess.call('python', 'classify.py', shell=False)
def upload_files():
    return render_template('tensor.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        # runprogram()
        # classify.run_inference_on_image('panda.JPG')
        output = subprocess.run("python classify.py --image_file " + f.filename, shell=True)
        #return (output)
        #return test
        return 'file uploaded successfully'


def hello():
    return "Hello World!sfaj laka"


if __name__ == "__main__":
    app.run(debug=True)
