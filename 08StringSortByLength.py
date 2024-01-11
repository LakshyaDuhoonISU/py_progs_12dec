#wap that takes a list of strings as input and sorts them based on their length
a=int(input("Enter number of strings: "))
b=[]
for i in range(a):
    c=input("Enter a string: ")
    b.append(c)
e=int(input("Select to sort the string:\n1.Ascending Order\n2.Descending Order\n"))
if e==1:
    for i in range(len(b)-1):
        for j in range(0,len(b)-1):
            if len(b[j])>len(b[j+1]):
                temp=b[j]
                b[j]=b[j+1]
                b[j+1]=temp
    for i in b:
        print(i)
elif e==2:
    for i in range(len(b)-1):
        for j in range(0,len(b)-1):
            if len(b[j])<len(b[j+1]):
                temp=b[j]
                b[j]=b[j+1]
                b[j+1]=temp
    for i in b:
        print(i)
else:
    print("Wrong choice")
