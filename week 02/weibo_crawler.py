#coding:utf-8
import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

user_id = int('your sina id here')

cookie = {"Cookie": "YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; login_sid_t=a64b781eb709f3390c97cf14aea7ad5f; YF-Page-G0\
=82cdcdfb16327a659fbb60cc9368fb19; _s_tentry=passport.weibo.com; Apache=3011179794927.168.1457573735242\
; SINAGLOBAL=3011179794927.168.1457573735242; ULV=1457573735246:1:1:1:3011179794927.168.1457573735242\
:; SUS=SID-2922145997-1457573747-GZ-9brhu-5e69f3d020f2620f329e0a933fb483be; SUE=es%3D2d9a3afc6b77fec1704bd37f6edfc4a1\
%26ev%3Dv1%26es2%3Da7b609f53d9812ae82c9904eed8f6743%26rs0%3DTY8kLFTTRcDgoum%252FI4uV3Jns%252F5uwTC%252FgjXJqG3oEd9uIj4jntKZTJ\
%252Bq6TzJGZLAXEM7tz3A5vqtQ5DtVScLFuxZwQ%252BcmQYHao0orpoAgGwybMT9P%252BMDo9BdLDwYEQfG2UP1kJow%252FG\
%252FiP5%252FIbbz2rCLFhR%252BJB2GnlhOn%252BKad4%252FbY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1457573747%26et\
%3D1457660147%26d%3Dc909%26i%3D83be%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D25%26st%3D0%26uid%3D2922145997\
%26name%3D13308859600%26nick%3D%25E7%2594%25A8%25E6%2588%25B72922145997%26fmp%3D%26lcp%3D2013-04-30%252022\
%253A19%253A23; SUB=_2A2575L8jDeRxGeRH6VAQ9CvFwjuIHXVYk5frrDV8PUNbuNBeLRj2kW9LHeucHlvnIBn8EId12IQ5OMaymHFLEg\
..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFAPkz3FWK7LdYn5.MRSiBZ5JpX5K2t; SUHB=0IIllWyIgsqjw8; ALF=1489109746\
; SSOLoginState=1457573747; un=13308859600; wvr=6; YF-V5-G0=a9b587b1791ab233f24db4e09dad383c; wb_feed_unfolded_2922145997\
=1"}

url = 'http://weibo.cn/u/%d?filter=1&amp;page=1'%user_id

html = requests.get(url, cookies=cookie).content
# print(html)
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

print pageNum

result = ""
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1, pageNum+1):

    ## 获取lxml页面
    url = 'http://weibo.cn/u/%d?filter=1&amp;page=%d'% (user_id, page)
    lxml = requests.get(url, cookies=cookie).content

    # 文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        if word_count >= 4:
            text = "%d :"%(word_count-3) + text+"\n\n"
        else:
            text = text + "\n\n"
        result = result + text
        print result
        word_count += 1

    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a', href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
    first = 0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'], cookies=cookie).url)
        image_count += 1

fo_path = os.path.join('data', str(user_id))
if not os.path.exists(fo_path):
    os.mkdir(fo_path)

fo = open(fo_path, 'wb')
word_path = os.getcwd() + '%d'%user_id
print u'文字微博爬取完成'

link = ""
fo2_path = os.path.join('data', str(user_id)+'_imageurls')
if not os.path.exists(fo_path):
    os.mkdir(fo_path)
for eachlink in urllist_set:
    link = link + eachlink + "\n"
fo2.write(link)

if not urllist_set:
    print u'该页面中不存在图片'
else:
  #下载图片,保存在当前目录的pythonimg文件夹下
    image_path=os.getcwd()+'/weibo_image'
    if os.path.exists(image_path) is False:
        os.mkdir(image_path)
    x=1
    for imgurl in urllist_set:
        temp= image_path + '/%s.jpg' % x
        print u'正在下载第%s张图片' % x
        try:
            urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(),temp)
        except:
            print u"该图片下载失败:%s"%imgurl
        x+=1
 
print u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path)
print u'微博图片爬取完毕，共%d张，保存路径%s'%(image_count-1,image_path)
