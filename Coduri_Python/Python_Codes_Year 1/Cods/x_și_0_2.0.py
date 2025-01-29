import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width = 250, height = 250, bg = 'black')
count_rect = 0
id_rect = [-1 for i in range(25)]

for i in range(50,251,50):
    canvas.create_line((0,i),(250,i),fill = 'white')
    canvas.create_line((i,0),(i,250),fill = 'white')

def button1(event):
    global count_rect, id_rect
    x = event.x
    y = event.y
    row = y // 50
    col = x // 50
    if row > 5 or col > 5:
        return

    cell_num = row*5+col
    if id_rect[cell_num] != -1:
        return
    cell_x = col*50
    cell_y = row*50
    _id = canvas.create_rectangle((cell_x,cell_y),(cell_x+50,cell_y+50),fill = 'white')
    count_rect += 1
    master.title(f'count={count_rect}')
    id_rect[cell_num] = _id

def button3(event):
    global id_rect, count_rect
    x = event.x
    y = event.y
    row = y // 50
    col = x // 50
    if row > 5 or col > 5:
        return
    
    cell_num = row*5+col
    if id_rect[cell_num] == -1:
        return

    canvas.delete(id_rect[cell_num])
    id_rect[cell_num] = -1
    count_rect -= 1
    master.title(f'count={count_rect}')

master.bind('<Button-3>',button3)
master.bind('<Button-1>',button1)
canvas.pack()
master.mainloop()