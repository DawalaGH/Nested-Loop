num = int(input("Enter a number: "))
t = num
numLen = 0
while t > 0:
    numLen += 1
    t //= 10 

if numLen >= 4:
    numLen //= 2
    chk = 0
    midOne = midTwo = 0 

    while num > 0:
        rem = num % 10
        if chk == numLen:
            midOne = rem
        elif chk == numLen - 1:
            midTwo = rem
        
        num //= 10  
        chk += 1
    
    prod = midOne * midTwo

    print(f"Product of mid numbers is {midOne} * {midTwo} = {prod}")
else:
    print("The number does not have enough digits.")
