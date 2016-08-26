import vsDefense

def main():
    # html = webscrape.OpenURl("http://www.cbssports.com/fantasy/football/stats/posvsdef/")
    # print(html)

    results = vsDefense.QBvsDefense()
    results2 = vsDefense.RBvsDefense()
    print(results)
    print(results2)

if __name__ == "__main__":
    main()
