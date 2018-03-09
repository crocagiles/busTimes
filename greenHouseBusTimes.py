#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:59:02 2017

@author: gholbrow
"""


def greenHouseBusTimes():
    import urllib
    import xml.etree.ElementTree as ET

    busTimes = []

    url23 = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&stopId=14199'

    tree23 = ET.parse(urllib.urlopen(url23))
    root23 = tree23.getroot()
    predictions23 = root23.find('predictions')
    direction23 = predictions23.find('direction')

    for t in range(1):
        if direction23 is None: #Continue if bus is not running (night)
            continue
        prediction23 = direction23.findall('prediction')

        numPredictions = []

        for i in range(len(prediction23)):
            next23Min = prediction23[i].attrib['minutes']
            numPredictions.append(next23Min)

        if len(numPredictions) == 1:
            if int(next23Min) == 1: #check for plural number of minutes
                disp23 =["23 in " + numPredictions[0] + " minute"]
            else:    
                disp23 =["23 in " + numPredictions[0] + " minutes"]
        else:
            if int(next23Min) == 1: #check for plural number of minutes
                disp23 = ["23 in " + numPredictions[0] + " minute",  "& " + numPredictions[1] + " minutes"]
            else:
                disp23 = ["23 in " + numPredictions[0] + " minutes", "& " + numPredictions[1] + " minutes"]

        busTimes.append(disp23)


    url1449 = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&stopId=15613'

    tree1449 = ET.parse(urllib.urlopen(url1449))
    root1449 = tree1449.getroot()
    predictions1449 = root1449.findall('predictions') 



    for i in range(len(predictions1449)):
        
        fullRouteInfo  = predictions1449[i].attrib
        busNum         = fullRouteInfo['routeTag']           # gives bus number for iteration i
        direction1449  = predictions1449[i].find('direction')  # 1 level deeper
        if direction1449 is None:
            continue
        prediction1449 = direction1449.findall('prediction')   # 1 level deeper - gives a bunch of next bus times
        next1449 = prediction1449[0].attrib['minutes']

        
        if len(prediction1449) > 1:
            following1449 = prediction1449[1].attrib['minutes'] # 0 index gives closest bus, attrib gives dict, minutes gives key value
        else:
            following1449 = 0
            
        if following1449 !=0:    
            if int(next1449) == 1: # change plural minute to singular
                addToBusTimes  = ([busNum + ' in ' + next1449 + ' minute' , "& " + following1449 + " minutes"])
            else:
                addToBusTimes  = ([busNum + ' in ' + next1449 + ' minutes', "& " +following1449 + " minutes"] )
                                  
        if following1449 == 0:   
            if int(next1449) == 1: # change plural minute to singular
                addToBusTimes  = ([busNum + ' in ' + next1449 + ' minute'])
            else:
                addToBusTimes  = ([busNum + ' in ' + next1449 + ' minutes'])


       
        busTimes.append(addToBusTimes)

        
    
    if not busTimes:
        busTimes = 'Zach is a nerd'

    return(busTimes)
    

