import sys

def main():
    # Read all lines from standard input
    input_lines = sys.stdin.read().splitlines()
    
    if len(input_lines) < 2:
        return
        
    # The first line is the message string
    s = input_lines[0].strip()
    
    # The second line is the target character
    c = input_lines[1].strip()
    
    # Use Python's highly optimized built-in count method
    print(s.count(c))

if __name__ == "__main__":
    main()