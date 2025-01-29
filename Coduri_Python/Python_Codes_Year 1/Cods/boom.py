import tkinter,time
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=600 , height=600 , bg = 'black')

bomb = tkinter.PhotoImage(file = 'bomb.png')
boom = tkinter.PhotoImage(file = 'boom.png')
count_created = 0
count_dest = 0
bombs = []
booms = []
def state():
    master.title(f'Create: {count_created} , Dest.:{count_dest}')
def mouse_click1(event):
    global count_created
    x = event.x
    y = event.y
    id_bomb = canvas.create_image(x,y,image = bomb)
    bombs.append(id_bomb)
    count_created +=1
    state()

def mouse_click2(event):
    global count_dest
    x = event.x
    y = event.y
    for i in range(len(bombs)-1,-1,-1):
        x1,y1 = canvas.coords(bombs[i])
        if x >= x1-32 and x<=x1+32 and y >= y1-32 and y<=y1+32:
            canvas.delete(bombs[i])
            del bombs[i]
            id_boom = canvas.create_image(x1,y1, image = boom)
            booms.append(id_boom)
            count_dest +=1
            state()





master.bind('<Button-1>', mouse_click1)
master.bind('<Button-3>', mouse_click2)
canvas.pack()
master.mainloop()