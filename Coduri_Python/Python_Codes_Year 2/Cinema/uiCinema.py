import tkinter
import json

file = open('Python Codes Year 2\Cinema\\txt\data.txt', 'r', encoding='utf-8')
data = json.load(file)
file.close()

file = open('Python Codes Year 2\Cinema\\txt\\booking.txt', 'r', encoding='utf-8')
booking = json.load(file)
file.close()

cells = {}

master = tkinter.Tk()
master.title('Cinema')
canvas = tkinter.Canvas(width=550, height=480, bg='#D3D3D3')
widget_font = ('Arial', 12, 'bold')

for i in  range(1,16):
    canvas.create_line((0, i * 30), (550, i*30))

for i in range(1, 11):
    canvas.create_line((i * 50, 0), (i*50, 480))

for i in range(1, 16):
    canvas.create_text(25, 15 + i * 30, text=i, font=widget_font)

for i in range(1, 11):
    canvas.create_text(25 + i*50, 15, text=i, font=widget_font)

for i in data:
    _range = i.split(':')

    for j in range(int(_range[0]), int(_range[1])+1):
        for k in range(1, 11):
            price = data[i][0]
            color = data[i][1]

            cell = f'{j}:{k}'

            if cell in booking:
                color = 'grey'

            x1 = k * 50
            y1 = j * 30

            cell_id = canvas.create_rectangle((x1, y1), (x1 + 50, y1 + 30), fill = color)
            cells[cell] = cell_id

            canvas.create_text(25 + k * 50, 15 + j * 30, text=str(price), font=widget_font)

canvas.pack()

def mouseClick1(event):
    col = event.x // 50
    row = event.y // 30

    if col < 1 or row < 1:
        return
    
    cell = f"{row}:{col}"

    if not cell in booking:
        booking.append(cell)

        id_cell = cells[cell]
        canvas.itemconfig(id_cell, fill='gray')

def mouseClick3(event):
    col = event.x // 50
    row = event.y // 30

    if col < 1 or row < 1:
        return
    
    cell = f"{row}:{col}"

    if cell in booking:
        booking.remove(cell)

        color = ''

        for i in data:
            _range = i.split(':')

            if row >= int(_range[0]) and row <= int(_range[1]):
                color = data[i][1]
                break

        id_cell = cells[cell]
        canvas.itemconfig(id_cell, fill=color)

master.bind('<Button-1>', mouseClick1)
master.bind('<Button-3>', mouseClick3)
master.mainloop()

file = open('Python Codes Year 2\Cinema\\txt\\booking.txt', 'w', encoding='utf-8')
json.dump(booking, file, indent=4)
file.close()