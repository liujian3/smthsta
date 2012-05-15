import urllib.request
import sys
 
#cookie = http.cookiejar.CookieJar()                                        
#cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(cjhdr)
 
url = "http://www.newsmth.net/nForum/#!board/GOLD"
postdata = urllib.parse.urlencode({'email': '112@gmail.com', 'password': '111123', 'Submit':''})
postdata = postdata.encode('utf-8')
 
res = urllib.request.urlopen(url,postdata)
f=open("1.txt",'w')
f.write(res.read().decode('gbk'))
 
if( res.status != 200 ):
    exit()
 
print('ok')