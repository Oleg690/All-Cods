import tkinter,random

master = tkinter.Tk()

canvas = tkinter.Canvas(master,width=600,height=600,bg = 'black')
r = 16

count = 0
cercuri = []
def create_cerc():
    d = r*2
    left = random.randint(0,600-d)
    top = random.randint(0,600-d)
    cerc = canvas.create_oval((left,top),(left+d,top+d), fill = 'yellow')
    cercuri.append(cerc)
    master.title(f'Bile:{len(cercuri)}')
    master.after(100, create_cerc)
def vector_move():
    x = master.winfo_pointerx() - master.winfo_rootx()
    y = master.winfo_pointery() - master.winfo_rooty()
    for i in range(len(cercuri)-1 , -1 , -1):
        x1,y1,x2,y2  = canvas.coords(cercuri[i])
        left = 0
        top = 0
        x_centru = x1+r
        y_centru = y1+r

        if x > x_centru:
            left = 1
        elif x < x_centru:
            left = -1

        if y > y_centru:
            top = 1
        elif y < y_centru:
            top =-1

        if left != 0 or top !=0:
            canvas.move(cercuri[i], left, top)
        else:
            canvas.delete(cercuri[i])
            del cercuri[i]

    master.after(20 , vector_move)
canvas.pack()
create_cerc()
vector_move()

master.mainloop()