class JustNotCoolError(Exception):
    pass


x = 2
try:
    # custom exceptions are not common though
    raise JustNotCoolError("This just isn't cool, man!")
    # print(x / 1)
    # if not type(x) is str:
    #     raise TypeError('Only strings are allowed.')
except NameError:
    print('NameError means somthing is porbably undefined')
except ZeroDivisionError:
    print('Please do not divide by 0.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without error")
