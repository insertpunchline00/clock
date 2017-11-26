import urllib2
import xmltodict

def parse_timetable ():
    file = urllib2.urlopen('http://www.ding.eu/ding2/XML_DM_REQUEST?language=de&itdLPxx_dmRefresh=1&typeInfo_dm=stopID&nameInfo_dm=9001353&deleteAssignedStops_dm=1&useRealtime=1&mode=direct&line=DIN:87001:%20:R')# Magirusstrasse richtugn stad

    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    times_magirus=999

    if type(data['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']) !=type(None):
        magirus=data['itdRequest']['itdDepartureMonitorRequest'] ['itdDepartureList']['itdDeparture']
        times_magirus=(magirus[0]['@countdown'])
        print(times_magirus)
    #key in a and value == a[key]
    #


    #def homepage(request):
    file2 = urllib2.urlopen('http://www.ding.eu/ding2/XML_DM_REQUEST?language=de&itdLPxx_dmRefresh=1&typeInfo_dm=stopID&nameInfo_dm=9001311&deleteAssignedStops_dm=1&useRealtime=1&mode=direct&line=DIN:87013:%20:H')#Koenigsstrassee richtugn Uni

    data2 = file2.read()
    file2.close()


    data2 = xmltodict.parse(data2)
    times_koenigs=999

    if type(data2['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']) !=type(None):
        koenigs=data2['itdRequest']['itdDepartureMonitorRequest'] ['itdDepartureList']['itdDeparture']
        times_koenigs=(koenigs[0]['@countdown'])
   
    return times_magirus, times_koenigs
    
#key in a and value == a[key]
#

#list=["12","13","  " ]                                                                                                          
#print(list[1][1])
   # return 
