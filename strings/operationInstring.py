
#indexing

name = "rajnish kumar "

print(name[6]) # h

#slicing last index is not included

# types of slicing 

#start:end 

print(name[0:3])  #raj


#only start specified

print(name[1:]) #ajnish kumar

#only end specified

print(name[:3]) # raj

# no start end 

print(name[:]) # rajnish kumar

# slicing with step 

print(name[0:7:3]) # rnh

# negative index also used for reverse

print(name[::-1])

#len() built in function to count leng of words including spaces

print(len(name))

# string repetition

print("hello\n" * 5)

# Memebership operatiors "in"   "not in"

print("raj" in name) # true

print("monu" in name) # false

print("kumar" not in name) # false

print("ok" not in name) # true

# methods in string

#  Changing letter cases


# Method	      Purpose	                               Example result
# upper()	      Uppercase          	                    HELLO PYTHON
# lower()	      Lowercase	                             hello python
# capitalize()	  Capitalize first character	            Hello python
# title()	        Capitalize each word	                     Hello Python
# swapcase()	       Reverse letter cases	            HELLO PYTHON → hello python 
 

#Removing spaces


# Method	     Purpose

# strip()	      Removes spaces from both ends
# lstrip()	Removes spaces from the left
# rstrip()	Removes spaces from the right


# immutable

name = "python"

name = "j" + name[1:]

print (name)
