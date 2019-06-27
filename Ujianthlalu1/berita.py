import requests

print('Selamat datang, mau tahu berita apa hari ini?\n'
  '[1] Berita seputar teknologi\n'
  '[2] Berita seputar bisnis\n'
  '[3] Berita seputar olahraga\n'
  '[4] Berita seputar kesehatan\n'
  '[5] Berita seputar science\n')

url = ('https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=95b921fd9e69416aa232a043fd5f3f60')

pilih = int(input('Ketik pilihan Anda [1/2/3/4/5] : '))
if pilih == 1:
    url = ('https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=95b921fd9e69416aa232a043fd5f3f60')
elif pilih == 2:
    url = ('https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=95b921fd9e69416aa232a043fd5f3f60')
elif pilih == 3:
    url = ('https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=95b921fd9e69416aa232a043fd5f3f60')
elif pilih == 4:
    url = ('https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=95b921fd9e69416aa232a043fd5f3f60')
elif pilih == 5:
    url = ('https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=95b921fd9e69416aa232a043fd5f3f60')


berita = requests.get(url)

for i in range(5):
    print(i+1, ' - ', berita.json()['articles'][i+1]['title'])

print()

