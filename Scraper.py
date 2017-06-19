import bs4 as bs
    # may need to change to bs3 dpepending on pythoon version
import urllib.request
# import tkinter as tk
# from tkinter.simpledialog import askstring, askinteger
# from tkinter.messagebox import showerror

'''
# it looks like having a dialog box is a lot of work; for future reference:
    https://stackoverflow.com/questions/40251509/how-to-open-a-tkinter-dialog-box-and-use-the-result-later-in-the-program
    https://stackoverflow.com/questions/10057672/correct-way-to-implement-a-custom-popup-tkinter-dialog-box
    https://stackoverflow.com/questions/34830906/taking-integer-and-string-input-from-gui-in-python

def string_from_dialog(title, text):
    root = Tk()
    root.result = simpledialog.askstring(title, text)
    root.withdraw()
    return root.result
'''

def get_links(page):
    source = urllib.request.urlopen(page).read()
    soup = bs.BeautifulSoup(source, "lxml")
    links = []
    body = soup.body
    for paragraph in body.find_all("p"):
        for url in paragraph.find_all("a"):
            links.append(url.get("href"))

    return links


def get_text(page):
    source = urllib.request.urlopen(page).read()
    soup = bs.BeautifulSoup(source, "lxml")
    text = []
    body = soup.body
    for paragraph in body.find_all("p"):
        text.append(paragraph.text)
    text = " ".join(text)
    new_text = text
    length = len(text)
    # print()
    # print("length:",length)
    for i in range(len(text)):
        if text[length-i-1] == "[":
            # print("i:",length-i-1)
            # new_text = new_text[:length-i-2] + new_text[length-i+1:]

            for j in range(i+1):
                # print("j:",j,text[j+length-i-1])
                if text[j+length-i-1] == "]":

                    new_text = new_text[:length-i-1] + new_text[length-i+j:]
                    break

    return new_text







if __name__ == "__main__":
    print()
    print(get_text("https://en.wikipedia.org/wiki/Veiki_moraine"))
