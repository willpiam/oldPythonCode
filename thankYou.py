#program is to write xmas thankyou cards based on two variables giver name and gift name

name = raw_input("Who do you want to thank?")
userName = raw_input("What is your name?")

print "What did", name,"get you?" 
gift = raw_input(" ")
print gift

from random import randint
greet = int(randint(1,2))

print greet

if greet == "1":
    greeting = "Dear"
    dismiss = "Lots of love "
else: greeting = "Hey"
dismiss = "With love "




print greeting," ", name,","

print "I hope your christmas was as great as ours. Thank you so much for the gift."

print "I really like my", gift,".  Have a happy New Year!"

print dismiss, " ", userName

i = 1
while i > -1:
    i = i + 0.1 #this thing is to stop the program from closing 

