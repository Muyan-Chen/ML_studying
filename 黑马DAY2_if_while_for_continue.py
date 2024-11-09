# 布尔类型：真和假
# 比较运算：真和假
# 布尔bool：表达现实生活中的逻辑，True and False
# 定义变量存储布尔类型的数据：变量名称=布尔类型字面量 or 用比较运算符
from base64 import standard_b64decode

result = 10>5
print(f"the result of 10>5 is {result},the type is {type(result)}")
# 运算符 == 判断是否相等，是为true，不是为false
# ！= 是否不相等
# >= 大于等于； <= 小于等于
# 定义变量存储bool类型的数据
bool_1 = True #caution:大写
bool_2 = False
print(f"bool_1 is {bool_1}, type is {type(bool_1)}")
print(f"bool_1 is {bool_2}, type is {type(bool_2)}")
# 内容的相等比较==，一个=是赋值
num1=10
num2=10
print(f"the result of 10==10 is {num1==num2}")
num1 = 10
num2 = 15
print(f"the result of 10!=15 is {num1!=num2}")
name1 = "Muyan"
name2 = "Runfeng"
print(f"Muyan and Runfen are the same person, that is {name1==name2}")
# 演示大于小于
print(f"10>15 is {num1>num2}")

##if语句的基本格式：if+判断条件+：（记得要空格）条件成立时要做的事情
age = 30
if age>=18:
    print("I am adult")
    print("I will go to the university")
print("Time goes fast")
# homework: adult judge
age = input("What is your age?")
age = int(age) # can also be written age=int(input())
if age >= 18 :
    print("You are adult and you need to pay more 10$")
print("Have a nice day")

# if else语句:
age = int(input("What is your age?"))
if age >= 18 :
    print("You are adult and you need to pay more 10$")
else:#不需要判断条件
    print("You can get in for free")
# homework
print("welcome to the zoo")
height = int(input("How high are you"))
if height >=120:
    print("You need to buy a ticket for 10$")
else:
    print("You can get in for free")
print("Have a nice day")

# if elif else语句：判断条件不止一个，用elif+条件2+：满足条件2该做的事情
height = int(input("what is your height?"))
vip_level = int(input("type in you vip level(1-5)"))
day = int(input("What day is it today?"))
if height<120:
    print("height below 120cm, free ")
elif vip_level>3:
    print("vip level above 3, free")
elif day == 1:
    print("Today is the special day, free")
else:
    print("you need buy a ticket for 10$")
