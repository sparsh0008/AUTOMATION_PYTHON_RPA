import requests

for i in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    z = r.text

    f = open('quotes.txt', 'a', encoding='utf-8')

    for line in z.split("\n"):
        if '<span class="text" itemprop="text">' in line:
            result = line.replace('<span class="text" itemprop="text">“', "")
            Final = result.replace('”</span>', "").strip()
            f.write(Final)
            f.write("\n")

    f.close()