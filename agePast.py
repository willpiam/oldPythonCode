"""
JUST A QUICK PROGRAM FOR MESSING ABOUT WITH NUMBERS 
"""
import time
#stage one colect info
print "Welcome user. What is your name?"
name = str(raw_input())
print "Please enter the current year."
ynow = int(raw_input())#current year... ynow stands for year now
print "And what year were you born?"
yborn = int(raw_input()) #year user was born

uAge = ynow-yborn #users age
print "Great! So the current year is",ynow,"and you are", uAge,"."

print "Explanation: my task is to help you find out what year it"
print "was (or will be) when a specific person was or will be your age."
print "."
print "."#dots have no function but look good (may get ride of them later
print "."
print "So, who is your person of interest?"
POI = str(raw_input()) #POI stands for person of intrest

print "GREAT! And in what year was" , POI, "born?"
yPOIb = int(raw_input())

agePOI = ynow-yPOIb
#print agePOI

print "So", POI,"is", agePOI,"years in age."

yItWouldBe = yPOIb + uAge
if uAge > agePOI:
    print "In", yItWouldBe, POI ,"will be your current age"
else:
    print "In", yItWouldBe, POI ,"would have been your age"
print "."
print "."
print "."

print "Press ENTER to close my program."
end = str(raw_input())
print ""
print ""
print ""
print ""
print ""
print "GOOD BYE", name
time.sleep(3)

