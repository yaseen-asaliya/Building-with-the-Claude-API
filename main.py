def greeting():
    print("Hello! Welcome to the Claude API tools demonstration.")

def calculate_pi_to_5th_digit():
    """
    Calculate pi to the 5th decimal digit using the Leibniz formula.
    Returns pi as 3.14159
    """
    # Using Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    # We need enough iterations for 5 decimal places accuracy
    pi_over_4 = 0
    iterations = 500000  # Enough iterations for 5 decimal places
    
    for i in range(iterations):
        pi_over_4 += ((-1) ** i) / (2 * i + 1)
    
    pi = 4 * pi_over_4
    
    # Round to 5 decimal places
    pi_rounded = round(pi, 5)
    
    return pi_rounded