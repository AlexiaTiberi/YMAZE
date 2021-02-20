#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import usefull stuff
import csv

#defining the analysis function
def ymaze():
    with open("ymazeanalysis.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("enter the animal code, then the abc string")
        animal = input("Enter animal code: ")
        str = input("Enter the abc string, no spaces, from y-maze: ")
        if str.isalpha():
            if "a" and "b" and "c" in str: 
                print ("you have inserted an alphabetic string, no spaces, as asked \n")
                str_counta = str.count('a')
                str_countb = str.count('b')
                str_countc = str.count('c')
                totnumentr=str_counta+str_countb+str_countc
                percA=(str_counta/totnumentr)*100
                percB=(str_countb/totnumentr)*100
                percC=(str_countc/totnumentr)*100
                #counting alter
                str_count1 = str.count('abc')
                str_count2 = str.count('bca')
                str_count3 = str.count('bac')
                str_count4 = str.count('acb')
                str_count5 = str.count('cab')
                str_count6 = str.count('cba')
                alt=str_count1+ str_count2+str_count3+str_count4+str_count5+str_count6
                altentr = 100*(alt/totnumentr)
        writer.writerow([animal, str, totnumentr, alt, altentr])
        print("you have entered {} = {} \n".format(animal, str))       
#create the csv file and write headers        
with open("ymazeanalysis.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Animal Code", "abc String from Y maze test", "Total number of entries", "Number of correct alternation", "Spontaneous Alternation %"])
#main loop
    active = True
while active:
    user = input("type n to add a new animal/string or type quit to exit the program: \n").lower()
    if user == "n":
        ymaze()
    elif user == "quit":
        active = False
    else:
        print ("Enter either the word quit or n: \n")
    
           
