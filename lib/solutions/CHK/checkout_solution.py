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
    ("W", 20),
}

double_offers = [
    ("A", 50, (3, 130), (5, 200)),
    ("H", 10, (5, 45), (10, 80)),
    ("V", 50, (2, 90), (3, 130)),
]

single_offers = [
    ("K", 80, 2, 150),
    ("P", 50, 5, 200),
]

get_one_free_offers = [
    ("F", 10, 3),
    ("U", 40, 4)
]

# base_prices sorted by value
group_offers = [
    {
        "STXYZ": {
            "base_prices": {
                "X": 17,
                "S": 20,
                "T": 20,
                "Y": 20,
                "Z": 21
            },
            "offer": {
                "required_number": 3,
                "discount_price": 45
            }
        }
    }
]

inter_dependant_offers = ["B", "M", "Q"]


def checkout(skus):

    if not isinstance(skus, str):
        print("invalid input")
        return -1        

    if re.findall('[^A-Z]', skus):
        print("invalid input")
        return -1

    total_cost = 0

    #print("\n\n\n\n" + skus)

    for product in non_offer_prices:
        num_product = skus.count(product[0])
        product_cost = num_product * product[1]
        total_cost += product_cost
        #print("non offer", total_cost)
    
    for product in double_offers:
        num_product = skus.count(product[0])
        product_cost = calculate_double_offer_cost(num_product, product[1], product[2], product[3])
        total_cost += product_cost
        #print("double offer", total_cost)

    for product in single_offers:
        num_product = skus.count(product[0])
        product_cost = calculate_single_offer_cost(num_product, product[1], product[2], product[3])
        total_cost += product_cost
        #print("single_offer", total_cost)

    for product in get_one_free_offers:
        num_product = skus.count(product[0])
        product_cost = calculate_get_one_free_cost(num_product, product[1], product[2])
        total_cost += product_cost
        #print("bogof", total_cost)

    for offer in group_offers:
        total_cost += calculate_group_offer_cost(skus, offer)

    total_cost += calculate_B(skus.count("B"), skus.count("E"))
    #print("B", total_cost)
    total_cost += calculate_M(skus.count("M"), skus.count("N"))
    ##print("M", total_cost)
    total_cost += calculate_Q(skus.count("Q"), skus.count("R"))
    #print("Q", total_cost)
    
    return total_cost


def calculate_double_offer_cost(num, base_price, lesser_offer, best_offer):
    
    best_offer_num = int(num / best_offer[0])
    remainder = num - best_offer_num * best_offer[0]
    #print(best_offer_num, remainder)

    lesser_offer_num = int(remainder / lesser_offer[0])
    remainder = remainder - lesser_offer_num * lesser_offer[0]
    #print(lesser_offer_num, remainder)

    return best_offer_num * best_offer[1] + lesser_offer_num * lesser_offer[1] + remainder * base_price


def calculate_single_offer_cost(num, base_price, required_num, offer_price):

    return int(num / required_num) * offer_price + (num % required_num) * base_price


def calculate_get_one_free_cost(num, base_cost, required_num):

    if num == 0:
        return 0

    free = int(num / required_num)
    num = num - free

    #print(num_F)

    return num * base_cost


def calculate_group_offer_cost(skus, offer):

    total_number = 0
    counts = {}
    
    for product in offer["base_prices"]:
        total_number += skus.count(product)
        counts[product] = skus.count(product)

    number_of_groups = int(total_number / offer["offer"]["required_number"])

    remainder = int(total_number % offer["offer"]["required_number"])

    remainder_cost = 0

    while remainder > 0:
        for purchased in counts:
            if counts[purchased] > 0:
                remainder_cost += offer["base_prices"][purchased]
                counts[purchased] = counts[purchased] - 1
            break

    return number_of_groups * offer["offer"]["required_number"] + remainder_cost


def calculate_B(num_B, num_E):

    if num_B == 0:
        return 0
    
    free_B = 0
    
    if num_E >= 2:
        free_B = int(num_E / 2)

    num_B = num_B - free_B
    #print(num_B, free_B)

    return (int(num_B / 2) * 45) + (num_B % 2 * 30)


def calculate_M(num_M, num_N):

    if num_M == 0:
        return 0

    free_M = 0

    if num_N >= 3:
        free_M = num_M - int(num_M / 3)

    num_M = num_M - free_M

    return num_M * 15


def calculate_Q(num_Q, num_R):

    if num_Q == 0:
        return 0
    
    free_Q = 0
    
    if num_R >= 3:
        free_Q = int(num_R / 3)

    num_Q = num_Q - free_Q

    return (int(num_Q / 3) * 80) + (num_Q % 3 * 30)



