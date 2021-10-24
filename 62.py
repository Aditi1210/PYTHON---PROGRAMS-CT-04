def middleOfThree(a, b, c):

     

    # Checking for b

    if ((a < b and b < c) or (c < b and b < a)) :

        return b;

 

    # Checking for a

    if ((b < a and a < c) or (c < a and a < b)) :

        return a;

 

    else :

        return c

 

# Driver Code

a = 20

b = 30

c = 40

print(middleOfThree(a, b, c))
