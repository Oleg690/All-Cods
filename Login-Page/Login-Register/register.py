import tkinter
import json
import subprocess

file = open('data.txt', 'r', encoding='utf-8')
data = json.load(file)
file.close()

#--------------------------------------------------------------------------
# Variable

special_characters =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*','+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
users = []
passwords = []
users_passwords = []
result = ''
psw = ''
user1 = ''
user2 = ''

#--------------------------------------------------------------------------
# Users and Passwords finder from the data.txt

# Command for btn to find in the list of users and passwords the match form the input
def btn1():
    global user1, special_characters, user, password
    user = text_input1.get()
    password = text_input2.get()
    cnf_password = text_input3.get()

    if user.strip() and password.strip() and cnf_password.strip():
        if ' ' not in user and ' ' not in password and ' ' not in cnf_password:
            if not any(char in special_characters for char in user):
                if len(user) >= 4:
                    if password == cnf_password:
                        if len(password) >= 8:
                            if user not in data:
                                global user1, user2, users_passwords
                                user1 = 'Password saved successfully!'
                                user2 = "Let's login!"
                                label4.config(text=user1 ,font=text_font, bg=bg_label)
                                label4.place(x=80, y=380)
                                label5.config(text=user2 ,font=text_font, bg=bg_label)
                                label5.place(x=155, y=410)
                                add_data()
                            else:
                                user1 = 'This user is taken!'
                                user2 = ''
                                label4.config(text=user1 ,font=text_font, bg=bg_label)
                                label4.place(x=125, y=390)
                                label5.config(text=user2 ,font=text_font, bg=bg_label)
                                label5.place(x=155, y=4010)
                        else:
                            user1 = 'Password must be longer than 4 characters!'
                            user2 = ''
                            label4.config(text=user1 ,font=text_font, bg=bg_label)
                            label4.place(x=15, y=390)
                            label5.config(text=user2 ,font=text_font, bg=bg_label)
                            label5.place(x=155, y=4010)
                    else:
                        user1 = 'Passwords are not equal!'
                        user2 = ''
                        label4.config(text=user1 ,font=text_font, bg=bg_label)
                        label4.place(x=95, y=390)
                        label5.config(text=user2 ,font=text_font, bg=bg_label)
                        label5.place(x=155, y=4010)
                else:
                    user1 = 'User must be longer than 4 characters!'
                    user2 = ''
                    label4.config(text=user1 ,font=text_font, bg=bg_label)
                    label4.place(x=45, y=390)
                    label5.config(text=user2 ,font=text_font, bg=bg_label)
                    label5.place(x=155, y=4100)
            else:
                user1 = 'Somewhere there are invalid characters!'
                user2 = ''
                label4.config(text=user1 ,font=text_font, bg=bg_label)
                label4.place(x=45, y=390)
                label5.config(text=user2 ,font=text_font, bg=bg_label)
                label5.place(x=155, y=4100)
        else:
            user1 = 'There are spaces in the sections!'
            user2 = ''
            label4.config(text=user1 ,font=text_font, bg=bg_label)
            label4.place(x=65, y=390)
            label5.config(text=user2 ,font=text_font, bg=bg_label)
            label5.place(x=155, y=4100)
    else:
        user1 = 'Complete all the sections!'
        user2 = ''
        label4.config(text=user1 ,font=text_font, bg=bg_label)
        label4.place(x=90, y=390)
        label5.config(text=user2 ,font=text_font, bg=bg_label)
        label5.place(x=155, y=4010)

def execute_python_project(file_path):
    try:
        subprocess.Popen(["python", file_path])
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")

def login():
    global error_label
    python_project_path = "login.py"

    try:
        execute_python_project(python_project_path)
        master.destroy()
    except FileNotFoundError:
        error_label = tkinter.Label(master, text=f"File not found: {python_project_path}")
    except Exception as e:
        error_label = tkinter.Label(master, text=f"Error: {str(e)}")

def add_data():
    user_input = text_input1.get()
    password = text_input2.get()

    try:
        # Load existing JSON data from data.txt
        with open('data.txt', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    # Add the new data to the JSON object
    existing_data[user_input] = [password]

    # Write the updated JSON object back to data.txt with UTF-8 encoding
    with open('data.txt', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
#--------------------------------------------------------------------------

# Register Window
master = tkinter.Tk()
master.title('Register')
canvas = tkinter.Canvas(width=400, height=450, bg='#D3D3D3')

font = ('Calibri', 18)
text_font = ('Calibri', 16)
bg_label = '#D3D3D3'

#--------------------------------------------------------------------------
# The text from the window

label1 = tkinter.Label(text="User:", bg=bg_label, font=font)
label1.place(x=170, y=20)

label2 = tkinter.Label(text="Create Password:", bg=bg_label, font=font)
label2.place(x=120, y=120)

label3 = tkinter.Label(text="Verify Password:", bg=bg_label, font=font)
label3.place(x=120, y=220)

label4 = tkinter.Label(text=user1 ,font=text_font, bg=bg_label)
label4.place(x=75, y=390)

label5 = tkinter.Label(text=user2 ,font=text_font, bg=bg_label)
label5.place(x=75, y=420)

#--------------------------------------------------------------------------
# The inputs from the window

text_input1 = tkinter.Entry(width=22, font=text_font)
text_input1.place(x=80, y=60)

text_input2 = tkinter.Entry(width=22, font=text_font)
text_input2.place(x=80, y=160)

text_input3 = tkinter.Entry(width=22, font=text_font)
text_input3.place(x=80, y=260)

#--------------------------------------------------------------------------
# The button from the login window

btn1 = tkinter.Button(text='Submit',command=btn1 , width=8, font=text_font, borderwidth=1)
btn1.place(x=100, y=320)

btn2 = tkinter.Button(text='Login',command=login , width=8, font=text_font, borderwidth=1)
btn2.place(x=210, y=320)

canvas.pack()
master.mainloop()