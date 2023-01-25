import requests

r = requests.get("https://quotes.toscrape.com/")
z = r.text
f = open('quotes.txt', 'w')

for line in z.split("\n"):
    if '<span class="text" itemprop="text">' in line:
        result = line.replace('<span class="text" itemprop="text">“', "")
        Fresult = result.replace('”</span>', "").strip()
        f.write(Fresult)
        f.write("\n")

f.close()
