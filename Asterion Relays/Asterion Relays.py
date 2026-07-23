import sys

def main():
    # Read all input simultaneously from standard input for maximum speed
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    # N is the number of dormant relays.
    # The total number of locations is N + 1 (including the Central Dock at index 0).
    n = int(input_data[0])
    num_nodes = n + 1
    
    # Parse the (N+1) x (N+1) energy cost matrix
    cost = []
    idx = 1
    for _ in range(num_nodes):
        row = []
        for _ in range(num_nodes):
            row.append(int(input_data[idx]))
            idx += 1
        cost.append(row)
        
    # Number of possible combinations of visited nodes is 2^(N+1).
    num_states = 1 << num_nodes
    INF = float('inf')
    
    # Initialize DP table.
    # dp[mask][u] represents the minimum cost to visit the subset of nodes 
    # encoded in `mask`, where the last visited node is `u`.
    dp = [[INF] * num_nodes for _ in range(num_states)]
    
    # Base case: We start at the Central Dock (node 0).
    # The binary representation of our visited set is `1` (which is 1 << 0).
    dp[1][0] = 0
    
    # Iterate through all possible subsets of visited locations
    # Since every valid state must include the Central Dock, the 0-th bit must be 1.
    # Therefore, we can safely step by 2.
    for mask in range(1, num_states, 2):
        # Localize variable lookups for speed
        dp_mask = dp[mask]
        
        for u in range(num_nodes):
            cost_u = dp_mask[u]
            
            # If this state is unreachable (or 'u' isn't in 'mask'), skip to save time
            if cost_u != INF:
                row_u = cost[u]
                
                # Try jumping from node 'u' to any unvisited node 'v'
                for v in range(1, num_nodes):
                    # Check if the v-th bit is 0 (meaning 'v' is NOT visited yet)
                    if not (mask & (1 << v)):
                        # Create the new mask representing the state after visiting 'v'
                        nxt_mask = mask | (1 << v)
                        nxt_cost = cost_u + row_u[v]
                        
                        # If this route is cheaper, update the dp table
                        if nxt_cost < dp[nxt_mask][v]:
                            dp[nxt_mask][v] = nxt_cost
                            
    # The ultimate goal is the state where EVERY node has been visited.
    # This is a bitmask consisting of (N+1) ones.
    final_mask = num_states - 1
    min_total_energy = INF
    
    # Evaluate the cost to return to the Central Dock (node 0) from whatever
    # node 'u' we happened to finish the activation sequence on.
    for u in range(1, num_nodes):
        if dp[final_mask][u] != INF:
            total_energy = dp[final_mask][u] + cost[u][0]
            if total_energy < min_total_energy:
                min_total_energy = total_energy
                
    # Output the absolute minimum energy required
    print(min_total_energy)

if __name__ == '__main__':
    main()