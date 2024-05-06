# 
# s = 0
# for i in range(1000,10000):
#     i = str(i)
#     a = i[0]
#     b = i[1]
#     c = i[2]
#     d = i[3]
#     if a == d and b == c:
#         s = s + 1
# print(s)


# n = int(input()) #
# a = n
# f = 0
# s = ''
# while n>0:
#     q = n%10
#     s = s + str(q)
#     n = n // 10
#     if a == int(s):
#         f = 1
# if f == 1:
#     print('Polindromdur')
# else:
#     print('Polindrom deyil')

# a=int(input())
# b=int(input())
# s=0
# f = 0
# if a>1:
#     for i in range(a,b+1):
#         f=0
#         for k in range(2,i//2+1):
#             if i%k==0 and i!=k:
#                 f=1
#         if f==0:
#             s+=i
# print(s)

# 8
# def f(y,elmeddin):
#     y += 5
#     elmeddin = elmeddin* 5
#     return elmeddin +y
# x = 5
# y = 6
# s= f(x,y)
# print(s)

# 12

# x = int(input())
# a = 0
# b = 0
# while x > 0:
#     a = a + 1
#     if (x%2)!=0:
#         b = b + x%8
#     x = x//8
# print(a)
# print(b)