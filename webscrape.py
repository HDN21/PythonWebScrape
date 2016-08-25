from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

def OpenURl (str):
    r = urlopen(str)
    soup = BeautifulSoup(r, "html.parser")

    return(soup.find("table", { "class" : "data compact" }))
