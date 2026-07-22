import sys
from collections import deque

def main():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Initialize a fast double-ended queue
    waiting_line = deque()
    
    idx = 1
    # Process all operations
    while idx < len(input_data):
        op = input_data[idx]
        
        if op == "ENTER":
            # Extract the vehicle ID. We can keep it as a string 
            # to save the overhead of converting to integer.
            vehicle_id = input_data[idx + 1]
            waiting_line.append(vehicle_id)
            idx += 2 # Move past 'ENTER' and 'X'
            
        elif op == "EXIT":
            # Remove the front vehicle if the line isn't already empty
            if waiting_line:
                waiting_line.popleft()
            idx += 1 # Move past 'EXIT'
            
    # Check the final state of the waiting line
    if waiting_line:
        # Print the vehicle currently at the front
        print(waiting_line[0])
    else:
        print("EMPTY")

if __name__ == "__main__":
    main()