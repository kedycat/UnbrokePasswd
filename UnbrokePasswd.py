print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Creating a password >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
import random
passwd =[]
#choice of number or character or alhabet character 
def threechoice():
    a=random.randint(1,3)
    return a
#choice of upper or lower
def twochoice():
    b=random.randint(1,2)
    return b
#choice of alhpabet character
def alphabet():
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","v","x","y","z"]
    c=random.randint(0,25)
    return alph[c]
#choice of character
def character():
    char = ["<",">","!","#","$","%","&","?","_","€","."]
    d=random.randint(0,10)
    return char[d]
#choce of number
def number():
    num = [0,1,2,3,4,5,6,7,8,9]
    e=random.randint(0,9)
    return num[e]
#list to string 
def listToString(list):
    listToStr=''.join(map(str, list))
    print("Password Created:    		{}".format(listToStr))


i=0
passwdlen=int(input("Please enter the number of characters you want in your password:"))
#new password
while(i<passwdlen):
    choose=threechoice()
    if choose==1:
        uplowchoose=twochoice()
        if uplowchoose==1:
            passwd.append(alphabet().lower())
        elif uplowchoose==2:
            passwd.append(alphabet().upper())
        i+=1
    elif choose==2:
        passwd.append(character())
        i+=1
    else:
        passwd.append(number())
        i+=1
listToString(passwd)





