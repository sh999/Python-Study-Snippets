'''
Tasks:
Use openweathermap API to display weather for a zip code 
'''

from urllib2 import Request, urlopen, URLError
request = Request("http://api.openweathermap.org/data/2.5/weather?zip=90210,us")
try:
   response = urlopen(request)
   rawOutput = response.read()
except URLError, e:
   print "Error in request! Code =",e
print rawOutput