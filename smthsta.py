#coding=gb2312
from urllib.error import URLError,HTTPError  
import urllib.request  
import urllib.parse
import re
import time
url='http://www.newsmth.net/bbsdoc.php?board=OurEstate'
url2='http://www.newsmth.net/'


t='D:\\'
t+=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
t+='.csv'
f=open(t,'a',encoding='gb2312')
while (1==1) :
    try:  
        full_url=urllib.request.Request(url)  
        full_url2=urllib.request.Request(url2)  
        response=urllib.request.urlopen(full_url)   #open=urlopen  
        response2=urllib.request.urlopen(full_url2)   #open=urlopen  
        the_page=response.read()
        the_page2=response2.read()
        s=the_page.decode('gb2312')
        s2=the_page2.decode('gb2312')
        r=re.search(r'<title>\s*(.*)\s*</title>.*在线\s*(\d+)\s*人.*最高\s*(\d+)\s*人',s,re.DOTALL)
        r2=re.search(r'当前论坛上总共有\s*<span.*>\s*(\d+)\s*</span>\s*人在线.*其中注册用户\s*<span.*>\s*(\d+)\s*</span>\s*人.*访客\s*<span.*>\s*(\d+)\s*</span>\s*人',s2,re.DOTALL)
        f.write(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+',')
        f.write(r2.group(1)+',')
        f.write(r2.group(2)+',')
        f.write(r2.group(3)+',')
        f.write(r.group(1)+',')
        f.write(r.group(2)+',')
        f.write(r.group(3)+'\n')
    except HTTPError as e:  
        print('Error code:',e.code)   
    except URLError as e:  
        print('Reason',e.reason)
    time.sleep(5)
    f.flush()
f.close()
