import math

a = 2
b = 4
c = -6

def quadratic(a,b,c):
    # Value underneath the square root
    x = (b*b) - (4*a*c)
    print(math.sqrt(abs(x)))
    
    if x<0:
        print('Imaginary')
    else:
        root1 = (-b + math.sqrt(abs(x))) / (2*a)
        root2 = (-b - math.sqrt(abs(x))) / (2*a)

        print('First root is: ',root1)
        print('Second root is: ',root2)

# function call
quadratic(a,b,c)

