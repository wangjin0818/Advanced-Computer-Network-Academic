import urllib2
from lxml import etree

url = 'http://www.ynu.edu.cn'
response = urllib2.urlopen(url)  
html = response.read()  
# print html

