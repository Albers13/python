import urllib.request
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connection, grabs the page
uClient = urllib.request.urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
    #gets brand
    try:
        brand_container = container.findAll("div", {"class":"item-branding"})
        brand = brand_container[0].a.img["title"]
    except:
        brand = "NOT AVAILABLE"

    #gets title
    try:
        title_container = container.findAll("a", {"class":"item-title"})
        product_title = title_container[0].text
    except:
        product_title = "NOT AVAILABLE"

    #gets price
    try:
        price_container = container.findAll("div",{"class":"item-action"})
        price1 = price_container[0].strong.text
        price2 = price_container[0].sup.text
        price = "$" + price1 + price2
    except:
        price = "NOT AVAILABLE"

    print (brand + ": " + product_title + ": Price: " + price + "\n")
