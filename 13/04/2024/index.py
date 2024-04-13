# 71
# n = int(input())
# s = 0
# for i in range(n):
#     a = int(input())
#     s += a
# print(s/n)

# 72

# n = int(input('Sayın daxil et: '))
# b = []
# for i in range(n):
#     a = int(input("Ədəd daxil et: "))
#     b.append(a)
# min_num = min(b)
# print(min_num)

# 67
# n = int(input()) #2345
# n = str(n)
# a = int(n[1])
# b = int(n[2])
# if b%2 == 0:
#     print(a+b)
# else:
#     print(a*b)



#  70

# n = int(input()) #2400
# m = n
# s = 0
# while n == 0:
#     a = n % 10
#     s = s + a
#     n = n//10
# if m % s == 0:
#     print('Bölünür')
# else:
#     print('Bölünmür')


# 68
# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+1/(i**2)
# print(s)

# 69

# n=int(input())
# s=0
# for i in range(1,n+1,2):
#     s=s+(1/i)**i
# print(s)

# 70

# n=int(input())
# m = n
# s = 0
# while n > 0:
#     a = n%10
#     s = s + a
#     n = n // 10
# if n%s==0:
#     print('Bolunur!')
# else: 
#     print("Bolunmur!")

# # 71
# n=int(input())
# s=0
# for i in range(n):  #== range(0,n,1)
#     a = int(input())
#     s = s + a
# print(s/n)

# 80
# n = int(input())
# s = 0
# if n > 1:
#     for i in range(2,(n//2)+1):
#         if n % i == 0:
#             s = s + 1
#     if s == 0:
#         print("Sadədir")
#     else:
#         print("Mürəkkəbdir")
# else:
#     print("1 nə sadədir nə də mürəkkəb")

#72

# n=int(input('Say daxil et: '))
# b=[]
# for i in range(n):  #== range(0,n,1)
#     a = int(input('Ədədləri daxil et: '))
#     b.append(a)
# print(min(b))


#  73

# n= int(input("say daxil et:"))
# b=[]
# for i in range(n):
#     a=int(input("eded daxil et:"))
#     b.append(a)
# print(max(b))

# b=[]
# for i in range (1,1000,2):
#         b.append(i)   
# print(b)