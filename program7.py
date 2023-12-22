#wap that converts camel case string to snake case
a=input("Enter a camel case string: ")
b=[]
for i in a:
    for j in i:
        #print(j)
        if j.isupper():
            #print(j)
            b.append("_")
            b.append(j.replace(j,j.lower()))
            print(j)
            break
        b.append(j)
print(b)
for i in b:
    print(i,end='')