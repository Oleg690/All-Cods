import tkinter,random
master = tkinter.Tk()
canvas = tkinter.Canvas(master , width=500,height=500,bg= 'black')
master.title('Mere mâncate:')
snake = []
direction = 0 
id_rect = canvas.create_rectangle((240,240),(260,260),fill = '#00ff00')
need_grow = False
count_apple = 0
move_interval = 300 
stop = False
id_create_apple = -1
id_apple = -1

def move():
    global need_grow , id_create_apple, stop , count_apple , id_apple
    front = canvas.coords(id_rect)
    if direction == 0:
        canvas.move(id_rect,20,0)
    elif direction == 1:
        canvas.move(id_rect, 0,20)
    elif direction == 2:
        canvas.move(id_rect,-20,0)
    elif direction == 3:
        canvas.move(id_rect,0,-20)

    for i in snake:
        new_front = canvas.coords(i)
        canvas.coords(i,front)
        front = new_front
    head_coord = canvas.coords(id_rect)
    
    if head_coord[0]<0 or head_coord[2]>500 or head_coord[1]<0 or head_coord[3]>500:
        master.title('Ai pierdut!')
        stop = True
        return
    
    for i in snake:
        if head_coord == canvas.coords(i):
            master.title('Ai pierdut!')
            stop = True
            return

    if need_grow == True:
        snake.append(canvas.create_rectangle(front , fill = 'yellow'))
        need_grow = False

    if id_apple !=-1:
       if head_coord == canvas.coords(id_apple):
           canvas.delete(id_apple)
           id_apple =-1
           count_apple +=1
           master.title(f'Mere mâncate: {count_apple}') 
           master.after_cancel(id_create_apple)
           id_create_apple = -1
           create_apple()

    master.after(move_interval,move)

def snake_grow():
    global need_grow
    need_grow = True
    master.after(3000,snake_grow)

def key_down(event):
    global direction
    if event.keysym == 'd':
        direction = 0
    elif event.keysym == 's':
        direction = 1
    elif event.keysym == 'a':
        direction = 2
    elif event.keysym == 'w':
        direction = 3

def create_apple():
    global id_apple,id_create_apple
    if stop == True:
        return
    if id_apple !=-1:
        canvas.delete(id_apple)
        id_apple = -1
    while True:
        left = random.randint(0,24)*20
        top = random.randint(0,24)*20
        coord = canvas.coords(id_rect)
        if coord[0] == left and coord[1] == top:
            continue
        intersect = False
        for i in snake:
            coord = canvas.coords(i)
            if coord[0] == left and coord[1] == top:
                intersect = True
                break
        if intersect == True:
            continue
        id_apple = canvas.create_rectangle((left,top),(left+20,top+20),fill = 'red')
        break
    id_create_apple= master.after(10000,create_apple)

def speed():
    global move_interval
    move_interval -= 100
    if move_interval == 100:
        return

move()
master.bind('<Key>',key_down)
master.after(3000,snake_grow)
master.after(5000,create_apple)
master.after(10000,speed)
canvas.pack()
master.mainloop()