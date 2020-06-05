import turtle

name = input('What is your ZZZ name?\n')
print('Hi, %s.' % name)

t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    t.color(c)
    t.forward(75)
    t.left(90)



turtle.write("Home = Hello", True, align="center")