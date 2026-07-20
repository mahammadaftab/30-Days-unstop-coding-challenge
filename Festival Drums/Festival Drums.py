import sys
import math

def main():
    # Read inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if len(input_data) < 2:
        return
        
    # Parse the intervals for Kabir's and Tara's drums
    a = int(input_data[0])
    b = int(input_data[1])
    
    # The next simultaneous beat is exactly the LCM of their intervals.
    # We use integer division (//) to keep the result as an exact integer.
    lcm_result = (a * b) // math.gcd(a, b)
    
    # Output the calculated waiting time
    print(lcm_result)

if __name__ == "__main__":
    main()