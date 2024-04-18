# # Klaviaturadan daxil edilmiş 2-dən böyük tam ədədin sadə vururqlarının alt-alta çapı

# n = int(input())
# s_vuruq = 2

# while n>1:
#     if n % s_vuruq ==0:
#         print(s_vuruq)
#         n = n//s_vuruq
#     else:
#         s_vuruq = s_vuruq + 1

# # Klaviaturadan daxil edilmiş 2-dən böyük tam ədədin sadə bölənlərinin alt-alta çapı

# n = int(input())
# s_vuruq = 2
# b = []
# while n>1:
#     if n % s_vuruq ==0:
#         b.append(s_vuruq)
#         if b.count(s_vuruq) == 1:
#             print(s_vuruq)
#         n = n//s_vuruq
#     else:
#         s_vuruq = s_vuruq + 1

# # Fibonacci ardıcıllığı hesablayan alqoritmi yazın. 
# # Bu alqoritmin neçən-ci Fibonacci ədədini hesabladığınızı izah edin.

# # def fiboncci(n):
# #     a, b = 0, 1
# #     for i in range(n): 
# #         a, b = b, a+b
# #     return b
# # n = int(input())
# # result = fiboncci(n)
# # print(result)

# # 'Elnur'.upper()
# # str()


# # Verilmiş bir sıra üzrə ən kiçik ədədi tapmaq üçün bir proqram yazın. 
# # proqramınız hansı metodlardan istifadə etdiyini izah edin.

# def min_num(list):
#     min_numb = list[0]
#     for i in range(1,len(list)):
#         if min_numb > list[i]:
#             min_numb = list[i]
#     return min_numb

# a = [12,18,24,30,4]




# # Bir sətir veriləndə, sətirdəki hər bir simvolların sayını tapan bir 
# # proqram yazın. Məsələn, "hello" sözünün daxilində hər bir hərfin neçə dəfə 
# # işləndiyini tapan alqoritmi yazmalısınız.

# # Bir listdə olan cüt ədədlərin cəmini hesablayan proqram yazın. 

# # *
# # **
# # ***
# # ****
# # ***** terminalda, çıxışda bunu qaytarsın

# for i in range(1,6):
#     print(i*'*')


# # list() vs split()
# a = 'Elnur, Ülvi, Tural, Nərmin'
# a = list(a) #bütün simvolları ayırdı hissə hissə.
# a = a.split(', ') #göndərdiyim əmrə görə ayırdı.
# print(a)


# decimal_number = 10
# hex_number = f'{decimal_number:x}' 
# print(hex_number)
