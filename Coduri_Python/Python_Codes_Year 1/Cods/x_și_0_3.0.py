import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width = 300, height = 300, bg = 'black')

id_rect_matrix = []
for i in range(10):
    line = []
    for j in range(10):
        line.append(-1)
    id_rect_matrix.append(line)

row, col = -1, -1
id_rect = -1

for i in range(30,271,30):
    canvas.create_line((0,i),(300,i),fill = 'white')
    canvas.create_line((i,0),(i,300),fill = 'white')

def motion(event):
    global row,col,id_rect
    move_row = event.y//30
    move_col = event.x//30

    if move_row != row or move_col != col:
        if id_rect != -1:
            canvas.delete(id_rect)
            id_rect = -1
    
    left = move_col*30
    top = move_row*30
    id_rect = canvas.create_rectangle((left,top),(left+30,top+30),fill = 'white')

master.bind('<Motion>',motion)
canvas.pack()
master.mainloop()