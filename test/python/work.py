#第十一题
print("hello world")
#整数类型
count = 10  
#浮点类型
average = 89.5  
# 字符类型（实际上是长度为1的字符串）, 
grade = 'A' 
# 字符串,
name = "Alice"  
#布尔类型
is_passed = True
print("Count:", count)
print("Average:", average)  
print("Grade:", grade)  
print("Name:", name) 
print("Passed:", is_passed)
#初始赋值为整数
variable=42
print(variable, type(variable))
#将变量类型改为浮点数
variable=42.0
print(variable, type(variable))
#for循环
for i in range(5):
    print("Number:",i)
#while循环
i=0
while i<5:
    print("Number:",i)
    i+=1
#迭代字符串列表
text="hello"
for char in text:
    print(char)
#迭代列表
numbers=[10,20,30,40,50]
for number in numbers:
    print("Number:",number)
#定义列表
numbers=[1,2,3,4,5]
#直接访问列表元素
for i,number in enumerate(numbers):
    print(f"Element {i}: is {number}")
#添加元素
numbers.append(6)
#删除指定位置元素
del numbers[2]
#插入元素
numbers.insert(2,7)
#输出列表
print("Updated list:",numbers)
#函数定义
def add(a,b):
    return a+b
#函数调用
result=add(2,3)
print("Result:",result)
#带有默认参数的函数
def greet(name,message="hello"):
    print(f"{message}, {name}!")
greet("Alice")
greet("Bob","welcome")
#带有可变参数的函数
def sum_all(*args):
    total=sum(args)
    print("Total:",total)
sum_all(1,2,3,4,5)


#第十二题
#题目 1：编写程序，输入任意大的自然数，输出各位数字之和。
num=input("请输入一个自然数：")
print(sum(map(int,num)))
#题目 2：输入一个三角形的三边长，求三角形面积。
a,b,c=map(int,input("请输入三角形的三边长：").split())
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print(f"三角形面积为{s}")
#写程序，使用 while 计算 1 到 100 的总和
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)
