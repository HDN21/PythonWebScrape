import webscrape
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    # html = webscrape.OpenURl("http://www.cbssports.com/fantasy/football/stats/posvsdef/")
    # print(html)

    # Create a variable with the URL to this tutorial
    url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
    #url = 'http://www.cbssports.com/fantasy/football/stats/posvsdef/'
    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text, 'lxml')

    # Create four variables to score the scraped data in
    first_name = []
    last_name = []
    age = []
    preTestScore = []
    postTestScore = []

    # Create an object of the first object that is class=dataframe
    table = soup.find(class_='dataframe')
    #table = soup.find(class_='data compact')
    # Find all the <tr> tag pairs, skip the first one, then for each.
    for row in table.find_all('tr')[1:]:
        # Create a variable of all the <td> tag pairs in each <tr> tag pair,
        col = row.find_all('td')

        # Create a variable of the string inside 1st <td> tag pair,
        column_1 = col[0].string.strip()
        # and append it to first_name variable
        first_name.append(column_1)

        # Create a variable of the string inside 2nd <td> tag pair,
        column_2 = col[1].string.strip()
        # and append it to last_name variable
        last_name.append(column_2)

        # Create a variable of the string inside 3rd <td> tag pair,
        column_3 = col[2].string.strip()
        # and append it to age variable
        age.append(column_3)

        # Create a variable of the string inside 4th <td> tag pair,
        column_4 = col[3].string.strip()
        # and append it to preTestScore variable
        preTestScore.append(column_4)

        # Create a variable of the string inside 5th <td> tag pair,
        column_5 = col[4].string.strip()
        # and append it to postTestScore variable
        postTestScore.append(column_5)

    # Create a variable of the value of the columns
    columns = {'first_name': first_name, 'last_name': last_name, 'age': age, 'preTestScore': preTestScore,
               'postTestScore': postTestScore}
    # Create a dataframe from the columns variable
    df = pd.DataFrame(columns)
    print(df)

if __name__ == "__main__":
    main()
