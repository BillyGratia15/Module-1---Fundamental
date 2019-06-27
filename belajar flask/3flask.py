from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

karyawan = [
    {'id': 1, 'NAMA':'Andi','JOB':'Sales'},
    {'id': 2, 'NAMA':'Budi','JOB':'Marketing'},
    {'id': 3, 'NAMA':'Andi','JOB':'IT'}
]

#localhost:5000/search?id=2
@app.route('/search')
def search():
    if 'id' in request.args:
        id = int(request.args['id'])
        if id < 1 or id > len(karyawan):
            return 'Maaf data tidak ditemukan'
        else:
            return jsonify(karyawan[int(id)-1])
    else:
        return jsonify(karyawan)

if __name__ == '__main__':
    app.run(debug = True)

