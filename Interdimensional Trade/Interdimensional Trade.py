import sys

def main():
    # Read all input simultaneously from standard input for maximum speed
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    q = int(input_data[2])
    
    INF = float('inf')
    
    # Initialize the distance matrix with Infinity
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # The distance from any world to itself is 0
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    idx = 3
    # Parse the gateways
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        # In case of multiple gateways between the same two worlds, 
        # always keep the one with the lowest energy tax.
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
            
    # Floyd-Warshall Algorithm
    # Time Complexity: O(N^3) -> (400^3 = 64,000,000 operations)
    for k in range(1, n + 1):
        # Localizing array references speeds up Python loop execution
        dist_k = dist[k]
        
        for i in range(1, n + 1):
            dist_i = dist[i]
            dik = dist_i[k]
            
            # Optimization: If 'k' is unreachable from 'i', skip evaluating 'j'
            if dik != INF:
                for j in range(1, n + 1):
                    dkj = dist_k[j]
                    
                    # If routing through 'k' is cheaper, update the shortest path
                    if dkj != INF and dist_i[j] > dik + dkj:
                        dist_i[j] = dik + dkj
                        
    # Process all audit requests instantly in O(1) time each
    out = []
    for _ in range(q):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        ans = dist[u][v]
        # Output -1 if transport is impossible
        if ans == INF:
            out.append("-1")
        else:
            out.append(str(ans))
            
    # Print all answers rapidly
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()