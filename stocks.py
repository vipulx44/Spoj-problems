import re
import urllib.request
import time
stime=time.time()
url="https://www.google.com/finance?q="

"""user=input("Enter Company name: ").upper()"""
url=url+"FB"
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
st=re.search('meta itemprop="price"',data1)
st=data1[st.start():st.start()+50]
act=re.search('content="',st)
start=act.end()
act=re.search('/',st)
end=act.end()-3
print("The stock value is:"+st[start:end])
print("%s seconds" % (time.time()-stime))
input("Press any button to exit") 
