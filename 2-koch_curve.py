import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)
        t.right(120)
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)

def draw_snowflake(t, length, depth):
    for i in range(3):
        koch_curve(t, length, depth)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.title("Кохів Фрактал Сніжинка")
    
    t = turtle.Turtle()
    t.speed(0)
    
    recursion_level = int(input("Будь ласка, введіть рівень рекурсії: "))
    # Зміна довжини сторони фрактала
    length = 300  

    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    draw_snowflake(t, length, recursion_level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()