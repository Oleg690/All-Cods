# Minipaint
import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master , width=600 , height=600, bg = 'black')
start_x = -1
start_y = -1
rects = []
mooving_list = []
offset_x = -1
offset_y = -1


def button1(event):
    global start_x,start_y
    start_x = event.x
    start_y = event.y
    id_rect = canvas.create_rectangle((start_x,start_y),(start_x,start_y), outline = 'white' , width=5)
    rects.append(id_rect)


def motion(event):
    x = event.x
    y = event.y
    if start_x !=-1:
        canvas.coords(rects[-1] , (start_x,start_y , x ,y ))
    elif len(mooving_list) > 0:
        for i in mooving_list:
            mooving_id = i[0] # [[1,2,3] , [4,5,6]]
            offset_x = i[1]
            offset_y = i[2]
            rect_coords = canvas.coords(mooving_id)
            width = rect_coords[2] - rect_coords[0]
            height = rect_coords[3] - rect_coords[1]
            left = x - offset_x
            top = y - offset_y
            canvas.coords(mooving_id , (left, top , left+width , top + height))

def button3(event):
    global mooving_id , offset_y , offset_x
    x = event.x
    y = event.y
    for i in rects:
        x1,y1,x2,y2 = canvas.coords(i)
        if x >=x1 and x<=x2 and y>=y1 and y<=y2:
            offset_x = x-x1
            offset_y = y-y1
            mooving_list.append([i , offset_x, offset_y])

def button3_rel(event):
    global mooving_list
    mooving_list = []

def button1_rel(event):
    global start_x,start_y
    start_x = -1
    start_y = -1

def button2(event):
    if len(rects)>0:
        canvas.delete(rects[-1])
        del rects[-1]

master.bind('<Button-1>',button1)
master.bind('<Button-2>',button2)
master.bind('<Button-3>',button3)
master.bind('<Motion>',motion)
master.bind('<ButtonRelease-1>',button1_rel)
master.bind('<ButtonRelease-3>',button3_rel)
canvas.pack()
master.mainloop()