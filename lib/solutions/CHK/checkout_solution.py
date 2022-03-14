import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Could do with knowing what format the input is, unless this is deliberate! :)
    # Assuming the input string is going to look something like AABBBBC etc

    if not isinstance(skus, str):
        print("invalid input")
        return -1        

    if re.findall('[^A-D]', skus) or not re.findall('[A-D]', skus):
        print("invalid input")
        return -1
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')

    cost_A = (int(num_A / 3) * 130) + (num_A % 3 * 50)
    cost_B = (int(num_B / 2) * 45) + (num_B % 2 * 30)
    cost_C = 20 * num_C
    cost_D = 15 * num_D
    
    return cost_A + cost_B + cost_C + cost_D







