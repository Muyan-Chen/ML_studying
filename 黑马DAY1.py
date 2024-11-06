print("Hallo world")

# 字面量：在代码中能被写下来的值：number,string,list,tuple,set,dictionary

# 注释的作用：更容易理解，增强代码的可读性
# 单行注释：#开头，一般用一个空格隔开
# 多行注释："""开头，"""结尾

# 变量# ：
money = 50
print("I have "+str(money)+" euro")
print("I have ", money ,"euro")

# 数据类型转换：从文件中读取的数字，默认是字符串；input（）默认结果是字符串，数字转换成string输出到外部
# int（x）：讲x转换成一个整数
# float（x）：浮点数
# str（x）：字符串
num_str = str(11)
print(type(num_str),num_str) #type()看括号里类型
float_str = str(11.56)
print(type(float_str),float_str)
#将string转换成数字
num = int("11")
print(type(num),num)
num2 = float("11.56")
print(type(num2),num2)
# num3 = int("python") #will not succeed如果要将字符串转为数字，字符串里面得是数字
# 整数转float
float_num = float(11)
print(type(float_num),float_num)
# float->int
int_num = int(11.545) #会丢失精度，不是四舍五入
print(type(int_num),int_num)

# 标识符syntax:变量的名字、方法的名字、类class的名字
# 只能出现英语、中文（不推荐）、数字（不可以用在开头）、下划线，能区分大小写
# 不可使用关键字：比如 false,true,none, and,as,assert,break.....
# 1_name = "zhangsan"
# uy@="mail"
name_1 ="zhangsan"
Ithema = "黑马"
ithema = "666"
print(Ithema)
print(ithema)
# class = 1
Class =1
# 命名规范：见名知意、下划线命名、英语字母全小写

# 运算符： +，-, *. /, //整除, %余数, **次方
print("1+1=",1+1)
print("2-1=",2-1)
print("2*1=",2*1)
print("4/2=",4/2)
print("11//2=",11//2)
print("11%2=",11%2)
print("2**2=",2**2)
# 赋值运算符：= 将右边赋给左边
# 复合赋值运算：c+=a->c=c+a
num = 1
num+=1#num will be 2
print("num =",num)
num *=4
print("num *=",num)
num/=2
print("num/=",num)

# 字符串扩展
name1 = '黑马程序员'
name2 = "黑马程序员"
name3 = """
我是
黑马程序员
"""
print(type(name3),name3)
# 如果我想定义的string本身带双引号或者单引号：单引号定义，里面包含双引号；双引号定义，内含单引号；使用转移字符\
name1 = '"黑马程序员"'
name2 = "'黑马程序员'"
# 使用\,解除紧随其后的引号的效用
name3 = "\"黑马程序员\""
print(name3)

# 字符串的拼接：字面量和变量 or 变量和变量 通过+
print("I have "+"81 credits")
name = "Alice"
address = "Karlsruhe"
print("I am "+name+" I live in "+address)
tel = 1621609396
print("I am "+name+" ,I live in "+address+", My phone number is "+ str(tel))

# 字符串格式化：%s，%
name = "黑马程序员"
message="学IT就来%s"%name #%表示占位，s表示将变量变成字符串放入占位的地方
print(message)
# 多变量占位: use () to seperate and be sure the order
class_num = 57
avg_salary = 16781
print("训练营%s期的学生的平均工资为%s"%(class_num,avg_salary))
message="训练营%s期的学生的平均工资为%s"%(class_num,avg_salary)
# %s：字符串占位； %d：转换成整数占位；%f：浮点型占位
name = "kit"
setup_year = 2001
studentengebuer = 1678.26
message = "%s成立与%d，国际学生每学期要交%f欧元"%(name,setup_year,studentengebuer)
print(message)

# 格式化的精度控制：比如float 19.9输出是19.0000
# 用辅助符号m.n控制：m控制宽度，.n控制小数点精度（会进行四舍五入）
# eg:%5d:表述整数控制在5位,但是宽度限制得大于实际宽度；%5.2f：宽度5，小数精度2
num1=11
num2=11.345
print("数字11限制宽度5，结果是：%5d"%num1)
print("数字11限制宽度1，结果是：%1d"%num1)
print("数字11.345限制宽度7，小书精度2，结果是：%7.2f"%num2)
print("数字11.345小书精度2，结果是：%.2f"%num2)

# 字符串格式化方式2：前面学习了%占位，现在有更简单的方式：f“内容（变量）”->字符串前加f
# 快速格式化方法不需要进行精度控制，什么类型都不用管，直接输出原变量
name = "My company"
setup_year = 2006
stock_price = 19.99
# f:format格式化的一个首字母
print(f"{name}is set up in {setup_year},the stock price today is {stock_price}")

# 对表达式进行格式化：表达式：一条有明确执行结果的代码语句，eg，1+1，2*6，name=“张三”
print("1*1等于%d"%(1*1))
print(f"1*1等于{1*1}")
print("字符串在python里的类型名是%s"%type("string"))

# exercise:股价计算小程序
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司{name}，股票代码{stock_code}，当前股价{stock_price},每日增长系数{stock_price_daily_growth_factor}，经过{growth_days}天增长后,"+"股价达到了%.2f"%(stock_price*stock_price_daily_growth_factor**growth_days))
# standard solution:
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
final_stock_price = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司{name}，股票代码{stock_code}，当前股价{stock_price}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,final_stock_price))

# 数据输入：input的语句的基本使用方式
# 数据输出：print()
# 数据输入：input()
print("tell me who you are")
name = input() #name来接受input,绿色代表输入
print(f"I know you are {name}")
# input语句本身就可以输出提示内容，见下
name = input("Tell me who you are")
print(f"I know you are {name}")
# 输入数字类型
num = input("告诉我你的银行卡密码")
num = int(num)
print("你的银行卡类型是",type(num)) #得到结果input类型会被认为是字符串，如果要把input弄成number，要进行数据转换
#exercise
user_name = input("input your name")
user_type = input("you vip status")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎光临")