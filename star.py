import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
  turtle.forward(400)   # 400ピクセル書く
  turtle.left(144)  # 角度指定
  if abs(turtle.pos()) < 1:
    break

turtle.end_fill()
turtle.done()