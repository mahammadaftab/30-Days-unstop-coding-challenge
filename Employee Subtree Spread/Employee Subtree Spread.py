# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def main():
    # Read all input simultaneously from standard input for maximum speed
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    N = int(input_data[0])
    
    # Adjacency list for the tree (1-indexed)
    adj = [[] for _ in range(N + 1)]
    
    idx = 1
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        # Since it's a tree, we record bidirectional edges
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    Q = int(input_data[idx])
    idx += 1
    
    # Arrays to store parent, pathScore and visited state
    parent = [0] * (N + 1)
    pathScore = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    # Queue for Level-Order Traversal (BFS)
    # Using a list and an index pointer is faster than collections.deque 
    # for simple flat insertions in massive datasets.
    queue = [1]
    visited[1] = True
    
    q_idx = 0
    while q_idx < len(queue):
        u = queue[q_idx]
        q_idx += 1
        
        # Explore subordinates (neighbors)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                pathScore[v] = pathScore[u] + w
                queue.append(v)
                
    # Initialize min and max scores with the employee's own pathScore
    min_score = list(pathScore)
    max_score = list(pathScore)
    
    # Process nodes from bottom to top (reverse level-order)
    # This magically propagates the min and max scores up to the root safely 
    # without incurring any Stack Overflow recursion limits.
    for i in range(len(queue) - 1, -1, -1):
        u = queue[i]
        p = parent[u]
        
        # If the current employee isn't the CEO, report extremes up to their manager
        if p != 0:
            if min_score[u] < min_score[p]:
                min_score[p] = min_score[u]
            if max_score[u] > max_score[p]:
                max_score[p] = max_score[u]
                
    # Process all queries instantly in O(1) time each
    out = []
    for _ in range(Q):
        v = int(input_data[idx])
        idx += 1
        
        # The spread is strictly the difference between max and min score in the subtree
        out.append(str(max_score[v] - min_score[v]))
        
    # Print all answers rapidly separated by newlines
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()