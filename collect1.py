import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import ast
from selenium import webdriver

path = r'D:chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.google.com/search?biw=1536&bih=722&tbm=isch&sxsrf=ACYBGNTTymdhKLpqNEvoIFGXCiQy0Ip3zA%3A1568461113876&sa=1&ei=OdF8XZ2SNcTMvgTK_aCwCQ&q=shpping+container&oq=shpping+container&gs_l=img.3...6952.8961..9069...0.0..0.329.1410.0j5j1j1......0....1..gws-wiz-img.......0i7i30.DPVUjNhKdGc&ved=0ahUKEwjdkqX8nNDkAhVEpo8KHco-CJYQ4dUDCAc&uact=5'
directory = 'D:Picture'
def getURLs(URL):

    driver.get(URL)
    a=input()
    page = driver.page_source
    print(page)

    soup = Soup(page, 'lxml')

    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})

    ourURLs = []

    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)

    return ourURLs




def save_images(URLs, directory):

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, url in enumerate(URLs):
        savePath = os.path.join(directory, '{:06}.jpg'.format(i))

        try:
            ulib.urlretrieve(url, savePath)

        except:
            print('I failed with', url)









URLs = getURLs(url)


for url in URLs:
    print(url)

save_images(URLs, directory)