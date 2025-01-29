import ctypes

def main():
    message = "You are Hacked"
    title = "ERROR"
    style = 0x40  # Icon: Information

    ctypes.windll.user32.MessageBoxW(0, message, title, style)

if __name__ == "__main__":
    for i in range(1, 37):
        main()