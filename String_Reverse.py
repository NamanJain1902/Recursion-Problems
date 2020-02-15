def strev(s):
    if(len(s) == 0):
        return s
    return strev(s[1:]) + s[0]  

s=input("Enter a string:")
print("Reversed string is",strev(s),sep='->')