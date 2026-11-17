def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    while steps > 0:
        f_x = 2*a*x0 + b
        x0 = x0 - lr * f_x 
        steps -= 1


    return x0