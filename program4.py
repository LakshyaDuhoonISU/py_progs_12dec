#wap to count number of vowels in a given string, considering both uppercase and lower case
a=input("Enter a string: ")
count=0
for i in a:
    if i.lower() in ['a','e','i','o','u']:
        count+=1
print("Vowel count:",count)