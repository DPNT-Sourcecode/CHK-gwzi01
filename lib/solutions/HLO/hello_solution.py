

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    
    if not isinstance(friend_name, str):
        raise TypeError
    try:
        return "{} says Hello World!".format(friend_name)
    except TypeError:
        return "A string must be passed to this function"

