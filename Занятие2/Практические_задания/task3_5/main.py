wind = int(input())

# TODO напишите с помощью if-elif-else условие проверки скорости ветра
if 1 <= wind <= 4:
    print("слабый")
elif 5 <= wind <= 10:
    print("умеренный")
elif 5 <= wind <= 10:
    print("сильный ")
else:
    print("ураганный")