def save_(role1,role2,count):
    file1='倚天屠龙记\\赵敏_'+str(count)+'.txt'
    file2='倚天屠龙记\\张无忌_'+str(count)+'.txt'
    with open(file2,'w') as f:
        f.writelines(role2)
    with open(file1,'w') as e:
        e.writelines(role1)
    
def split_(filename):
    role1=[ ]
    role2=[ ]
    count=1
    with open(filename) as a:
        for eachlines in a:
            if eachlines[:6] != '======':
                [name,lines]=eachlines.split(':',2)
                if name=='赵敏 ':
                        role1.append(lines)
                else:
                        role2.append(lines)
            else:
                save_(role1, role2,count)
                role1=[ ]
                role2=[ ]
                count+=1
        save_(role1, role2,count)
   
split_('倚天屠龙记_编剧：右前方.txt')
            
            
