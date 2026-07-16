import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    r = int(input_data[0])
    c = int(input_data[1])
    
    idx = 2
    for _ in range(r):
        # Extract the current row of size C
        row = input_data[idx : idx + c]
        
        # Reverse the row using slicing [::-1] and print it as a space-separated string
        print(" ".join(row[::-1]))
        
        # Move the index to the start of the next row
        idx += c

if __name__ == "__main__":
    main()