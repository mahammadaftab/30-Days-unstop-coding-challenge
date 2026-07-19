import sys

def main():
    # Read entire input block rapidly
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Initialize adjacency lists for the original and reversed graph (1-indexed)
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        
    # Pass 1: Gather post-order finishing times iteratively
    visited = [False] * (n + 1)
    order = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                # Positive ID implies exploring down the tree
                if node > 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                    
                    # Push the negative representation as a post-order marker
                    stack.append(-node)
                    
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                # Negative ID means all children were visited, safe to add to finishing order
                else:
                    order.append(-node)
                    
    # Pass 2: Traverse transposed graph in reverse finishing order
    scc_id = [0] * (n + 1)
    current_scc = 0
    
    for i in reversed(order):
        if scc_id[i] == 0:
            current_scc += 1
            stack = [i]
            scc_id[i] = current_scc
            
            while stack:
                curr = stack.pop()
                for neighbor in rev_adj[curr]:
                    if scc_id[neighbor] == 0:
                        scc_id[neighbor] = current_scc
                        stack.append(neighbor)
                        
    # Collapse the graph and compute incoming connections per SCC
    in_degree = [0] * (current_scc + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                in_degree[scc_id[v]] += 1
                
    # Count how many Independent components exist
    required_announcers = sum(1 for i in range(1, current_scc + 1) if in_degree[i] == 0)
    
    print(required_announcers)

if __name__ == '__main__':
    main()