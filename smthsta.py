#coding=gb2312
import urllib.request
import sys
import re

#cookie = http.cookiejar.CookieJar()                                        
#cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(cjhdr)
 
url = "http://www.newsmth.net/bbsdoc.php?board=GOLD"
#postdata = urllib.parse.urlencode({'email': '112@gmail.com', 'password': '111123', 'Submit':''})
#postdata = postdata.encode('utf-8')
 
#res = urllib.request.urlopen(url)
#resstr = str(res.read().decode('gb2312'))
#print(resstr)
pat = re.compile(r'[\u4e00-\u9fa5] ')
mat = pat.match(r'\xc8\xcb')
print(mat)