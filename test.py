import turtle as tr

 
def fibonachi(num):
    fibo = [0, 1]
    if num < 2:
        return fibo[num]
    
    else:
        for i in range(2, num+1):
            fibo.append(fibo[i-1]+ fibo[i-2])
    return fibo[i]

print(fibonachi(10))


number = 10
screen = tr.Screen()
screen.title("fibonacci")
screen.bgcolor("pink")

pen = tr.Turtle()
pen.speed(100)
for j in range(180):
    for i in range(number):
        pen.circle(fibonachi(i)*10, 45)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.left(100)



tr.mainloop()

