# # Задание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

a=[x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(a))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №2:
# a = 333
# b = 555
# Поменяйте значения переменных местами(НЕ ВРУЧНУЮ!), чтобы в ПЕРЕМЕННОЙ "a" было значение 555, а в ПЕРМЕННОЙ "b" было значение 333.

a = 333
b = 555

buf = a
a = b
b = buf

print(a, b)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.
num = 4729461084
sum = 0
while num>0:
    num1 = num%10
    sum = sum+num1
    num = int(num/10)
print(sum)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:

a = {'год':input(),
'месяц':input()
'день':input(),
'время':input()}
print(a)




a = input()
b = input()
c = input()
d = input()
q = {'year':{a}, 'month':{b}, 'day':{c}, 'time':{d}}
for value in q.items():
print(f'{a}-{b}-{c}-{d}')






# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №5:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?


print(str(1+1+1+1+1))
a=1
b=7
print(str(a+a+a+a+a))
print(str(b*a))





# a = ("w" + "h" + "i" + "l" + "e")
# t = int(len(a))
# print(t)

# b = ("a" * 7)
# c = int(len(b))
# print(c)


# a = ("a" * 5)
# t = int(len(a))
# print(t)

# b = ("a" * 7)
# c = int(len(b))
# print(c)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №6:
# Напишите команду Linux которая создаст ДИРЕКТОРИЮ в НЕСУЩЕСТВУЮЩЕЙ директории БЕЗ ОШИБОК!
mkdir -p /home/aimira/Рабочий стол/test/{test1,test2}


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №7:
# Как в Linux выглядит полный путь до Desktop Директории для пользователя 'developer'.\
/home/aimira/Рабочий стол


# #Задача 1
# # Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# #Выведите все элементы, которые больше 5.

a=[1,1,2,3,5,8,13,21,34,55,89]
for elem in a:
    if elem>5:
        print(elem)

 
#Задача 2
#Есть набор чисел digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
#Поделить каждое число из digits на 9 и вывести на экран.
digits=(113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
dint=9
digitss=[]
for x in digits:
    digitss.append(x/dint)
print(digitss)


 
# #Задача 3
fruits = ('banana','stawberry','apple','orange','limon','ananas')
Выведите первый и последний элемент списка.
fruits=("banana","strawberry","apple","orange","limon","ananas")
print(fruits[0])
print(fruits[-1])
 
# Задача 4 
# Здесь замешаны разные типы данных. 
# Если вы уверены что логика написана правильно, но оно всё равно не работает скорее всего вы справились с заданием
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)


spisok_1 = {'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23}
spisok_2 = {'Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23}
spisok =(set(spisok_1).difference(spisok_2))
print(spisok)
 
 
# Задача 5
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов и останавливается, если встречает число 237.

numbers=[ i for i in range(1,300)]
for x in numbers:
  if x == 237:
    break
  elif x % 2 == 0:
    print (x)
 
 
