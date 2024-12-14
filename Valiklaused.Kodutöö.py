from math import*

#ülesanne 1

n = float(input("Введите число: "))

if n > 0:
    print("Число положительное")
    if n %2 ==0:
        print("Число четное")
    else:
        print("Число нечетное")

elif n < 0:
    print("Число отрицательное")
else:
    print("Введите положительное число для определения четности/нечетности!")


#ülesanne 2

print("Введите три числа: ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print("Это треугольник.")
        if a == b == c:
            print("Треугольник равносторонний.")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный.")
        else:
            print("Треугольник разносторонний.")
    else:
        print("Сумма углов не равна 180. Это не треугольник.")
else:
    print("Углы должны быть положительными числами.")


#ülesanne 3

answer = input("Хотите расшифровать день недели? (да/нет): ").lower()

if answer == "да":
    day = int(input("Введите номер дня недели (1-7): "))
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    
    if 1 <= day <= 7:
        print(f"Это {days[day - 1]}.")
    else:
        print("Число должно быть от 1 до 7.")
else:
    print("Операция завершена.")


#ülesanne 4

month = int(input("Введите месяц рождения (число от 1 до 12): "))
day = int(input("Введите день рождения (число от 1 до 31): "))

if 1 <= month <= 12 and 1 <= day <= 31:
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Ваш знак зодиака: Водолей")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Ваш знак зодиака: Рыбы")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Ваш знак зодиака: Овен")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Ваш знак зодиака: Телец")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Ваш знак зодиака: Близнецы")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Ваш знак зодиака: Рак")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Ваш знак зодиака: Лев")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Ваш знак зодиака: Дева")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Ваш знак зодиака: Весы")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Ваш знак зодиака: Скорпион")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Ваш знак зодиака: Стрелец")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Ваш знак зодиака: Козерог")
    else:
        print("Вы ввели некорректную дату!")
else:
    print("Месяц или день вне допустимого диапазона!")


#ülesanne 5

user_input = input("Введите число или текст: ")

try:
    num = float(user_input)
    if num.is_integer():
        print(f"50% от числа: {num / 2}")
    else:
        print(f"70% от числа: {num * 0.7}")
except ValueError:
    if user_input.isalpha():
        print(f"Это текст: {user_input}")
    else:
        print("Некорректный ввод!")


#ülesanne 6

answer = input("Хотите решить квадратное уравнение? (да/нет): ").lower()

if answer == "да":
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    print("Найти D: D=b**2-4ac.")

    D = b ** 2 - 4 * a * c
    print(f"Дискриминант (D) = {D:.2f}")
    if D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print(f"Уравнение имеет два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif D == 0:
            x = -b / (2 * a)
            print(f"Уравнение имеет один корень: x = {x:.2f}")
    else:
        print("Уравнение не имеет действительных корней.")

else:
    print("Хорошо, до свидания!")