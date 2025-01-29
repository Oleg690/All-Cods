import tkinter, random
master = tkinter.Tk()

master.title('Balon')
canvas = tkinter.Canvas(master, width = 600, height = 600, bg = 'lightblue')
cell_width = random.randint(30,60)
cell_width = random.randint(40,80)
canvas.create_oval((300-cell_width/2,400),(300+cell_width/2,480+cell_width),fill = 'yellow')


canvas.pack()
master.mainloop()