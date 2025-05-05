#This program is to generate a password of given length using name and date of birth
#The obtained password will be stored in a txt file named as wordlist.txt and this will be word list used for initiating the attack

import random
import os
import time

#function using to generate random password from the given input
def random_password(name,dob,length):
    new = name + dob
    temp = list(new)
    passwords = []

    random.seed(time.time())#always gives out unique password
    for i in range(100):
        random.shuffle(temp)
        passwords.append(''.join(temp[:length]))
    generate_wordlist(passwords)

#saves the generated password inside a txt file from a list
def generate_wordlist(arr):

    if os.path.exists("wordlist.txt"):
        #checking if wordlist.txt file exsist if it does opening in append mode
        f = open("wordlist.txt","a")
        for i in range(100):
            f.write(str(arr[i]) + "\n")
        f.close()
    else:
        f = open("wordlist.txt","w")
        for i in range(100):
            f.write(str(arr[i]) + "\n")
        f.close()

name = input()
date = input()
length = int(input())
random_password(name,date,length)
