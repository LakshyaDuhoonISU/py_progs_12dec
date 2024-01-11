#wap to check if 2 strings are anagrams of each other 
a=input("Enter a string: ")
b=input("Enter another string: ")
count=0
if len(a)==len(b):
    for i in a:
        #print(i)
        if i in b:
            count+=1
if count==len(a):
    print("It is an anagram")
else:
    print("It is not an anagram")
