from bs4 import BeautifulSoup
from urllib.request import urlopen

def OpenURl (str):
    r = urlopen(str)
    soup = BeautifulSoup(r, "html.parser")

    return(soup.find("table", { "class" : "data compact" }))
