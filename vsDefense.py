import requests
from bs4 import BeautifulSoup
import pandas as pd

def QBvsDefense ():

# Create a variable with the URL to this tutorial
    #url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
    url = 'http://www.cbssports.com/fantasy/football/stats/posvsdef/'
    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text, 'lxml')

    # Create four variables to score the scraped data in
    rank = []
    team = []
    pAtt = []
    pCmp = []
    pYd = []
    pTd = []
    pInt = []
    pRating = []
    rAtt = []
    rYd = []
    rAvg = []
    rTd = []
    fmbl = []
    fpts = []

    # Create an object of the first object that is class=dataframe
    #table = soup.find(class_='dataframe')
    table = soup.find(class_='data compact')
    # Find all the <tr> tag pairs, skip the first one, then for each.
    for row in table.find_all('tr')[3:]:
        # Create a variable of all the <td> tag pairs in each <tr> tag pair,
        col = row.find_all('td')

        # Create a variable of the string inside 1st <td> tag pair,
        column_1 = col[0].string.strip()
        # and append it to first_name variable
        rank.append(column_1)

        # Create a variable of the string inside 2nd <td> tag pair,
        column_2 = col[1].string.strip()
        # and append it to last_name variable
        team.append(column_2)

        # Create a variable of the string inside 3rd <td> tag pair,
        column_3 = col[2].string.strip()
        # and append it to age variable
        pAtt.append(column_3)

        # Create a variable of the string inside 4th <td> tag pair,
        column_4 = col[3].string.strip()
        # and append it to preTestScore variable
        pCmp.append(column_4)

        # Create a variable of the string inside 5th <td> tag pair,
        column_5 = col[4].string.strip()
        # and append it to postTestScore variable
        pYd.append(column_5)

        # Create a variable of the string inside 6th <td> tag pair,
        column_6 = col[5].string.strip()
        # and append it to postTestScore variable
        pTd.append(column_6)

        # Create a variable of the string inside 7th <td> tag pair,
        column_7 = col[6].string.strip()
        # and append it to postTestScore variable
        pInt.append(column_7)

        # Create a variable of the string inside 8th <td> tag pair,
        column_8 = col[7].string.strip()
        # and append it to postTestScore variable
        pRating.append(column_8)

        # Create a variable of the string inside 9th <td> tag pair,
        column_9 = col[8].string.strip()
        # and append it to postTestScore variable
        rAtt.append(column_9)

        # Create a variable of the string inside 10th <td> tag pair,
        column_10 = col[9].string.strip()
        # and append it to postTestScore variable
        rYd.append(column_10)

        # Create a variable of the string inside 11th <td> tag pair,
        column_11 = col[10].string.strip()
        # and append it to postTestScore variable
        rAvg.append(column_11)

        # Create a variable of the string inside 12th <td> tag pair,
        column_12 = col[11].string.strip()
        # and append it to postTestScore variable
        rTd.append(column_12)

        # Create a variable of the string inside 13th <td> tag pair,
        column_13 = col[12].string.strip()
        # and append it to postTestScore variable
        fmbl.append(column_13)

        # Create a variable of the string inside 14th <td> tag pair,
        column_14 = col[13].string.strip()
        # and append it to postTestScore variable
        fpts.append(column_14)

    # Create a variable of the value of the columns
    columns = {'Rank': rank, 'Team': team, 'PAtt': pAtt, 'PCmp': pCmp, 'PYD': pYd, 'PTD': pTd, 'INT': pInt,
               'QBR': pRating, 'RAtt': rAtt, 'RYD': rYd, 'RAvg':rAvg, 'RTD':rTd, 'RFmbl': fmbl, 'FPTS': fpts}

    # Create a dataframe from the columns variable
    df = pd.DataFrame(columns)

    print(df)

    #target = df[df['Team']=="QB vs Browns"]
    #print(target)

    #print(df)


def RBvsDefense():
    # Create a variable with the URL to this tutorial
    # url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
    url = 'http://www.cbssports.com/fantasy/football/stats/posvsdef/RB/all/avg/standard/'
    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text, 'lxml')

    # Create four variables to score the scraped data in
    rank = []
    team = []
    rAtt = []
    rYd = []
    rAvg = []
    rTd = []
    recTargets = []
    recRecpt = []
    recYd = []
    recAvg = []
    recTd = []
    fmbl = []
    fpts = []

    # Create an object of the first object that is class=dataframe
    # table = soup.find(class_='dataframe')
    table = soup.find(class_='data compact')
    # Find all the <tr> tag pairs, skip the first one, then for each.
    for row in table.find_all('tr')[3:]:
        # Create a variable of all the <td> tag pairs in each <tr> tag pair,
        col = row.find_all('td')

        # Create a variable of the string inside 1st <td> tag pair,
        column_1 = col[0].string.strip()
        # and append it to first_name variable
        rank.append(column_1)

        # Create a variable of the string inside 2nd <td> tag pair,
        column_2 = col[1].string.strip()
        # and append it to last_name variable
        team.append(column_2)

        # Create a variable of the string inside 3rd <td> tag pair,
        column_3 = col[2].string.strip()
        # and append it to age variable
        rAtt.append(column_3)

        # Create a variable of the string inside 4th <td> tag pair,
        column_4 = col[3].string.strip()
        # and append it to preTestScore variable
        rYd.append(column_4)

        # Create a variable of the string inside 5th <td> tag pair,
        column_5 = col[4].string.strip()
        # and append it to postTestScore variable
        rAvg.append(column_5)

        # Create a variable of the string inside 6th <td> tag pair,
        column_6 = col[5].string.strip()
        # and append it to postTestScore variable
        rTd.append(column_6)

        # Create a variable of the string inside 7th <td> tag pair,
        column_7 = col[6].string.strip()
        # and append it to postTestScore variable
        recTargets.append(column_7)

        # Create a variable of the string inside 8th <td> tag pair,
        column_8 = col[7].string.strip()
        # and append it to postTestScore variable
        recRecpt.append(column_8)

        # Create a variable of the string inside 9th <td> tag pair,
        column_9 = col[8].string.strip()
        # and append it to postTestScore variable
        recYd.append(column_9)

        # Create a variable of the string inside 10th <td> tag pair,
        column_10 = col[9].string.strip()
        # and append it to postTestScore variable
        recAvg.append(column_10)

        # Create a variable of the string inside 11th <td> tag pair,
        column_11 = col[10].string.strip()
        # and append it to postTestScore variable
        recTd.append(column_11)

        # Create a variable of the string inside 12th <td> tag pair,
        column_12 = col[11].string.strip()
        # and append it to postTestScore variable
        fmbl.append(column_12)

        # Create a variable of the string inside 12th <td> tag pair,
        column_13 = col[12].string.strip()
        # and append it to postTestScore variable
        fpts.append(column_13)

    # Create a variable of the value of the columns
    columns = {'Rank': rank, 'Team': team, 'Att': rAtt, 'RushYD': rYd, 'Avg': rAvg, 'TD': rTd, 'Targets': recTargets,
               'Receptions': recRecpt, 'RecYD': recYd, 'RecAvg': recAvg, 'RecTD': recTd, 'FMBL': fmbl, 'FPTS': fpts}

    # Create a dataframe from the columns variable
    df = pd.DataFrame(columns)

    print(df)

    # target = df[df['Team']=="QB vs Browns"]
    # print(target)

    # print(df)