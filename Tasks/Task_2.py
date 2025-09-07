import turtle

def koch_curve(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)
        turtle.right(120)
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)

def draw_snowflake(level):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()

    for _ in range(3):
        koch_curve(300, level)
        turtle.right(120)

    turtle.done()

try:
    user_level = int(input("Введіть рівень рекурсії і натисніть 'Enter' (наприклад, 2 або 3): "))
    draw_snowflake(user_level)
except ValueError:
    print("✗ Помилка: потрібно ввести ціле число")
