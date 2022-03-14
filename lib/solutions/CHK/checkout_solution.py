import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        print("invalid input")
        return -1        

    if re.findall('[^A-E]', skus):
        print("invalid input")
        return -1
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    num_E = skus.count('E')

    fives_of_A = int(num_A / 5)
    threes_of_A = int((num_A - fives_of_A * 5) / 3)
    remainder_of_A = int()



    cost_B = (int(num_B / 2) * 45) + (num_B % 2 * 30)
    cost_C = 20 * num_C
    cost_D = 15 * num_D
    
    return cost_A + cost_B + cost_C + cost_D



