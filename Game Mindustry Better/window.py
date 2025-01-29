import tkinter as tk
import keyboard

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#print(screen_width)
#print(screen_height)

root.title("Mindustry")
root.attributes('-fullscreen', False)
root.geometry(f'{screen_width-400}x{screen_height-200}')

label = tk.Label(root, text="This is a full screen window")
label.pack()

def on_key_press(event):
    #print(f"Key {event.name} pressed")
    if event.name == 'f11':
        if root.attributes('-fullscreen') == True:
            root.attributes('-fullscreen', False)
        else:
            root.attributes('-fullscreen', True)
            root.geometry(f'{screen_width-400}x{screen_height-200}')

keyboard.on_press(on_key_press)

root.mainloop()