''' In Anlehung an http://flask.pocoo.org/docs/1.0/patterns/fileuploads/ '''
import os
from flask import Flask, request
from werkzeug.utils import secure_filename

FORM = '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
<p>{}</p>
'''

app = Flask(__name__)
app.secret_key = '4be387e9eb7cf340d1ee280719a7e14d0b965cfa'
app.config['UPLOAD_FOLDER'] = '.'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'GET':
    return FORM.format('')
  if 'file' not in request.files:
    return FORM.format('Please choose a file')
  sel_file = request.files['file']
  if sel_file:
    filename = secure_filename(sel_file.filename)
    sel_file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                               filename))
    return ('<h1>file {} was uploaded successfully<h1>'
            .format(sel_file.filename))
