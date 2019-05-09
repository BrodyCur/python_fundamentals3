# Exercise 11

# bit_range = range(1, 101)

# def bit_fizz(range):
#     for num in range:
#         if num % 3 == 0 and num % 5 == 0:
#             print('BitMaker')
#         elif num % 3 == 0:
#             print('Bit')
#         elif num % 5 == 0:
#             print('Maker')
#         else:
#             print(num)

# bit_fizz(bit_range)

# Exercise 12

def pizza_maker():
    customer_order = int(input("How many pizzas do you want? "))
    quantity = range(1, customer_order + 1)

    for pizza in quantity:
        print(f"How many toppings for pizza {pizza}?")
        topping_number = int(input())
        print(f"You have ordered a pizza with {topping_number}")

pizza_maker()