import urllib.request,urllib.response,urllib.error,urllib.parse
from urllib.request import urlopen
import xml.etree.ElementTree as et
import json
import ssl



# ignore ssl certificate error 
ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

#opening url
url=input("Enter URL : ")
html=urlopen(url,context=ctx).read()
data=html.decode()

sumCount=0
#json return dict into info
info=json.loads(data)

#retrieving data from dict

for i in info["comments"]:
    sumCount+=int(i["count"])

print(sumCount)

