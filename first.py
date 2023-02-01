# def my_func(x):
# #    '''Ընդունումա թիվ վերադարձնումա 
# #     թվի քառակուսին'''
#     # returns the square of a number
    
#     return x**2
# # # print(my_func(4))    
# print(my_func.__doc__)

# print(set.__doc__)

# 1. returns the square of a number
# 2. None  True
# 3. Error
# 4. Նշվածներից ոչ մեկը

# ----------------------------------------------

# lst = [lambda x: x**2,
#         lambda x: x**3,
#         lambda x: x**4]

# for i in lst:
#     print(i(3), end= ' ')


# 1. Error
# 2. 9 27 81  True
# 3. 6 9 12
# 4. Նշվածներից ոչ մեկը

# ----------------------------------------------
# def my_func(**dicts):
#     if 'x' in dicts:
#         x = dicts['x']
#        return x+1

# print(my_func(y=6, x=7, z=9))

# 1. 8     True
# 2. Error
# 3. 6
# 4. 7

# ----------------------------------------------

# def func(x, y):
#     if x < y:
#         return x
#     return y

# print(func(12,13))

# my_func = lambda x, y: x if x<y else y
# print(my_func(12, 13))
 
# 1. 12    True
# 2. 13
# 3. None
# 4. Error

# ----------------------------------------------

# def my_func(**kwargs):
#     for i in kwargs:
#         return kwargs.get('c', 'Python')

# x = my_func(a=1, b=2, c=3)
# y = my_func(d=4, e=5, f=6)

# print(y)


# 1. 3
# 2. Error
# 3. None
# 4. Նշվածներից ոչ մեկը   True

# -----------------------------------------------

# Լրացնել բացը, որպեսզի ֆունկցիան հաշվի տրաված թվի ֆակտորիալը։

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return _______

# print(fact(5))

# 1. num*fact(num)
# 2. num*fact(num-2)
# 3. num*fact(num+1)
# 4. num*fact(num-1)  True


# -----------------------------------------------

# def my_func(x, **kwargs, *args):
#     y = x**2
#     return y

# print(my_func(x=1))

# 1. 2
# 2. None
# 3. Error   True
# 4. 1

# -----------------------------------------------

# def my_func(x, *args, **kwargs):
#     out = x
#     for i in args:
#         out += i

#     out += kwargs['y']
#     return out

# print(my_func(1,1,1,1, y=7))

# 1. 10
# 2. 11   True
# 3. Error
# 4. 1

# ------------------------------------------------

# def my_func(x, *args):
#     out = x
#     for i in args:
#         out += i

# x = my_func(1,1,1,1)
# print(x)

# 1. Error
# 2. 4
# 3. None   True
# 4.3

# -------------------------------------------------

# def my_func(i, j):
#     if i == 0:
#         return j
#     return my_func(i-1, i+j)

# print(my_func(4, 7))

# 1. Error
# 2. 11
# 3. 3
# 4. 17   True

# ------------------------------------------------


# print([[i,j,k] for i in range(1,100) for j in range(1,100) for k in range(1,100) if i**2+j**2==k**2])
# -----------------------------------------------

# for i in range(1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if i**2+j**2==k**2:
#                 print(i, j, k)

# ----------------------------------------------------