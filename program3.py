#wap to check 2 user given strings and check whether which one of them is greater
a=input("Enter a string: ")
b=input("Enter another string: ")
if a>b: #comparison operators check ascii values of string variables and prints the appropriate statement
    print(a,"is greater than",b)
elif a<b:
    print(b,"is greater than",a)
else:
    print("Both of them are equal")
