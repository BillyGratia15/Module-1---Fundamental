from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

#https://shopee.co.id/search?keyword=tamiya     --> cth request argumen dari shopee
@app.route('/search')
def search():
    # print(request.args)                       #==> kalau gini aja akan keluar:ImmutableMultiDict([('keyword','tamiya')])
    # print(request.args['keyword'])            #==> kalau gini langsung keluar value dari keyword yg dicari (diteminalnya)
    # print(request.args)                       # keluar value id yang dicari di terminal
    # print(request.args['katakunci'])          # kalau gini aja munculnya ImmutableMultiDict(['katakunci','tamiya']),('Lokasi','Jakarta') --> kalau misalkan ada tambahan route lokasi
    # print(request.args['lokasi'])
    # return request.args['katakunci'] + ' ' + request.args['lokasi']
    ''' kalau pakai cara diatas, misalkan katakunci ga di get makan error, cara menanggulanginya: '''
    if 'keyword' in request.args:
        return request.args['keyword']
    else:
        return 'Data tidak ditemukan'

if __name__ == '__main__':
    app.run(debug=True)