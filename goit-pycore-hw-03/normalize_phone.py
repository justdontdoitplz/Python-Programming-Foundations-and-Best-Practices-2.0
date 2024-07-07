import re

REGEXP_PATTERN = '[^0-9]'

def normalize_phone(phone):
    phone = re.sub(REGEXP_PATTERN, '', phone)
    if phone.startswith('38'):
        return '+' + phone
    else: 
        return '+38' + phone
    
if __name__ == '__main__':
    raw_numbers = [
        '067\\t123 4567',
        '(095) 234-5678\\n',
        '+380 44 123 4567',
        '380501234567',
        '    +38(050)123-32-34',
        '     0503451234',
        '(050)8889900',
        '38050-111-22-22',
        '38050 111 22 11   ',
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)