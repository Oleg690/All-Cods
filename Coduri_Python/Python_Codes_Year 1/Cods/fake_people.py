import random
import emoji
from faker import Faker

fake_person = Faker('ro_RO')

emojis = ['👍', '💪', '👅', '👶']

random_emoji = random.choice(emojis)

first_word = ['Nice', 'Cool', 'Great', 'Good']

second_word = ['Video', 'Content', 'Vid', 'Stream', 'Live']

random_first_word = random.choice(first_word)
random_second_word = random.choice(second_word)

print(f'Nume: {fake_person.name()}')

print(emoji.emojize(f'Comentariu: {random_first_word} {random_second_word} {random_emoji}'))