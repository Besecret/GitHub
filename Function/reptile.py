import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for flag in imglist:
        urllib.urlretrieve(flag,'%s.jpg' % x)
        x=x+1

html=getHtml("http://tieba.baidu.com/p/4049194967")
getImg(html)
