

# default name
name = ""

def __console():
    return raw_input("> ")
    
def say(message = "",params = []):
    if len(params) < 1:
        print message
    else:
        print message % params

def ask(thing = ""):
    if len(thing) > 1:
        print thing
    return __console()
    
