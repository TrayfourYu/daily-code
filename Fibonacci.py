def fibo(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    return( fibo(a-1)+fibo(a-2))
month=int(input('输入正整数'))
print(fibo(month))
