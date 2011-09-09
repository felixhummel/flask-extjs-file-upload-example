#!/usr/bin/env python
# vim: set fileencoding=utf-8 filetype=python :

import os
from flask import Flask, request, redirect, url_for
from flask import send_from_directory
from flask import render_template
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/uploads', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_url = '/uploads/%s'%filename
        return '''\
{
    "success":true, // note this is Boolean, not string
    "msg":"Consignment updated",
    "file": "%s",
    "file_url": "%s"
}\
'''%(filename, file_url)
    return '''\
{
    "success": false, // note this is Boolean, not string
    "msg":"Consignment updated"
}\
'''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
