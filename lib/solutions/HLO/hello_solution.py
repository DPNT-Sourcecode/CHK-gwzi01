

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    
    if not isinstance(friend_name, str):
        raise TypeError("A string must be passed to this function")
    else:
        return "Hello, {}!".format(friend_name)
