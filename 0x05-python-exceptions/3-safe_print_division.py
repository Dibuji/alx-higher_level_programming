#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
    finally:
        pass
