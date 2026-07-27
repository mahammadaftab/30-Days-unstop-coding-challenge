import sys

def main():
    # Read the input efficiently and strip any surrounding whitespace or newlines
    s = sys.stdin.read().strip()
    
    # Safeguard for empty input
    if not s:
        return
        
    # Check if the string is identical to its reverse using Python's fast slicing
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()