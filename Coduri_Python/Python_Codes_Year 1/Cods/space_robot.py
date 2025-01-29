x = open('D:\\gaina.txt', 'r', encoding='utf-8')
text = x.read()
x.close

text2 = ''
count_space = 0

for i in text:
    if i == ' ':
        count_space += 1
        if count_space == 1:
            text2 += i
        else:
            continue
    else:
        text2 += i
        count_space = 0
        
start_sentence = True
text3 = ''

for i in text2:
    if i == '.' or i == '!':
        start_sentence = True
        text3 += i
    elif i != ' ' and start_sentence == True:
        text3 += i.upper()
        start_sentence = False
    else:
        text3 += i

x = open('D:\\gaina_fixed.txt', 'w', encoding='utf-8')
x.write(text3)
x.close()
