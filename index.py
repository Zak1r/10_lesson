# i= 0

# while i <= 10:
#     print(i)
#     i += 1


# i= 0

# while i <= 10:
#     if i % 2 == 1: break                             # break == полностью останавливает цикл преждевременно
#     print(i)
#     i += 1



# while int(input('Enter number: ')) > 0:            #pass пропусти (ничего не делает)
#     pass
# def a():
#     return #возвращает

# for i in range (5):
#     if int(input('Enter number: ')) < 0: break



                                        # обработка ошиб
# print('Now you will be asked to enter 2 numbers that will be divided and the answer will be printed')
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))
# if b == 0:
#     while True:
#         print('Stupid asshole')
#         b = int(input('Enter 2nd number: '))
#         if b != 0: 
#             print(a / b)
#             break
# else:
#     print(a / b)

# print('Now you will be asked to enter 2 numbers that will be divided and the answer will be printed')
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number. Note that you cannot use 0!: '))
# if b == 0:
#     i = 1
#     while True:
#         # if user entered 0 more than 3 times 
#         if i > 3:
#             print('Stupid asshole........')
#         else:   print('Please, enter non-zero value!')
#         b = int(input('Enter 2nd number. Note that you cannot use 0!: '))
#         if b != 0: 
#             print(a / b)
#             break
#         i += 1
# else:
#     print(a / b)


'''
a = int(input('Enter 1st number: '))
i = 1
while True:
    b = int(input('Enter 2nd number. Note that you cannot use 0!: '))
    try: #trying for working with mistakes
        print(a / b)
        break
    except ArithmeticError:  #ZeroDivisionError and TypeError ArithmeticError
        if i > 3:   print('Please enter non zero number')
        else: print('Please enter non-zero number')
    i += 1'''




# while True:
#     a = int(input('Enter number: '))
#     if a > 0:   break
#     else: print ('you were asked to enter + number')


# while True:
#     try:
#         a = int(input('Enter positive number: '))
#         if a < 0: raise ValueError('you were asked to enter positive number: ')
#         else: break
#     except ValueError as ve:
#         print(ve)


'''while True:
    a = int(input('enter posive num'))
    if a > 0:   break
    else: print('you were asked to enter positive num ')

while True:
    try:
        a = int(input('enter posive num'))
        if a > 0: raise ValueError('you were asked enter posive num: ')
        else: break
    except ValueError as ve:
        print(ve)
'''