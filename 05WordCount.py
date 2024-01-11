#wap that takes a sentence as input and counts the number of words in it
a=input("Enter a sentence: ")
b=a.split()
count=0
for i in b:
    count+=1
print("Word count:",count)
