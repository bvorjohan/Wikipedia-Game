import bs4 as bs
import urllib.request

# source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Pahari_languages").read()

soup = bs.BeautifulSoup(source, "lxml")

# print(source)
#
# for paragraph in soup.find_all("p"):
#     print(paragraph.text)
#     print()
#
# print(soup.get_text)

#

meth_1 = []
meth_2 = []


for url in soup.find_all("a"):
    # print(url.get("href"))
    meth_1.append(url.get("href"))
#
#
#
# for div in soup.find_all("div", class_="body"):
#     for url in div.find_all("a"):
#         print(url.get("href"))

body = soup.body
for paragraph in body.find_all("p"):
    for url in paragraph.find_all("a"):
        # print(url.get("href"))
        meth_2.append(url.get("href"))


print(len(meth_1))
print(len(meth_2))
