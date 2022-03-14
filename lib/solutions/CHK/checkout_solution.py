import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Could do with knowing what format the input is, unless this is deliberate! :)
    # Assuming the input string is going to look something like AABBBBC etc

    A_matches = re.search('\dA')
    B_matches = re.search('\dB')
    C_matches = re.search('\dB')
    D_matches = re.search('\dB')



