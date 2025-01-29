from prettytable import PrettyTable
from faker import Faker
import random

table = PrettyTable()

table.field_names = ['Nume', 'Clasa', 'Nota medie']

for i in range(4):
    grade = random.randint(5, 12)    
    fake_human = Faker()
    random_mark = random.uniform(4.99, 10.01)
    mark = round(random_mark, 2)
    table.add_row([f'{fake_human.name()}', f'{grade}', f'{mark}'])

print(table)