from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter URL : ")
count=int(input("Enter count : "))
position=int(input("Enter position : "))

lastName=[]

#function to follow the links
def extractLastName(count,position,url):
    if(count>0):
        lastName.clear()
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        urls=[]
        tags=soup('a')
        itr=0
        for tag in tags:
            
            if(itr<=position):
                urls.append(tag.get("href",None))
                lastName.append(tag.contents[0])
            else:
                break
        count-=1
        url=urls[position-1]
        print("Retrieving : ",url)
        return extractLastName(count,position,url)
    else:
        print(lastName[position-1])


extractLastName(count,position,url)