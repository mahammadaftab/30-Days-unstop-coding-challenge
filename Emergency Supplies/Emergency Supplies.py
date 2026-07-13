import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    k = int(input_data[1])
    
    # Parse the priorities into a list
    priorities = [int(x) for x in input_data[2:n+2]]
    
    # Sort the priorities in descending order
    priorities.sort(reverse=True)
    
    # Select the first K packages
    top_k_packages = priorities[:k]
    
    # Print the result as space-separated integers
    print(*(top_k_packages))

if __name__ == "__main__":
    main()