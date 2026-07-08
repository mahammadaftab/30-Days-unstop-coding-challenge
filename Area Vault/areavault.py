import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    prev2 = 0 # Represents MaxAt[i-2]
    prev1 = 0 # Represents MaxAt[i-1]
    
    # Process each chamber
    for i in range(n):
        crystal = int(input_data[i + 1])
        current = max(prev1, prev2 + crystal)
        
        prev2 = prev1
        prev1 = current
        
    print(prev1)

if __name__ == "__main__":
    main()