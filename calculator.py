# Калькулятор фізичних величин

def main():
    print("Виберіть операцію:")
    print("1. Обчислити швидкість (v = d / t)")
    print("2. Обчислити відстань (d = v * t)")
    print("3. Обчислити час (t = d / v)")
    print("4. Вийти з програми")

    choice = input("Ваш вибір: ")

    if choice == '1':
        d = float(input("Введіть відстань : ", 'метрів'))
        t = float(input("Введіть час : ", 'секунди'))
        v = calculate_speed(d, t)
        print(f"Швидкість: {v} м/с")
    elif choice == '2':
        v = float(input("Введіть швидкість (м/с): "))
        t = float(input("Введіть час (секунди): "))
        d = calculate_distance(v, t)
        print(f"Відстань: {d} метри")
    elif choice == '3':
        d = float(input("Введіть відстань : ", 'метрів'))
        v = float(input("Введіть швидкість (м/с): "))
        t = calculate_time(d, v)
        print(f"Час: {t} секунди")
    elif choice == '4':
        print("ok")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        main()

def calculate_speed(distance, time):
    return distance / time

def calculate_distance(speed, time):
    return speed * time

def calculate_time(distance, speed):
    return distance / speed

if __name__ == "__main__":
    main()