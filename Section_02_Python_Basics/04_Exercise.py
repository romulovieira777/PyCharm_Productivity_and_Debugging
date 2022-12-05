"""
Created on June 03, 2022

@author: romulo
"""

# NumberA and NumberB
# Subtract numberA from numberB
# Print the result

numberA = float(input("First number is: "))
numberB = float(input("Second number is: "))

sub = numberA - numberB

print("Result: " + str(sub))

if sub < 0:
    print("Negative Number")
else:
    print("Positive Number")
