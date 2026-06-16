###----------*arg and **kwarg in python--------->
def funargs(*args):
    if args:
        print(args[0])
    else:
        print('No arguments provided')