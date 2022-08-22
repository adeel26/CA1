a = 2
b = 4
c = -6

def quadratic(a,b,c):
    # Value underneath the square root
    x = b**2 - 4*a*c

    # Squae root of x
    sqrt = x*0.5

    if(x<0):
        print('Imaginary')
    else:
        root1 = ((-b+sqrt)/2*a)
        root2 = ((-b+sqrt)/2*a)

        print('First root is: ',root1)
        print('Second root is: ',root2)

quadratic(a,b,c)

