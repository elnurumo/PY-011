# 68 1 - ci mövzu
# 54, 57, 58 , 56 3-cü mövzu

# 1 ci method
import math
x = float(input())
if x<=5:
    abs(x+2)+3*x
elif x>7:
    x**3 - 2
else:
    math.sqrt(3*(x**4) +10)

# 2-ci metod

x = float(input())
if x<=5:
    abs(x+2)+3*x
elif x>7:
    x**3 - 2
else:
    (3*(x**4) +10)**0.5

# 60 3 - cu mövzu
a = [12,45,23,16,121,34,66,15]
s = 0
for i in a:
    i = str(i)
    if i.count('1') != 0:
        s = s + 1
print(s)

# 61 1-ci mövzu

saat1 = int(input())
deqiqe1 = int(input())
saniye1 = int(input())
saat2 = int(input())
deqiqe2 = int(input())
saniye2 = int(input())
a1 = saat1*3600 + deqiqe1*60 + saniye1
a2 = saat2*3600 + deqiqe2*60 + saniye2
print(a2-a1)

# 58 3-cu mövzu

n = input().lower()
n = n.split(" ")
s = 1
for i in n:
    m = i.count('w')
    print('daxil edilmiş cümlənin',s, 'saylı sözündə ', m, 'sayda w simvolu var')
    print(f'daxil edilmiş cümlənin {s} saylı sözündə {m} sayda w simvolu var')
    s = s + 1

# 66

Email = input()
password = input()
if Email == 'email@inbox.ru' and password == '321abc':
    print('Giriş tamamlandı')
else:
    print('şifrə və ya email səhvdir')


