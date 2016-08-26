# import webscrape
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
import vsDefense

def main():
    # html = webscrape.OpenURl("http://www.cbssports.com/fantasy/football/stats/posvsdef/")
    # print(html)

    results = vsDefense.QBvsDefense()

    print(results)

if __name__ == "__main__":
    main()
