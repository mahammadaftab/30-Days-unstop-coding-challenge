import sys
from bisect import bisect_left, bisect_right

def solve():
    # Read all input simultaneously for maximum speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    M = int(input_data[1])
    
    idx = 2
    edges = []
    # Parse all treaties (edges)
    for _ in range(M):
        edges.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])))
        idx += 4
        
    Q = int(input_data[idx])
    idx += 1
    
    queries_raw = []
    queried_times = set()
    
    # Parse all queries and isolate the exact days that are requested
    for i in range(Q):
        t = int(input_data[idx+2])
        queries_raw.append((int(input_data[idx]), int(input_data[idx+1]), t, i))
        queried_times.add(t)
        idx += 3
        
    # Sort and compress time
    times = sorted(list(queried_times))
    K = len(times)
    if K == 0:
        return
        
    # Find the nearest power of 2 for the Segment Tree size
    P = 1
    while P < K:
        P <<= 1
        
    tree = [[] for _ in range(P << 1)]
    
    # Insert treaties into the Segment Tree ranges
    for u, v, l, r in edges:
        # Find the span of queried times this treaty covers
        L_idx = bisect_left(times, l)
        R_idx = bisect_right(times, r) - 1
        
        # If the treaty spans at least one requested query day
        if L_idx <= R_idx:
            curr_L = L_idx + P
            curr_R = R_idx + P
            
            # Map into logarithmic tree components
            while curr_L <= curr_R:
                if curr_L & 1:
                    tree[curr_L].append((u, v))
                    curr_L += 1
                if not (curr_R & 1):
                    tree[curr_R].append((u, v))
                    curr_R -= 1
                curr_L >>= 1
                curr_R >>= 1
                
    time_to_idx = {t: i for i, t in enumerate(times)}
    queries_by_time = [[] for _ in range(K)]
    for u, v, t, i in queries_raw:
        queries_by_time[time_to_idx[t]].append((u, v, i))
        
    ans = ["NO"] * Q
    
    # DSU Arrays
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    history = []
    
    # Iterative DFS state tracking
    applied_counts = [0] * (P << 1)
    stack = [1]
    
    while stack:
        node = stack.pop()
        
        # Positive node signifies branching down (Enter)
        if node > 0:
            stack.append(-node) # Queue up the backtrack (Exit) action
            count = 0
            
            # Localizing arrays for faster lookups in Python
            for u, v in tree[node]:
                # Find operation (without path compression)
                root_u = u
                while parent[root_u] != root_u:
                    root_u = parent[root_u]
                root_v = v
                while parent[root_v] != root_v:
                    root_v = parent[root_v]
                    
                # Union operation by size
                if root_u != root_v:
                    if size[root_u] < size[root_v]:
                        root_u, root_v = root_v, root_u
                    parent[root_v] = root_u
                    size[root_u] += size[root_v]
                    history.append((root_v, root_u)) # Save state for rollback
                    count += 1
                    
            applied_counts[node] = count
            
            # If we hit a Leaf, resolve all specific queries for this day
            if node >= P:
                idx_time = node - P
                if idx_time < K:
                    for u, v, q_idx in queries_by_time[idx_time]:
                        root_u = u
                        while parent[root_u] != root_u:
                            root_u = parent[root_u]
                        root_v = v
                        while parent[root_v] != root_v:
                            root_v = parent[root_v]
                        if root_u == root_v:
                            ans[q_idx] = "YES"
            else:
                # Push right then left children
                stack.append((node << 1) | 1)
                stack.append(node << 1)
                
        # Negative node signifies jumping back up (Exit)
        else:
            node = -node
            count = applied_counts[node]
            # Rollback all applied treaties for this node
            for _ in range(count):
                root_v, root_u = history.pop()
                size[root_u] -= size[root_v]
                parent[root_v] = root_v
                
    # Output results
    sys.stdout.write("\n".join(ans) + "\n")

if __name__ == '__main__':
    solve()