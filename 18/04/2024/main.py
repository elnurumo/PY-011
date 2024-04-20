# n = input().upper()
# reqemler = '0123456789ABCDEF'
# digit = 0
# # reqemler = reqemler.split(' ')
# reqemler = list(reqemler)
# nl = len(n) - 1
# for i in n:
#     digit = digit + reqemler.index(i) * 16 ** nl
#     nl = nl - 1
# print(digit)

# # 94
# n=input().upper()
# digit=0
# a='0123456789ABCDEF'
# a=list(a)
# n1=len(n)-1
# for i in n:
#     digit=digit+a.index(i)*16**n1
#     n1=n1-1
# print(digit)

# # 95
# n=input()
# s=0
# k=0
# n=list(n)
# n.reverse()
# for i in n:
#     s=s+int(i)*8**k
#     k+=1
# print(s)

# # 103
# n=int(input())
# s=0
# for i in range(1,n+1,2):
#     s=s+i*(i+1)*(i+2)
# print(s)

# # 104
# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+i*(i+1)
# print(s)

# # 108
# n=int(input())
# n=str(n)
# s='01234567'
# f = 0
# for i in n:
#     if s.count(i)==0:
#         f = 1
# if f == 1:
#     print('Mövcud deyil')
# else:
#     print('Mövcuddur')


# # 108
# n = input()
# f = 0
# for i in n:
#     if int(i) >=8:
#         f = 1
# if f == 1:
#     print('Mövcud deyil')
# else:
#     print('Mövcuddur')

# # 105
# n=input()
# s=0
# a='0123456789'
# for i in n:
#     if a.count(i)==1:
#         s+=1
# print(s)


# # 106
# n=input()
# b=[]
# for i in n:
#     if b.count(i)==0:
#         b.append(i)
# print(b)

# # 110
# s=100
# k=100
# n=1
# while s<200:
#     s+=k*1.05
#     n+=1
# print(n)