import random

input_length = input("Introduceți lungimea parolei: ")

alphabet = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z', 'A',
            'B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S',
            'T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

special_characters = ['!', '@', '#', '$', '%', '^',
                      '&', '*', '(', ')', '_', '-',
                      '=', '+', '[', ']', '{', '}',
                      ';', ':', ',', '.', '<', '>',
                      '/', '?', '|', '\\', '`', '~']


password = ''
print(list)


while True:
    print("Introduceți ce doriți să selectați:")
    print('1 - alphabet;')
    print('2 - numbers and alphabet;')
    print('2 - numbers and alphabet;')
    print('3 - numbers and alphabet and special characters')
    print('4 - close')
    print('5 - re-input the length')
    select = int(input())

    if select == 1:
        for i in range(0, int(input_length)):
            alphabet_choice_random = random.choice(alphabet)
            list2 = [alphabet_choice_random]
            password += random.choice(list2)
        print()
        print(password)
        print()
        password = ''
    elif select == 2:
        for i in range(0, int(input_length)):
            alphabet_choice_random = random.choice(alphabet)
            number_choice_random = random.choice(numbers)
            list = [alphabet_choice_random, number_choice_random]
            password += random.choice(list)
        print()
        print(password)
        print()
        password = ''
    elif select == 3:
        for i in range(0, int(input_length)):
            sp_char_choice_random = random.choice(special_characters)
            alphabet_choice_random = random.choice(alphabet)
            number_choice_random = random.choice(numbers)
            list = [sp_char_choice_random, alphabet_choice_random, number_choice_random]
            password += random.choice(list)
        print()
        print(password)
        print()
        password = ''
    elif select == 4:
        break
    if select == 5:
        input_length = input("Introduceți lungimea parolei: ")

print('By, by')