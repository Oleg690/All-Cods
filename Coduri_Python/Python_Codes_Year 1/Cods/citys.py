city = input('Introduceti orasul: ')

while True:
    prior_city = city
    
    prior_char = prior_city[-1]
    city = input(f'Introduceti un oras care se incepe cu litera {prior_char}: ')

    if not city.startswith(prior_char):
        print('STOP JOC')
        break