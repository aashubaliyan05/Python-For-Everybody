from urllib.request import urlopen
import xml.etree.ElementTree as et
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter URL : ")
html=urlopen(url,context=ctx,).read()
data=html.decode()


sumCount=0
tree=et.fromstring(data)
counts = tree.findall('.//count')
for ele in counts:
    sumCount+=int(ele.text)
print(sumCount)

