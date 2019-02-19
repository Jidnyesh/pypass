"""
This is a module to generate random password of different length for your project
download this or clone and then from pypass import randompasswordgenerator
"""

import random

#String module used to get all the upper and lower alphabet in ascii
import string

#Declaring strings used in password
special_symbols = "!@#$%^&*()_+{}|:<>?-=[]\;',./"
alphabets = string.ascii_letters
numbers = string.digits



def randompasswordgenerator():

    #Taking inputs for information of password
    n = int(input("Enter the length of password:"))
    print("1:Alpha \n2:Alpha numeric \n3:Aplha symbol numeric")
    choice = int(input("Choose the type of password:\n"))

    #Making a empty list to store passwords
    passw = []

    #Setting value of str_list to combination according to choice
    if choice == 1:
        str_list = alphabets
    elif choice == 2:
        str_list = alphabets + numbers
    elif choice == 3:
        str_list = special_symbols + alphabets + numbers

    for x in range(n):
        rnd = random.choice(str_list)
        passw.append(rnd)

    password = "".join(passw)

    print(password)

#Function call
if __name__=="__main__":
    randompasswordgenerator()
