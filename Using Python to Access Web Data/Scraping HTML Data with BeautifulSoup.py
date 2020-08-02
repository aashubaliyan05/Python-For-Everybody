from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#opening url
url = "http://py4e-data.dr-chuck.net/comments_780918.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#extracting all tr tags
tags = soup('tr')
tag=[]
sumNo=0

#adding to list
for i in tags:
    tag.append(str(i))
    print(tag)

#finding numbers
for nos in tag:
    no=re.findall("[0-9]+",nos)
    for i in no:
        sumNo+=int(i)
print(sumNo)
