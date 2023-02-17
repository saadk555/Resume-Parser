from ast import dump
from flask import * 
from glob import glob 
import os
from io import BytesIO
from zipfile import ZipFile
from flask import after_this_request
import io
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage




app = Flask(__name__) 

app.static_folder = 'static'


UPLOAD_FOLDER = r"D:\python_workspaces\Resume-parser_ms\Resume-Parser\UPLOAD_FOLDER"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'hello123'    

keyword = []
value=0

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global value
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success'),code=307)
    return render_template('index.html')  

@app.route('/success', methods=['GET', 'POST'])
def success():
    from main import mainf
    if request.method=='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file_name = file.filename
            result = mainf(file_name)
            return result


if __name__ == '__main__':  
    app.run(host= 'localhost', debug = True) 
