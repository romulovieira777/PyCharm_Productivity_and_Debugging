"""
Created on June 03, 2022

@author: romulo
"""

# Master degree required.
# More than 2 years of experience.
from facebook_business.adobjects import experience

degree = input("What is your degree? Master, Bachelor or PhD? ")
experience = input("How many years of experience do you have? ")

if degree == "Master" or degree == "master" or degree == "Phd" or degree == "phd":
    if int(experience) >= 2:
        print("You are accepted for the interview")
    else:
        print("You don't have enough experience'")
else:
    print("You don't have the required degree")
