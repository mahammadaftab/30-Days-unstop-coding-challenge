import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Extract the positions and threshold limits
    X = [int(x) for x in input_data[1:n+1]]
    Th = [int(x) for x in input_data[n+1:2*n+1]]
    
    # M1 isolates the max required right-shift bound
    M1 = max([x + t for x, t in zip(X, Th)])
    
    # M2 isolates the max required left-shift bound
    M2 = max([-x + t for x, t in zip(X, Th)])
    
    # M3 handles the bare minimum individual threshold capability
    M3 = max(Th)
    
    # Calculate the ceiling of (M1 + M2) / 2 using integer division
    req_P = (M1 + M2 + 1) // 2
    
    # The minimum valid power is the maximum constraint out of the two
    ans = max(M3, req_P)
    
    # Print the absolute minimum power P required
    print(ans)

if __name__ == '__main__':
    main()