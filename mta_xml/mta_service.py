#import necessary packages, there may be dependancies
#apt-get install libxml2-dev libxslt1-dev python-dev
#pip install requests
#pip install lxml
#pip install Flask
#the later two are included in the virtenv, however the apt-get portions are required

import requests
#from io import StringIO, BytesIO
#from lxml import html, etree
from lxml import etree
from flask import Flask, render_template

app = Flask(__name__)

mta_url = 'http://mta.info/status/serviceStatus.txt'

page = requests.get(mta_url) #contains content from xml status
#print(page.text) # make sure this works
root = etree.fromstring(page.content) # HtmlElement
#root = etree.fromstring(page.content) # lxml.etree._Element
#decoded_page = page.content.decode("utf8") # decode the page content in expected UTF-8
#root = etree.parse(StringIO(unicode(decoded_page)))
#print(root.getroot())

#prints all of XML elements recursively
#for elt in root.getiterator():
#	print elt.tag

#same as above, but does not us a deprecated function
#print out via iterator http://infohost.nmt.edu/tcc/help/pubs/pylxml/web/ElementTree-getiterator.html
#for elt in doc.iter():
#     print elt.tag

#pull out XML blocks for each MTA service
#subway
#bus
#BT (Bridge/Tunnel)
#LIRR
#MetroNorth

#possible statuses include 'PLANNED WORK', 'GOOD SERVICE', 'PLANNED WORK', 



#list of services ['subway','bus','BT','LIRR','MetroNorth']


services = ['subway','bus','BT','LIRR','MetroNorth']
service_data = {}

for service in services:
	#print root.xpath('/service/'+service+'/line/name/text()')
	lines = root.xpath('/service/'+service+'/line/name/text()')
	status = root.xpath('/service/'+service+'/line/status/text()')
	service_data[service] = {}
	for i in range(len(lines)):
		service_data[service][lines[i]] = status[i]

#print(service_data)
	#stuff {subway: {'1,2,3': 'GOOD STATUS'}}

@app.route('/')
def get_service_data():
    #return 'Hello World!'
    #return '"'+service_data+'"'
    #print(service_data)
    #return render_template('status.html', service_data=service_data)
    return render_template('index.html', service_data=service_data)

if __name__ == '__main__':
    #app.debug = True
    #app.run()
    app.run(host='104.131.116.94')





