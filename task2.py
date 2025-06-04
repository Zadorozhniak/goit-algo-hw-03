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

def draw_koch_snowflake():
    # Налаштування екрану
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    screen.bgcolor("white")
    
    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    
    # Запит рівня рекурсії у користувача
    depth = screen.numinput("Рівень рекурсії", 
                           "Введіть рівень рекурсії (ціле число від 0 до 5):", 
                           minval=0, maxval=5)
    depth = int(depth) if depth is not None else 3
    
    # Малюємо сніжинку (3 криві Коха)
    length = 300
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_koch_snowflake()
