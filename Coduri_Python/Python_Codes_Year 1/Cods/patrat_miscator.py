import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=600 , height=600 , bg = 'gray')
rect = canvas.create_rectangle((250,250),(350,350), fill = 'yellow')
mooving = False
rect_x = 0
rect_y = 0
def motion(event):
    x = event.x
    y = event.y
    #master.title(f'x = {x} , y = {y}')
    if mooving == True:
        left = x-rect_x
        top = y-rect_y
        canvas.coords(rect, (left,top,left+100,top+100))


def mouse_click1(event):
    global mooving, rect_x, rect_y
    x = event.x
    y = event.y
    master.title(f'x = {x} , y = {y}, {True}')
    x1,y1,x2,y2 = canvas.coords(rect)
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        mooving = True
        rect_x = x-x1
        rect_y = y-y1

def mouse_click2(event):
    global mooving
    x = event.x
    y = event.y
    master.title(f'x = {x} , y = {y}, {False}')
    mooving = False

def move():
    if mooving == False:
        canvas.move(rect,0,1)
    master.after(10,move)

master.bind('<Motion>',motion)
master.bind('<Button-1>',mouse_click1)
master.bind('<ButtonRelease-1>',mouse_click2)
move()
canvas.pack()
master.mainloop()