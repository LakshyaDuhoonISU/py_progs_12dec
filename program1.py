#string operations
str='ITM Skills University'
'''print("str[-21:]=",str[-21:]) #slicing
print("str[0]=",str[0]) #indexing
print("str[0:3]=",str[0:3])
print("str[0::2]=",str[0::2])
print("reverse:",str[::-1])
'''
#looping through the string
'''i=0
while i<len(str): #while loop
    print(str[i])
    i+=1'''

'''for letter in str:
    print(letter) #for loop'''

'''def fun(str,char): #function to print first occurence of character
    for i in str:
        if i==char:
            print("First occurence at index number:",str.index(i))
            break
fun(str,"i")'''

'''def fun(str,char): #function to count occurences of character in the string
    count=0
    for i in str:
        if i==char:
            count+=1
    if count>0:
        print("Count:",count)
    else:
        print("character not found")
a=input("Enter a character to search for: ")
fun(str,a)'''

'''print(str.find('ITM',0,11)) #find() function to print index of first letter I in ITM from range index 1 to index 11
print(str.find('i')) #prints index of first occurence of 'i' in string str
print(str.find("Skills",1,5)) #as "Skills" is not present in range 1 to 5, find() returns -1 to indicate no match '''

'''def funct(str,subs): 
    if subs in str: #in membership operator is used to find substring in the string
        print("Substring is available in the string")
    else:
        print("No match")
a=input("Enter a string: ")
b=input("Enter a substring to find: ")
funct(a,b)'''

'''print('Hi, what\'s up?') 
print("Hi,\"what's up?") #\- escape sequence(eg- \n for newline, \t- tabspace)
print(r"""Hi,"what's up?""") #r- raw string, can't use escape sequences with r string 
print("Welcome to {},{}".format("ITM","Kharghar")) #.format() is used to to send arguments to the parameters in the string(default- positional arguments)
print("Welcome to {1},{0}".format("Kharghar","ITM")) #.format() is used to send keyword based arguments'''
a=input("Enter your name: ")
print("Hello {}".format(a))
print(f"Hello {a}") #f string or formatted string is used to directly place variables in string

