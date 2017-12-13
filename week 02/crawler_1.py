import requests
from lxml import etree

url="http://econpy.pythonanywhere.com/ex/001.html"
page=requests.get(url)
html=page.text
# print(html)

selector = etree.HTML(html)

buyer=selector.xpath('//div[@title="buyer-name"]/text()')
prices=selector.xpath('//span[@class="item-price"]/text()')

print (buyer)
print (prices)
