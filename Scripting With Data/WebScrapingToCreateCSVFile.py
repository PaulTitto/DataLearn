from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=samsung%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", { "class": "_2kHMtA"})
container = containers[0]
price = container.findAll("div", {"class":"col col-5-12 nlI3QM"})
ratings = container.findAll("span",{"class":"_2_R_DZ"})


filename = "products.csv"
f =open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class":"col col-5-12 nlI3QM"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("span",{"class":"_2_R_DZ"})
    rating = rating_container[0].text
    print(f"Product_Name : {product_name}")
    print(f"Price : {price}")
    print(f"Ratings : {rating}")
