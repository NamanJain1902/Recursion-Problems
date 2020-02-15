def power(n,x):
    if(x == 0):
        return 1
    return n*power(n,x-1)

n=int(input("Enter a number:"))
x=int(input("Enter power of number:"))
print("Answer",power(n,x),sep='->')