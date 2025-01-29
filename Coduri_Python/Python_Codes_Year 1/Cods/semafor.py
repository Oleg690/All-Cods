import time

state = 0

while True:
    if state == 0:
        print('Verde')
        time.sleep(5)
        state = 1
    elif state == 1:
        print('Galben')
        time.sleep(2)
        state = 2
    elif state == 2:
        print('Rosu')
        time.sleep(5)
        state = 3
    elif state == 3:
        print('Galben')
        time.sleep(2)
        state = 0