# homework
num = 10
if int(input("你猜的数字是")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次"))== num:
    print("猜对了")
elif int(input("猜错了，再猜一次")) == num:
    print("恭喜猜对了")
else:
    print("sorry,都猜错啦，是10")

# 判断语句的嵌套：外层判断，内层判断，关键是空格缩进
if int(input("你的身高是多少"))>120:
    print("升高超出限制")
    print("如果VIP超过3，就可以免费")

    if int(input("你的vip等级"))>3:
        print("可以免费")
    else:
        print("买票吧")
else:
    print("免费玩")
# homework 1
if 18<= int(input("how old are you")) <30:
    if int(input("how long been worked"))>2 or int(input("级别"))>3:
        print("get a gift")
    else:
        print("not satisfy the condition, canot get the gift")
else:
    print("not satisfy the condition, canot get the gift")

# homework2
import random
num = random.randint(1,10)
print("猜数字游戏")
if int(input("guess a number")) != num:
    print("Have another guess")
    if int(input("Guess2")) !=num:
        print("Have another guess")
        if int(input("Guess2")) !=num:
            print("wrong")
        else:
            print("you are right")
    else:
        print("you are right")
else:
    print("you are right")
# standard  solution
import random
num = random.randint(1,10)
guess_num = int(input("guess a number"))

if guess_num == num:
    print("第一次就猜中了")
else:
    if guess_num>num:
        print("猜大了")
    else:
        print("猜小了")

    guess_num = int(input("another guess"))

    if guess_num == num:
        print("第二次就猜中了")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

        guess_num = int(input("last guess"))

        if guess_num == num:
            print("第三次猜中了")
        else:
            print("没有猜中")

# 循环loop：while循环的基础语法：while+条件（bool比较类型）+：条件满足时执行的操作
i=0
while i<100:
   print("I love you, XXX")
   i+=1
# homework:sum of 1-100
i=0
sum = 0
while i<100:
    i += 1
    sum+=i

print(f"The sum from 1 to 100 is {sum}")

# while循环的基础案例：用while写猜数字
import random
num = random.randint(1,100)
i=1
guess_num = int(input("猜个数"))
while guess_num != num:
    if guess_num < num:
        print("猜小了")
    else:
        print("猜大了")
    guess_num = int(input("再猜个数"))
    i+=1
print(f"猜对了，一共猜了{i}次")
# standard solution
import random
num = random.randint(1,100)
count=0 #定义变量记录次数
# 通过一个bool变量来决定循环是否继续
flag = True
while flag:
    guess_num = int(input("Print your guess_number"))
    count+=1
    if guess_num == num:
        print("Right")
        flag = False
    else:
        if guess_num > num:
            print("Your guess is bigger")
        else:
            print("Your guess is smaller")
print(f"You totally guess {count} times")

# while循环的嵌套运用：
# while 条件1：
#     while 条件2：
i = 1
while i<=100:
    print(f"今天是第{i}天，准备表白")
    # 内层循环的控制变量
    j=0
    while j<=10:
        print(f"送给小美第{j}支玫瑰花")
        j+=1
    print("小美，我喜欢你")
    i+=1
print(f"坚持到第{i-1}天，表白成功")

# while循环的嵌套案例：打印九九乘法表
# 首先输出print不换行：
print("Hallo",end='')
print("world",end='')
# \t相当于tab键，能将多行字符串进行对齐
print("hallo\tworld")
print("good\tnews")
# 9x9乘法表：控制行的循环；控制每一行内容的循环
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print() #print空内容，输出一个换行
    
# for循环的基础语法：while的循环条件是自定义的，但是for是轮询机制，是逐个处理
# for 临时变量 in 待处理数据集（序列）
name = "itheima"
for x in name:
# 将name里的内容，挨个取出赋予x
    print(x)
# for循环无法构建无限循环
# homework：数一数有几个a
sent = "itheima is a brand of itcast"
count = 0 #注意是循环外部
for x in sent:
    if x == "a":
        count+=1
print(count)

# 语法1：range语句：range(num),从0开始到num结束（不含num）
# eg：range(5):[0,1,2,3,4]
# 语法2：range(num1,num2):从num1-num2（不含num2）
# 语法3：range(num1,num2,step):num1-num2,数字之间的步长是step
# eg:range(5,10,2):[5,7,9]
for x in range(10):
    print(x)
for x in range(5,10):
    print(x)
for x in range(5,10,2):
    print(x)
# 送玫瑰花
for x in range(10):
    print("送玫瑰花") 
#  homework：有几个偶数
num = 100
count = 0
for x in range(1,num):
    if x%2==0:
        count+=1
print(count)

# 变量作用域
for i in range(5):
    print(i)
print(i) #规则上不允许，实际上可以；如果要遵守规则，在for循环之前定义i

# for循环的嵌套应用
i = 0
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天")

    for j in range(1,11):
        print(f"给小美送第{j}朵玫瑰花")
    
    print("I love you")
print(f"第{i}天，表白成功")
# homework:99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}x{i}={i*j}\t",end="")
    print()

# break and continue
# continue:中断本次循环，进入下一个循环
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3") #不会被执行
    print("语句4")
# break：直接把循环结束
for i in range(1,6):
    print("语句1")
    for j in range(1,5):
       print("yuju2")
       break #会导致第二层循环game over
       print("语句3")
print("语句4")
# homework:发工资
import random
sum_money = 10000
for staff_order in range(1,21):
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{staff_order},绩效分{num}，低于5，不发工资，下一位")
        continue
    elif sum_money == 0:
        print("工资发完了，下月领取吧")
        break
    else:
        sum_money-=1000
        print(f"员工{staff_order}，绩效分{num},发1000元,账户余额还剩{sum_money}元")

