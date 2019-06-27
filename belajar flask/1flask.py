from flask import Flask , send_from_directory, render_template, request , redirect, url_for

app = Flask(__name__, static_url_path='')

data = {
    'nama' :"Andi",
    'pwd' : "12345"
}

#home route
@app.route('/')
def home():
    return '<h1>Welcome to my web server!</h1>'

#render template html
@app.route('/login')
def login():
    return render_template('html.html')

@app.route('/signup')
def signup():
    return render_template('html2.html')

#POST route
@app.route('/post', methods= ['POST'])
def post():
    nam = request.form['nama']
    pwd = request.form['pass']
    print('Nama:', nam , ' Pass :', pwd)
    # return 'Nama: ' + nam + ' Pass: ' + pwd
    return redirect(url_for('sukses', nama = nam))

@app.route('/sukses/<string:nama>')
def sukses(nama):
    return '<h1>Selamat datang ' + nama + '</h1>' 

    # data = request.json
    # print('Anda nge-Post : ' + data['nama'] + data['pass'])
    # return 'Anda nge-Post : ' + data['nama'] + data['pass']

#render static file
@app.route('/images/<path:x>')
def staticfile(x):
    return send_from_directory('images', x)

#404 route
@app.errorhandler(404)
def error404(error):
    return '<h1>Error : 404 Not Found</h1>'

if __name__ == '__main__':
    app.run(debug = True)