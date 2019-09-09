import math
m=6
dmax=530
dmin=95
k=4.77
zq_max=int(dmax/m)
zt_min=int(dmin/m)
zq=[]
zt=[]
re_1=[]
re_2=[]
bw=[]
for i in range(zt_min,zq_max+1):
    for j in range(zt_min+1,zq_max+1):
        k_=i/j
        b_k=k_/k-1
        if (b_k<0.02) and (b_k>-0.02):
            zq.append(i)
            zt.append(j)
for i in range(0,len(zq)):
    print(zq[i],zt[i])
for i in range(0,len(zq)):
   if (zq[i]-zt[i])%2==0:
        zx=(zq[i]-zt[i])/2
   else:
        zx=int((zq[i]-zt[i])/2)
        bw.append(i)                #行星轮变位
   for q in range(2,7):
        if (zq[i]+zt[i])%q==0:
                an_j=2*math.pi/q
                sin_j=math.sin(an_j/2)
                t=zt[i]*sin_j-zx*(1-sin_j)-1.6
                if t>=1:
                    if q>=3:
                        re_1.append(zq[i])
                        re_1.append(zt[i])
                        re_1.append(zx)
                        re_1.append(q)
                        re_1.append(t)
                    else:
                        an_min=360*math.asin((zx+1.6)/(zt[i]+zx))/math.pi
                        for n in range(1,zq[i]+zt[i]):
                            an=360*n/(zq[i]+zt[i])
                            if an>an_min and an<180/q:
                                sin_j=math.sin(an/360*math.pi)
                                t_=zt[i]*sin_j-zx*(1-sin_j)-1.6
                                re_2.append(zq[i])
                                re_2.append(zt[i])
                                re_2.append(zx)
                                re_2.append(q)
                                re_2.append(an)
                                re_2.append(t_)
                                break    
print('一组行星轮:')
for i in range(0,len(re_1)):
    flag=0
    if i%5==0:
        for each in bw:
            if zq[each]==re_1[i] and zt[each]==re_1[i+1]:
                flag=1
        if flag:
           print('zq:%d,zt:%d,zx:变位,<=%d,q:%d,k:%0.4f,δk:%0.2f%%,t:足够'%(re_1[i],re_1[i+1],re_1[i+2],re_1[i+3],re_1[i]/re_1[i+1],100*(re_1[i]/re_1[i+1]/k-1)))
        else:
            print('zq:%d,zt:%d,zx:%d,q:%d,k:%0.4f,δk:%0.2f%%,t:%0.2f'%(re_1[i],re_1[i+1],re_1[i+2],re_1[i+3],re_1[i]/re_1[i+1],100*(re_1[i]/re_1[i+1]/k-1),re_1[i+4]))
print('两组行星轮:')
for i in range(0,len(re_2)):
    if i%6==0:
        print('zq:%d,zt:%d,zx:%d,q:%d,Θj:%.1f°,k:%0.4f,δk:%0.2f%%,t:%0.2f'%(re_2[i],re_2[i+1],re_2[i+2],re_2[i+3],re_2[i+4],re_2[i]/re_2[i+1],100*(re_2[i]/re_2[i+1]/k-1),re_2[i+5]))
print('两组行星轮之间的间隙比较小，可以采用变位改善这种情况')


