import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Extract energy values into a list (0-indexed)
    energy = [int(x) for x in input_data[1:n+1]]
    
    # Initialize DP array with infinity. 
    # dp[i] stores the minimum energy to reach tower i.
    dp = [float('inf')] * n
    
    # Base case: Starting at the first tower costs 0 energy.
    dp[0] = 0
    
    # Fill the DP table
    for j in range(1, n):
        for i in range(j):
            # Calculate the cost to jump from tower i to tower j
            jump_cost = abs(energy[i] - energy[j]) * (j - i)
            
            # Update the minimum energy to reach tower j
            if dp[i] + jump_cost < dp[j]:
                dp[j] = dp[i] + jump_cost
                
    # The result is the minimum energy to reach the last tower (index n - 1)
    print(dp[n - 1])

if __name__ == "__main__":
    main()