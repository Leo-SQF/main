print("能购买鸡蛋的数量计算")
t=int(input("请输入付款金额："))
r=t%12
print("总金额：",t)
print("完整的打数（12个为一打）：",(t-r)/12)
print("找零：",r)
print("")

print("加法计算器")
a=str(input("请输入一个数字："))
b=str(input("请输入第二个数字："))
print(a,"+",b,"=",int(a)+int(b))
print(a+"+"+b+"="+str(int(a)+int(b)))
print("")

print("帮你计算你的名字是什么")
f=str(input("请输入您的Family name："))
g=str(input("请输入您的Given name："))
print("Hello,"+" "+g+f+"!")
print("")

print("判断整数的正负")
x=int(input("请输入一个整数："))
if(x>0):
    print(str(x)+" "+"is positive")
if(x<0):
    print(str(x)+" "+"is negative")
if(x==0):
    print(str(x)+" "+"is zero")
print("Done!")
print("")
input()
