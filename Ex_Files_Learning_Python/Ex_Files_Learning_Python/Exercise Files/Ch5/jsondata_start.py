# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)

  # now we can access the contents of the JSON like any other Python object
  print(theJSON['metadata']['title'])

  
  # output the number of events, plus the magnitude and each event name  
  print(theJSON['metadata']['count'])


  # for each event, print the place where it occurred
  for jsonData in theJSON['features']:
    print(jsonData['properties']['place'])

  # print the events that only have a magnitude greater than 4
  for jsonData in theJSON['features']:
    if(jsonData['properties']['mag'] > 4):
      print(jsonData['properties']['mag'], jsonData['properties']['place'])
      
  # print only the events where at least 1 person reported feeling something
  for jsonData in theJSON['features']:
    fell = jsonData['properties']['felt']
    if(fell != None):
      if(fell > 0):
        print("%2.1f" % jsonData["properties"]["mag"], jsonData["properties"]["place"], " reported " + str(fell) + " times")

def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if webUrl.getcode() == 200:
    printResults(webUrl.read())

if __name__ == "__main__":
  main()
