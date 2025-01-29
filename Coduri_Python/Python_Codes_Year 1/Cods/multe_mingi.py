import tkinter, random
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width= 600, height=600,bg='black')

culori = ('#00ffff', 'blue', '#ff00ff', 'green', 'maroon','pink', 'violet', 'red', 'yellow', 'violet', '#4b0082','chartreuse', '#00ff00', '#f55c4b')
cercuri = []
r = 30
def move(event):
  x = event.x
  y = event.y
  cerc = canvas.create_oval((x-r,y-r),(x+r,y+r),fill = random.choice(culori))
  cercuri.append(cerc)
  print(cercuri)
  if len(cercuri) > 30:
    canvas.delete(cercuri[0])
    del cercuri[0]
def mouseclick(event):
  canvas.delete('all')
  cercuri.clear()

master.bind('<Button-3>', mouseclick)

master.bind('<Motion>', move)
canvas.pack()
master.mainloop()
