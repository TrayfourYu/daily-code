def recursion(n):
    if n==1:
        return 1
    else:
        return n*recursion(n-1)
n=int(input('输入正整数'))
re_=recursion(n)
print('结果是%d'%(re_))
