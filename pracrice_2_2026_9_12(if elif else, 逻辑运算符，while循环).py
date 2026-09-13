age=int(input("your age："))
if age==13:
    print("you are a teenager")
elif age==14:
    print("you are a teenager")
elif age==15:
    print("you are a teenager")
elif age==16:
    print("you are a teenager")
elif age==17:
    print("you are a teenager")
elif age==18:
    print("you are a teenager")
else:
    print("you are not a teenager")
input()

#the above is equalivent to:
age=int(input("your age："))
if age>=13 and age<=18:
    print("you are a teenager")
else:
    print("you are not a teenager")
input()

score=int(input("score:"))
abcences=int(input("abcences:"))
if score<60 or abcences>5:
    print("need to retake course")
else:
    print("no need to retake course")
input()

rain_today=False
if not rain_today:
    print("rain today, bring umbrella")
input()

#while 循环
count=1
while count<=5:
    print("count=",int(count),", count is too small")
    count=count+1
print("Done!")
input()

print("please input number that is integer and odd and greater than 0" )
a=int(input("incert number:"))
while not (a>0 and a%2==1):
    print("number does not fit description, try again:")
    a=int(input("enter number:"))
else:
    print("success!")
input()

b=1
while b<=10:
    print(b)
    b=b+1
print("Done!")
input()

print("please input integar less than 100;enter -1 to stop.")
t=int(input("input:"))
while t!=-1:
    if t>=100:
        print("too big")
    else:
        print("Done! enter another")
    t = int(input("input:"))
print("stopped")
