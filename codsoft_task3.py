import random

string="qwertyuiopasdfghjklmnbvcxzQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*^"
s=int(input("Enter the length of the password:-"))
password=""
for k in range(s):
    f= int(random.randint(0,59))
    password+=string[f]
print(f"Your Generated Password is:- {password}")
