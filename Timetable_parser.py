import urllib2
import xmltodict

file = urllib2.urlopen('http://www.ding.eu/ding2/XML_DM_REQUEST?language=de&itdLPxx_dmRefresh=1&typeInfo_dm=stopID&nameInfo_dm=9001353&deleteAssignedStops_dm=1&useRealtime=1&mode=direct&line=DIN:87001:%20:R')# Magirusstrasse richtugn stad

data = file.read()
file.close()

data = xmltodict.parse(data)
test=data['itdRequest']['itdDepartureMonitorRequest'] ['itdDepartureList']['itdDeparture']

for c in range(0,2):
    print(test[c]['@countdown'])
#key in a and value == a[key]
#


#def homepage(request):
file = urllib2.urlopen('http://www.ding.eu/ding2/XML_DM_REQUEST?language=de&itdLPxx_dmRefresh=1&typeInfo_dm=stopID&nameInfo_dm=9001311&deleteAssignedStops_dm=1&useRealtime=1&mode=direct&line=DIN:87013:%20:H')#Koenigsstrassee richtugn Uni
data = file.read()
file.close()

data = xmltodict.parse(data)
test=data['itdRequest']['itdDepartureMonitorRequest'] ['itdDepartureList']['itdDeparture']

for c in range(0,2):
    print(test[c]['@countdown'])
#key in a and value == a[key]
#

#list=["12","13","  " ]                                                                                                          
#print(list[1][1])
   # return 
