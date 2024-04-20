a = [1,2,3]
a.append(5)
print(a)

n = [7, 6, 5]
n = sum(n)
print(n)

n = ', '.join(n)
print(n)
n = str(n)
print(n)
# n = list(n)
n = n.split(' ')
print(n)

# 111

# 102
n = int(input())
x = int(input())
s = 0
f = 1
for i in range(1, n+1):
    f = f * i
    s = s + ((-1)**(i+1) *x **i)/f
print(s)

# 104
n = int(input())
s = 0
for i in range(1, n+1):
    s = s + i*(i+1)
print(s)

# 107
n = input() # 001111
l = len(n)
if l%3 == 1:
    n = '00' + n
elif l%3 == 2:
    n = '0' + n
l = len(n)
s = 0
k = 0
for i in range(0, l ,3):
    k = k*10 + int(n[i]) *4 + int(n[i+1])*2 + int(n[i+2])
    s = s + k
print(s)

# 107

n = input()
rl = len(n) - 1
s = 0
for i in n:
    s = s + int(i)*2**rl
    rl = rl -1
sekkizlik = ''
while s > 0:
    a = s % 8
    sekkizlik = str(a) + sekkizlik
    s = s // 8
print(sekkizlik)

# 111

x = 29
g = 1
while x<=100:
    x = x + x+5
    g = g+1
print(g,x)


# 50
n=input()
n=n.split(" ")
for i in n:
    print(len(i))

# 51
amil=16
eltac=8
anar=13
print((amil+eltac+anar)/3)

# 52
a=['amil','anar','eltac']
s=0
for i in a:
    s=s+len(i)
print(s)

# 53
a='123145124567'
a=a.replace('1','bir')
print(a)

# 54
x=[13,27,19,23]
b=[]
for i in x:
    c=i%10
    d=i//10
    e=c+d
    b.append(e)
print(b)

# 55
n=input()
n=n.split(' ')
print(len(n))

# 56 
n=input()
b=[]
for i in n:
    if n.count(i)==1:
        b.append(i)
print(len(b))

# 57
n=["ecoinoew",'econwno','kcoiwcoiej']
n=max(n)
print(len(n))

# 58 ?
n=input()
n=n.split(' ')
for i in n:
    i.count(w)
print(n)


# 59?
n=input()
n=str(n)
n=list(n)
n.sort()
n.reverse()
n=' '.join
print(int(n))

