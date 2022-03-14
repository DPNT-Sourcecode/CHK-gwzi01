import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Could do with knowing what format the input is, unless this is deliberate! :)
    # Assuming the input string is going to look something like AABBBBC etc

    if not re.findall('[^A-D]', skus):
        print("invalid input")
        return -1
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')

    cost_C = 20 * num_C
    cost_D = 20 * num_D

    if num_A >= 3:
        cost_A = (int(num_A / 3) * 130) + 





