import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master,height=300,width = 300, bg = 'white')

for i in range(30,271,30):
    canvas.create_line((0,i),(300,i),fill = 'black')
    canvas.create_line((i,0),(i,300),fill = 'black')

num = 0
for row in range(10):
    for col in range(10):
        x = col*30+15
        y = row*30+15
        canvas.create_text((x,y),text = str(num+1), fill = 'blue', font = 'Arial 12 bold')
        num +=1
canvas.pack()
master.mainloop()