a = '5'
b = '6'
print(a + b) #11 
print(type("a + b")) # a + b
print('a'+ 'b') # ab

n = float(input())
print(type(n))

print()
n=123
print(n//10 + n%10)

n = int(input()) # 253
s = 0
while n>0:
    a = n%10 
    s += a
    n = n//10
print(s)
# 55
n=int(input())
if n%6==0:
    print("he")
else:
    print("yox")

# 56
n=int(input())
if n<100 and n>=10:
     print("ikireqemli")
elif n <100 and n<10 :
    print("birreqemli")

# # 57
n=int(input())
if n%2==0:
    print(n-1, n+1, "Cütdür")
else:
    print(n-1,n+1, "Təkdir")
#58
# y=int(input())

# 1 ci method
import math
a = 36
b = int(math.sqrt(a))
print(b)

print("-----------------------------------------")
# 2 ci method
b = a**0.5
print(b)


# 58
x=int(input("x="))
if x<=5:
   print(abs(x+2)+(3*x))
elif 5<x<=7:
    print((3*x**4+10)**0.5) 
else :
    print(x**3-2)

