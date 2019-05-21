#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except Exception as excep:
        print("Exception: {}".format(excep), file=sys.stderr)
        return None
