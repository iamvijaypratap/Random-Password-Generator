import string
import random
import time
str = string.printable
slen = int(input("Enter Your Password Length : \n"))
RandStr=[]
RandStr.extend(list(str))
random.shuffle(RandStr)
print("Generating...")
time.sleep(3)
print("Your Password is Generated ")
print("".join(RandStr[0:slen]))
