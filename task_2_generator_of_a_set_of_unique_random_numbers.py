import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> int:
        if not (1 <= min <= max <= 1000 and quantity <= (max - min + 1)):
            return ("...\nПомилка розрахунку. "
            "Введені аргументи виходять за межі діапазону. "
            "\nБудь ласка, вкажіть валідні значення! ")

        else:
            return random.sample(range(min, max), k=quantity)
        

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")
