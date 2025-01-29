import tkinter
import json
import subprocess

file = open('data.txt', 'r', encoding='utf-8')
data = json.load(file)
file.close()

#--------------------------------------------------------------------------
# Variable

users = []
passwords = []
users_passwords = []
result = ''
psw = ''
user1 = ''

#--------------------------------------------------------------------------

# Users and Passwords finder from the data.txt
for i in data.keys():
    users.append(i)
for i in data:
    passwords.append(data[i][0])
users_passwords = list(zip(users, passwords))

def execute_python_project(file_path):
    try:
        subprocess.Popen(["python", file_path])
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")

def sing_up():
    global error_label, master1
    python_project_path = "register.py"  
    try:
        execute_python_project(python_project_path)
        master1.destroy()
    except FileNotFoundError:
        error_label = tkinter.Label(master1, text=f"File not found: {python_project_path}")
        error_label.pack(pady=10)
    except Exception as e:
        error_label = tkinter.Label(master1, text=f"Error: {str(e)}")
        error_label.pack(pady=10)

# Command for btn to find in the list of users and passwords the match form the input
def btn1():
    global user1, user, password
    user = text_input1.get()
    password = text_input2.get()

    for pair in users_passwords:
        search_element = user
        result = [pair[1] for pair in users_passwords if pair[0] == search_element]

    if user in users and password in result:
        global error_label, master1
        python_project_path = "main.py"

        try:
            execute_python_project(python_project_path)
            master1.destroy()
        except FileNotFoundError:
            print('Hello World!')
        except Exception as e:
            print('Hello World!')
    else:
        user1 = 'User or Password incorrect!'
        label.config(text=user1)

#--------------------------------------------------------------------------

# Login Window
master1 = tkinter.Tk()
master1.title('Login')
canvas = tkinter.Canvas(width=400, height=400, bg='#D3D3D3')

font = ('Calibri', 18)
text_font = ('Calibri', 16)
bg_label = '#D3D3D3'

# The text from the window

label = tkinter.Label(text=user1 ,font=text_font, bg=bg_label)
label.place(x=90, y=330)

label1 = tkinter.Label(text="User:", bg=bg_label, font=font)
label1.place(x=170, y=50)

label2 = tkinter.Label(text="Password:", bg=bg_label, font=font)
label2.place(x=150, y=150)

# The inputs from the window
text_input1 = tkinter.Entry(width=22, font=text_font)
text_input1.place(x=80, y=90)

text_input2 = tkinter.Entry(width=22, font=text_font)
text_input2.place(x=80, y=190)

# The button from the login window

btn1 = tkinter.Button(text='Submit',command=btn1 , width=8, font=text_font, borderwidth=1)
btn1.place(x=100, y=260)

btn2 = tkinter.Button(text='Register',command=sing_up , width=8, font=text_font, borderwidth=1)
btn2.place(x=210, y=260)

canvas.pack()
master1.mainloop()