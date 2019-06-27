from flask import Flask , render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename #bawaan flask
import os #untuk ngatur path dimana mau disimpan

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './storage'

#home route
@app.route('/')
def home():
    return render_template('0home.html')

#new route
@app.route('/new')
def new():
    return render_template('0new.html')    

#upload route
@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['file'] #buat ngupload files
    namafile = secure_filename(data.filename)
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], namafile))
    return redirect('/storage/' + namafile)

# after upload = render static file
@app.route('/storage/<path:path>')
def suksesUpload(path):
    return send_from_directory('storage', path)
#404 route
@app.errorhandler(404)
def error404(error):
    return render_template('0error.html')

if __name__ == '__main__':
    app.run(debug = True)