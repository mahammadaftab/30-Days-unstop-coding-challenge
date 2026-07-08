import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    d = int(input_data[1])
    
    checkpoints = [int(x) for x in input_data[2:n+2]]
    checkpoints.sort()
    
    count = 1
    last_picked = checkpoints[0]
    
    for i in range(1, n):
        if checkpoints[i] - last_picked >= d:
            count += 1
            last_picked = checkpoints[i]
            
    print(count)

if __name__ == "__main__":
    main()