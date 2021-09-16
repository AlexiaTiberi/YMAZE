#!/usr/bin/env python
# coding: utf-8

# In[15]:
#import usefull stuff
import csv
import os
#defining the analysis function
def ymaze():
    with open("ymazeanalysis.csv", mode="a+", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        animal = input("Enter animal code: \n")
        abc = input("Enter the abc string, no spaces, from y-maze (ex:abcbabcbacb): \n")
        if abc.isalpha():
            if "a" or "b" or "c" in abc: 
                str_counta = abc.count('a')
                str_countb = abc.count('b')
                str_countc = abc.count('c')
                totnumentr=len(abc)
                percA=(str_counta/totnumentr)*100
                percB=(str_countb/totnumentr)*100
                percC=(str_countc/totnumentr)*100
                #counting alter
                str_count1 = abc.count('abc')
                str_count2 = abc.count('bca')
                str_count3 = abc.count('bac')
                str_count4 = abc.count('acb')
                str_count5 = abc.count('cab')
                str_count6 = abc.count('cba')
                alt=str_count1+ str_count2+str_count3+str_count4+str_count5+str_count6
                altentr = 100*(alt/(totnumentr-2))
        writer.writerow([animal, abc, totnumentr, alt, altentr, percA, percB, percC])
        print("you have entered {} = {} \n".format(animal, abc))       
#main loop
try:
    user_cwd = input("Please insert directory where you want your results to be saved ex: C:\\test \nor quit the program by typing quit\n")
    if user_cwd == "quit":
        print("Thank you for using my code!\n")
    else:    
        os.chdir(r"{}".format(user_cwd)) 
        #create the csv file and write headers        
        with open("ymazeanalysis.csv", mode="x", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Animal Code", "abc String from Y maze test", "Total number of entries", "Number of correct alternation", "Spontaneous Alternation %", "percentage of A","percentage of B","percentage of C"])
        active = True
        while active:
            user = input("type n to add a new animal/string or type quit to exit the program: \n").lower()
            if user == "n":
                ymaze()
            elif user == "quit":
                active = False
                print("Thank you for using my code!\n")
            else:
                print ("Enter either the word quit or n: \n")
except FileNotFoundError:
    print("You did not insert a valid directory\nYou have to copy and paste the directory from the address bar! \n")
           



