import math


def calculate_trajectory(initial_height, initial_velocity, angle_degrees):

    g = 9.81

    
    angle_rad = math.radians(angle_degrees)


    initial_vertical_velocity = initial_velocity * math.sin(angle_rad)
    initial_horizontal_velocity = initial_velocity * math.cos(angle_rad)

    
    time_of_flight = (2 * initial_vertical_velocity) / g


    max_height = (initial_vertical_velocity**2) / (2 * g)


    horizontal_distance = initial_horizontal_velocity * time_of_flight

    return time_of_flight, max_height, horizontal_distance


initial_height = float(input("Введіть початну висоту (метри): "))
initial_velocity = float(input("Введіть початну швидкість (м/с): "))
angle_degrees = float(input("Введіть кут відносно горизонту (градуси): "))


time_of_flight, max_height, horizontal_distance = calculate_trajectory(
    initial_height, initial_velocity, angle_degrees)


print(f"Час польоту: {time_of_flight} секунд")
print(f"Максимальна висота: {max_height} метрів")
print(f"Горизонтальна відстань: {horizontal_distance} метрів")
