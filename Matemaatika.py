import random

print("Добро пожаловать в тест по математике!")
print("Выберите уровень сложности:")
print("1 - Легкий (+, -)")
print("2 - Средний (+, -, *, /)")
print("3 - Сложный (+, -, *, /, **)\n")

level = int(input("Введите номер уровня: "))
max_number = int(input("Введите максимальное значение чисел: "))
num_problems = int(input("Сколько примеров вы хотите решить? "))

correct_answers = 0

for i in range(num_problems):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)

    if level == 1:
        operation = random.choice(['+', '-'])
    elif level == 2:
        operation = random.choice(['+', '-', '*', '/'])
    else:
        operation = random.choice(['+', '-', '*', '/', '**'])

    if operation == '/':
        while num2 == 0:  # чтобы избежать деления на ноль
            num2 = random.randint(1, max_number)
        correct_answer = round(num1 / num2, 2)
    elif operation == '**':
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 3)
        correct_answer = num1 ** num2
    elif operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2

    print(f"Пример {i + 1}: {num1} {operation} {num2}")
    try:
        user_answer = float(input("Ваш ответ: "))
        if user_answer == correct_answer:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_answer}")
    except ValueError:
        print(f"Неправильный ввод. Правильный ответ: {correct_answer}")

percentage = (correct_answers / num_problems) * 100

if percentage > 90:
    grade = 5
elif percentage > 75:
    grade = 4
elif percentage >= 60:
    grade = 3
else:
    grade = 2

print(f"\nВы правильно решили {correct_answers} из {num_problems} примеров.")
print(f"Ваша оценка: {grade}")
