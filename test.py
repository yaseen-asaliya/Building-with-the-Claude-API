"""
Test file for the pi calculation function in main.py
"""
import math
from main import calculate_pi_to_5th_digit


def test_pi_calculation():
    """
    Test the calculate_pi_to_5th_digit function
    """
    # Get the calculated pi value
    calculated_pi = calculate_pi_to_5th_digit()
    
    # Expected value of pi to 5 decimal places
    expected_pi = 3.14159
    
    # Also compare with Python's math.pi rounded to 5 decimal places
    math_pi_rounded = round(math.pi, 5)
    
    print("=" * 50)
    print("Pi Calculation Test Results")
    print("=" * 50)
    print(f"Calculated Pi:        {calculated_pi}")
    print(f"Expected Pi:          {expected_pi}")
    print(f"Python's math.pi:     {math.pi}")
    print(f"math.pi (rounded):    {math_pi_rounded}")
    print("=" * 50)
    
    # Check if the calculated value matches expected
    if calculated_pi == expected_pi:
        print("✓ TEST PASSED: Calculated pi matches expected value!")
    else:
        print(f"✗ TEST FAILED: Expected {expected_pi}, got {calculated_pi}")
    
    # Check if it matches Python's math.pi (rounded)
    if calculated_pi == math_pi_rounded:
        print("✓ TEST PASSED: Calculated pi matches math.pi (rounded to 5 digits)!")
    else:
        print(f"✗ TEST FAILED: math.pi rounded is {math_pi_rounded}, got {calculated_pi}")
    
    # Check the type
    if isinstance(calculated_pi, float):
        print("✓ TEST PASSED: Return type is float")
    else:
        print(f"✗ TEST FAILED: Expected float, got {type(calculated_pi)}")
    
    print("=" * 50)
    
    return calculated_pi == expected_pi and calculated_pi == math_pi_rounded


if __name__ == "__main__":
    print("\nRunning pi calculation tests...\n")
    success = test_pi_calculation()
    
    if success:
        print("\n🎉 All tests passed successfully!")
    else:
        print("\n⚠️  Some tests failed. Please review the results above.")
