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
    ("N", 40),
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
    ("A", 50, (3, 130), (5, 200)),
    ("H", 10, (5, 45), (10, 80)),
    ("V", 50, (2, 90), (3, 130)),
]

single_offers = [
    ("K", 2, 150),
    ("P", 5, 200),
]

get_one_free_offers = [
    ("F", 2, 10),
    ("U", 3, 40)
]

inter_dependant_offers = ["B", "M", "Q"]



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
    
    for product in double_offers:
        num_product = skus.count(product[0])
        product_cost = calculate_double_offer_cost(num_product, product[1], product[2], product[3])

    cost_A = calculate_A(num_A)
    cost_B = calculate_B(num_B, num_E)
    cost_C = 20 * num_C
    cost_D = 15 * num_D
    cost_E = 40 * num_E
    cost_F = calculate_F(num_F)

    #print(skus)
    #print(cost_A, cost_B, cost_C, cost_D, cost_E, cost_F)
    
    return cost_A + cost_B + cost_C + cost_D + cost_E + cost_F


def calculate_double_offer_cost(num, base_price, offer_1, offer_2):
    
    offer_2_num = int(num / offer_2[0])
    remainder = num - offer_2_num * offer_2[0]
    #print(fives_of_A, remainder_A)

    offer_1_num = int(num / offer_1[0])
    remainder = num - offer_1_num * offer_1[0]
    #print(threes_of_A, remainder_A)

    return offer_2_num * offer_2[1] + offer_1 * 130 + remainder_A * 50


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
