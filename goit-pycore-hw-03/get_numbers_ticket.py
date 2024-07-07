import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and (quantity >= min and quantity <= max):
        random_numbers_list = []
        for i in range(quantity):
            random_value = random.randint(min, max)
            if random_value not in random_numbers_list:
                random_numbers_list.append(random_value)
            else:
                while True:
                    random_value = random.randint(min, max)
                    if random_value not in random_numbers_list:
                        random_numbers_list.append(random_value)
                        break
        return sorted(random_numbers_list)
    else:
        return 'plz use correct conditions for min (min >= 1), max (max >=1 and max <= 1000) and quantity (betweem min and max) values'

if __name__ == '__main__':
    input_values = input('input min, max and quantity plz (using space to separate) - ')
    input_values = input_values.split()

    if len(input_values) != 3:
        print('plz input correct values')
    else:
        try:
            input_values = [int(value) for value in input_values]
            numbers_ticket = get_numbers_ticket(input_values[0], input_values[1], input_values[2])
            if numbers_ticket is not None:
                print('your numbers_tiket - {}'.format(numbers_ticket))
        except ValueError as value_error:
            print('plz input correct numbers')
