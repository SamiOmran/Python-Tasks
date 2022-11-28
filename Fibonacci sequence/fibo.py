def fibo(numb):
    if not numb:
        return 0
    elif numb <=2:
        return 1
    return fibo(numb-1) + fibo(numb-2)


print(fibo(-2))