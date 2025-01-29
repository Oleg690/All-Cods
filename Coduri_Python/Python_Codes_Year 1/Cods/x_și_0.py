import tkinter
master = tkinter.Tk()
master.title('X și 0')
size = 5
cell_size = 150
canvas = tkinter.Canvas(master, width = cell_size*size,\
 height = cell_size*size, bg = 'black')

index = 0

for i in range(cell_size, (size-1)*cell_size +1, cell_size):
    canvas.create_line((0, i), (cell_size*size, i), fill= 'white')
    canvas.create_line((i, 0), (i, cell_size*size), fill= 'white')
    if index == 2:
        index -=2
    else:
        index +=1

def button1(event):
    x = event.x
    y = event.y
    row = y//cell_size
    col = x//cell_size
    master.title(f'randul = {row+1}, coloana = {col+1}')
    print(x,y)
    cell_x = col*cell_size
    cell_y = row*cell_size
    canvas.create_rectangle((cell_x,cell_y),\
    (cell_x+cell_size,cell_y+cell_size), fill = 'white')

master.bind('<Button-1>',button1)
canvas.pack()
master.mainloop()