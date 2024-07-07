import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or min > max or max > 1000 or max-min < quantity:
        return []
    else:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min, max))
        numbers = list(numbers)
        numbers.sort()
        return numbers
    