import re

# noinspection PyUnusedLocal
# skus = unicode string

non_offer_prices = {
    ("C", 20),
    ("D", 15),
    ("E", 40),
    ("G", 20),
    ("I", 35),
    ("J", 60),
    ("L", 90),
    ("M", 15),
    ("O", 10),
    ("R", 50),
    ("S", 30),
    ("T", 20),
    ("W", 20),
    ("X", 90),
    ("Y", 10),
    ("Z", 50),
}

double_offers = [
    ("A", (3, 130), (5, 200)),
    ("H", (5, 45), (10, 80)),
    ("V", (2, 90), (3, 130)),
]

single_offers = [
    ("K", 2, 150),
    ("P", 5, 200)
]



def checkout(skus):

    if not isinstance(skus, str):
        print("invalid input")
        return -1        

    if re.findall('[^A-Z]', skus):
        print("invalid input")
        return -1

    non_offer_cost = 0

    for product in non_offer_prices:
        num_product = skus.count(product[0])
        product_cost = num_product * product[1]
        non_offer_cost += product_cost
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    num_E = skus.count('E')
    num_F = skus.count('F')

    cost_A = calculate_A(num_A)
    cost_B = calculate_B(num_B, num_E)
    cost_C = 20 * num_C
    cost_D = 15 * num_D
    cost_E = 40 * num_E
    cost_F = calculate_F(num_F)

    #print(skus)
    #print(cost_A, cost_B, cost_C, cost_D, cost_E, cost_F)
    
    return cost_A + cost_B + cost_C + cost_D + cost_E + cost_F


def calculate_A(num_A):
    
    fives_of_A = int(num_A / 5)
    remainder_A = num_A - fives_of_A * 5
    #print(fives_of_A, remainder_A)

    threes_of_A = int(remainder_A / 3)
    remainder_A = remainder_A - threes_of_A * 3
    #print(threes_of_A, remainder_A)

    return fives_of_A * 200 + threes_of_A * 130 + remainder_A * 50


def calculate_B(num_B, num_E):

    if num_B == 0:
        return 0
    
    free_B = 0
    
    if num_E >= 2:
        free_B = int(num_E / 2)

    num_B = num_B - free_B
    #print(num_B, free_B)

    return (int(num_B / 2) * 45) + (num_B % 2 * 30)

def calculate_F(num_F):

    free_F = int(num_F / 3)
    num_F = num_F - free_F

    #print(num_F)

    return num_F * 10







