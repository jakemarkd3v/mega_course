def fib(n):

    #check if n is not less than zero

    if n<0:
        print("incorrect value")
    

    elif n == 0:
        return 0


    elif n == 1 or n == 2:
        return 1

    else:
        return  fib(n-1)   +  fib(n-2)


print (fib(8))