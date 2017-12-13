import io
import sys
import urllib.request
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

res=urllib.request.urlopen('http://www.ynu.edu.cn/xykx.htm')
html=res.read()
selector = etree.HTML(html)

urls=selector.xpath('//a[@target="_blank"]/@href')
pages = selector.xpath('//a[@target="_blank"]/text()')

for url in urls:
    if 'www.news.ynu.edu.cn'  in url:
        response = urllib.request.urlopen(url)
        sub_html = response.read()
        sub_selector = etree.HTML(sub_html)

        title = sub_selector.xpath('//div[@class="atitle"]/text()')
        print(title[0])

        text = sub_selector.xpath('//div[@class="acontent"]/p/span/text()')
        print(''.join(text))


