# Exercise 1(a)

def square_root (x, eps):
    '''(float, float) -> float
    Return the square root of x to within an accuracy of eps
    >>> square_root (2, 0.01)
    1.4142
    '''
    this_guess = 1.0

    i = 1
    while i > 0:
        next_guess = 0.5 * (this_guess + x/this_guess)
        i += 1
        if (abs(next_guess - this_guess) < eps):
            return next_guess
        else:
            this_guess = next_guess
        if i > 10:
            return -1.0

  
        

        
    


        
        

        

    
        

        

        

            
