import os, json

print('Content-type: text/html\n')

html = ''
task_number = 0

for i in os.listdir("algor"):
    index_ex = i.rfind('.')
    file_ex = i[index_ex + 1:]

    if file_ex != 'py':
        continue

    task_number += 1

    html += '<h2><i>Problema Nr.' + str(task_number) + '</i></h2>'
    file_name_txt = i[:index_ex] + '.txt'
    file_txt = open('algor/' + file_name_txt, 'r', encoding='utf-8')
    txt_ = file_txt.read()
    txt_ = txt_.replace('\n', '<br>')
    file_txt.close()

    html += '<p>' + txt_ + '</p>'

    html += '<h3>Algoritmul:</h3>'

    file_py = open('algor/' + i, 'r', encoding='utf-8')
    py = file_py.read()
    py = py.replace(' ', '&nbsp')
    py = py.replace('\n', '<br>')
    file_py.close()

    html += py

    html += '<br><br><br><hr>'

print(json.dumps(html))