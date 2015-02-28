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
root = etree.fromstring(page.content) # HtmlElement
#root = etree.fromstring(page.content) # lxml.etree._Element
#decoded_page = page.content.decode("utf8") # decode the page content in expected UTF-8

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
	#print root.xpath('/service/'+service+'/line/text/text()')
	lines = root.xpath('/service/'+service+'/line/name/text()')
	status = root.xpath('/service/'+service+'/line/status/text()')
	#TODO remove gross hack where we assume <text> is always the next sibling to status	
	
	detail_text = []
	for t in root.xpath('/service/'+service+'/line/status/following-sibling::*[1]/text()'):
		#print t + '\r\r----------------\r\r'
		if(t):
			detail_text.append(t)
			print detail_text[-1]
		else:
			detail_text.append('')
			print detail_text[-1]

	service_data[service] = {}
	for i in range(len(lines)):
		print str(i)+ '  ' + ('present' if (i in detail_text) else 'absent') +'\r'
		service_data[service][lines[i]] = status[i],(detail_text[i] if (i in detail_text) else '') 
		#service_data[service][lines[i]] = status[i],('' if (detail_text[i].isempty()) else detail_text[i]) 
		#service_data[service][lines[i]] = status[i] #this works

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
    app.debug = True
    #app.run()
    app.run(host='104.131.116.94')





