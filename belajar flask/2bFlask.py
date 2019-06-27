from flask import Flask , send_from_directory, render_template, request , redirect, url_for
app = Flask(__name__, static_url_path='')

import json

with open('1.json') as dataku:
    data = json.load(dataku)

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
@app.route('/postlogin', methods = ['POST'])
def postlogin():
    nam = request.form['nama']
    pwd = request.form['pass']
    print('Nama:', nam , ' Pass :', pwd)
    i = 0
    while i < len(data):
        if data[i]['nama'] == nam and data[i]['pass'] == pwd:
            return redirect(url_for('suksesLogin', nama = nam))
        elif i == (len(data)-1) and data[i]['nama'] != nam and data[i]['pass'] != pwd:
            return redirect(url_for('gagalLogin', nama = nam))
        i += 1

x = {'nama' : '', 'pass' : ''}

@app.route('/postsignup', methods = ['POST'])
def postsignup():
    nam = request.form['nama']
    pwd = request.form['pass']
    print('Nama:', nam , ' Pass :', pwd)
    i = 0
    while i < len(data):
        if data[i]['nama'] == nam and data[i]['pass'] == pwd:
            return redirect(url_for('gagalSignup', nama = nam))
        elif i == (len(data)-1) and data[i]['nama'] != nam and data[i]['pass'] != pwd:
            x['nama'] = nam
            x['pass'] = pwd
            data.append(x)
            jsonku = open ('1.json', 'w')
            jsonku.write = (str(json.dumps(data)))
            return redirect(url_for('suksesSignup', nama = nam))
        i += 1

@app.route('/sukseslogin/<string:nama>')
def suksesLogin(nama):
    return '<h1>Anda telah berhasil login! Selamat Datang ' + nama + '</h1>'

@app.route('/gagallogin/<string:nama>')
def gagalLogin(nama):
    return '<h1>Maaf anda gagal login, nama anda belum terdaftar!</h1>'

@app.route('/suksessignup/<string:nama>')
def suksesSignup(nama):
    return 'Selamat Datang' + nama + '! Anda telah berhasil di sign-up</h1>'

@app.route('/gagalsignup/<string:nama>')
def gagalSignup(nama):
    return '<h1>Maaf nama anda telah terdaftar!</h1>'

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