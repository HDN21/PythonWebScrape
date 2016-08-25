import webscrape

def main():
    html = webscrape.OpenURl("http://www.cbssports.com/fantasy/football/stats/posvsdef/")
    print(html)

if __name__ == "__main__":
    main()
