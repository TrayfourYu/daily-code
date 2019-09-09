def hanoi(a,x,y,z):#将一堆a个由小到大堆起来的盘从x轴完全转移到z轴
    if a==1:
        print(x,'---->',z)
    else:
        hanoi(a-1,x,z,y)
        print(x,'---->',z)
        hanoi(a-1,y,x,z)
c=int(input())
hanoi(c,'x','y','z')
