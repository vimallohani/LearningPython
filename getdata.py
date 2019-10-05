import requests
from bs4 import BeautifulSoup
request=requests.get("https://www.amazon.in/Decals-Design-Designer-Sticker-Vinyl/dp/B019T1DPMU/ref=pd_rhf_se_s_qp_1_1?_encoding=UTF8&pd_rd_i=B019T1DPMU&pd_rd_r=DH0EMYGYCYC2P99ZJJ3A&pd_rd_w=POL3Y&pd_rd_wg=6oYDd&psc=1&refRID=DH0EMYGYCYC2P99ZJJ3A")
content=request.content

soup=BeautifulSoup(content,"html.parser")
# print(soup)
#<span id="priceblock_ourprice" class="a-size-medium a-color-price"><span class="currencyINR"></span> 135.00</span>
data=soup.find("span",{"id":"priceblock_ourprice", "class":"a-size-medium a-color-price"})
print(data.text.strip())

input()


# import sys
# x=sys.modules.keys()
# print(x)













