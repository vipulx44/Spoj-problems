import re
import urllib.request
import time
stime=time.time()
url="https://www.google.com/finance?q="
'''user=input("Enter Company name: ").upper()'''
url=url+'FB'
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
st=re.search('meta itemprop="price"',data1)
print("The stock value is:"+data1[st.start()+39:st.start()+45])
print("%s seconds" % (time.time()-stime))
input("Press any button to exit") 
