# import libs
import requests
from bs4 import BeautifulSoup

# write to txt file
f = open('movies.txt', 'w', encoding='utf-8')

# count variable for serial number to present in the output screen
count = 0

r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# Code below is for Extracting data from the website
for q in soup.findAll('tbody', {'class': 'lister-list'}):
    for a in q.findAll('td', {'class': 'titleColumn'}):
        for b in a.findAll('a'):
            print("", end="")
            count = count + 1

        for y in a.findAll('span'):
            f.write("{0} : {1} - {2}".format(count, b.string, y.string))
            f.write("\n")

print("\nEnd of writing into txt file Top 250 Movies")
f.close()
