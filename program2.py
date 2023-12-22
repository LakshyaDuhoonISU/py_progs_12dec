#wap to print all letters from string 1 that are also present in string 2
def funct(str1,str2):
    if len(str1)>len(str2):
        for i in str2:
            for j in i:
                if j in str1:
                    print(j)
    else:
        for i in str1:
            for j in i:
                if j in str2:
                    print(j)

str1='''Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.'''
str2="xyz abc def limited to maximum length"
funct(str1,str2)