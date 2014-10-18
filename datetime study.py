'''
Datetime study
Create date object
Create today's date object
Print day, month, year of the date object
'''
from datetime import *

def getMonth(month):
	monthDict = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
	return monthDict[month]
def getDay(day):
	dayDict = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
	return dayDict[day]
today = date.today()
print "Today's date =", today
print "This year is", today.year
print "This month is", getMonth(today.month)
print "Next month is", getMonth(today.month+1)
print "The day of the month is", getDay(today.weekday())