

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    try:
        return "{} says Hello World!".format(friend_name)
    except TypeError:
        return "A string must be passed to this function"

