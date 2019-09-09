import random
import time
secret=random.randint(1,9)
print("""--------------------爷爷游戏---------------------
规则：三次机会，堵上尊严，猜10以内一个整数，猜中你就是我爷爷，否则为孙子。""")
temple=input("输入一个数:")
guess=int(temple)
count=0
if guess<secret:
        print("小了!")
if guess>secret:
        print("大了!")
while  (guess != secret)  and  (count < 2):
        temple=input("输入一个数:")
        guess=int(temple)
        count=count+1
        if guess<secret:
                print("小了!")
        if guess>secret:
                print("大了!")
print("游戏结束\n")
if guess==secret:
        print("流批，你是我爷爷!")
else:
        print("辣鸡，你是我孙子!")
print("游戏5秒后自动退出")
time.sleep(5)


