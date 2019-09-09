import random
con_=open('c:\\users\\lenovo\\desktop\\py\\倚天屠龙记_编剧：右前方.txt','w')
role1='赵敏 : '
role2='张无忌 : '
line_role1=['我本名叫敏敏特穆尔。','叫我一声好姐姐。','我和周姑娘谁更漂亮？','我就不给！']
line_role2=['赵姑娘，请自重。','老子最讨厌女人了，给我滚！！！','当然是灭绝师太了！','那恕张某得罪了！']
for i in range(0,6):
    num=int(random.randint(0,3))
    con_.write(role1)
    con_.writelines(line_role1[num])
    con_.write('\n')
    con_.write(role2)
    con_.writelines(line_role2[num])
    con_.write('\n')
    if i==1 or i== 3:
        con_.writelines('========\n')
con_.close()
