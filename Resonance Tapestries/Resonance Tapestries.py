import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Extract the dimensions of the weaving frames
    # The frames are defined by dimensions p[0] to p[N]
    p = [int(x) for x in input_data[1:n+2]]
    
    # Create a 2D DP array initialized to 0
    # dp[i][j] will store the minimum energy required to fuse frames from i to j.
    # Note: We use a 1-indexed DP table for easier mapping to frame numbers.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # L is the length of the chain of frames we are considering
    # We start from chains of length 2 up to chains of length N
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            # j is the ending index of the current chain
            j = i + L - 1
            
            # Pre-fetch boundary values to optimize the inner loop's lookups
            pi_1 = p[i - 1]
            pj = p[j]
            
            # Initialize with infinity to find the minimum cost
            min_cost = float('inf')
            
            # Try splitting the chain at every possible point k between i and j-1
            for k in range(i, j):
                # Calculate the cost of fusing the left part, right part, and combining them
                cost = dp[i][k] + dp[k + 1][j] + pi_1 * p[k] * pj
                
                if cost < min_cost:
                    min_cost = cost
                    
            # Store the optimal minimum cost for the chain i to j
            dp[i][j] = min_cost
            
    # The final answer is the cost to fuse all frames from 1 to N
    print(dp[1][n])

if __name__ == "__main__":
    main()