import random

def get_numbers_ticket(min, max, quantity):

    if not (1 <= min <= max <= 1000):
        return []

    total_numbers = max - min + 1

    if quantity < 1 or quantity > total_numbers:
        return []

    ticket = random.sample(range(min, max + 1), quantity)
    ticket.sort()
    return ticket


if __name__ == "__main__": 
    try:
        floor = int(input("Enter floor value (1–1000): "))
        ceil  = int(input("Enter ceil value (>= floor, ≤1000): "))
        qty   = int(input("Enter quantity: "))
    except ValueError:
        print("Error: Please enter whole numbers only.")
    else:
        nums = get_numbers_ticket(floor, ceil, qty)
        if nums:
            print("Ваші лотерейні числа:", nums)
        else:
            print("Параметри неправильні — нічого не згенеровано.")



   
