# Excercise 2 (b)


from e2a import *


def reporter(f, x):

    try:
        f(x)
    except ValueError:
        return "Value"
    
    except E2OddError:
        return "E2Even"
    
    except E2Error:
        return "E2"
    
    except Exception:
        return "E"
    
    else:
        return "okay"

        
        
        
