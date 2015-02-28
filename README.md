# mta-service-status
Ingest data from the MTA's XML feed and render in a human readable format within a web browser. http://mta.info/status/serviceStatus.txt
import necessary packages, there may be dependancies
set up python virtualenv to compartmentalize package dependancies
globally install these
apt-get install libxml2-dev libxslt1-dev python-dev
install these with the virtualenv active to use the proper python
pip install requests
pip install lxml
pip install Flask
pip install gunicorn
the later two are included in the virtenv, however the apt-get portions are required
