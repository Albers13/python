import urllib.request
from bs4 import BeautifulSoup as soup
import csv
import datetime

stock_url = 'https://www.marketwatch.com/investing/index/djia'

uClient = urllib.request.urlopen(stock_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll('div', class_='template template--aside')

container_rows = containers[2].div.div.table.tbody

rows = container_rows.findAll('tr', class_='table__row')

row_count = 0
stocks = []
now = datetime.datetime.now()
date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

for row in rows:
    try:
        company = row.td.text
    except:
        company = 'null'

    try:
        price_row = rows[row_count].findAll('td', class_="table__cell w15 ignore-color")
        price = price_row[0].text
    except:
        price = 'null'

    try:
        change_row = rows[row_count].findAll('td', class_="table__cell w15")
        change = change_row[0].text
        percent = change_row[1].text
    except:
        change = 'null'

    stock = [company, price, change, percent, date]
    stocks.append(stock)
    row_count += 1


with open('stocks.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(stocks)

writeFile.close()
