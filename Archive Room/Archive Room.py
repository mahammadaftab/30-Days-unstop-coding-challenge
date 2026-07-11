import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Python lists natively function as highly efficient stacks
    stack = []
    
    idx = 1
    for _ in range(n):
        op = input_data[idx]
        
        if op == "ADD":
            # Read the value to add and push it onto the stack
            x = int(input_data[idx + 1])
            stack.append(x)
            idx += 2 # Move index past 'ADD' and 'X'
        elif op == "REMOVE":
            # Pop the top element if the stack is not empty
            if stack:
                stack.pop()
            idx += 1 # Move index past 'REMOVE'
            
    # Check the final state of the stack
    if not stack:
        print("-1")
    else:
        # Print the last element (top of the stack)
        print(stack[-1])

if __name__ == "__main__":
    main()