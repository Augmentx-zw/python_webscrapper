import requests

responce = requests.get('https://en.m.wikipedia.org/wiki/Khabib_Nurmagomedov')

print(responce.status_code)
print(responce.text)

with open('khabib_2.html', 'w', encoding='utf-8') as f:
    f.write(responce.text)