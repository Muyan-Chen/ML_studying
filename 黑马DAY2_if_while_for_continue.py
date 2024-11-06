# 布尔类型：真和假
# 比较运算：真和假
# 布尔bool：表达现实生活中的逻辑，True and False
# 定义变量存储布尔类型的数据：变量名称=布尔类型字面量 or 用比较运算符
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

# if语句的基本格式：