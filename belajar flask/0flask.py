# pip install flask

from flask import make_response, abort, Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

karyawan = [
    {'id': 1, 'nama': 'Andi', 'usia': 22},
    {'id': 2, 'nama': 'Budi', 'usia': 23},
    {'id': 3, 'nama': 'Caca', 'usia': 24},
]

@app.route('/data')
def data():
    return jsonify(karyawan)
    
@app.route('/data/<int:id>')
def dataSatuan(id):
    if id < 1 or id > len(karyawan):
        abort(404)
    else:
        return jsonify(karyawan[int(id) - 1])    

profilku = {
    'nama' : 'Budi Sudarsono',
    'usia' : 21
}

@app.route('/about')
def about():
    # nama = 'Andi'
    # usia = 32
    return render_template('about.html',
        profil = profilku
    )

@app.route('/tes', methods = ['GET','POST','PUT','DELETE'])
def tes():
    if request.method == 'GET':
        return 'Anda nge-Get'
    elif request.method == 'POST':
        pesanBody = request.json
        print(pesanBody['nama'])
        return 'Pesan yang anda kirim = ' + pesanBody['nama']
    else:
        return 'Anda tidak nge-Get atau nge-Post'


@app.errorhandler(404)
def tidakFound(error):
    # return make_response('<h1>Sorry! Not Found!!</h1>', 404)
    return make_response(
        render_template('error.html')
    )
if __name__ == '__main__':
    app.run(debug = True)

