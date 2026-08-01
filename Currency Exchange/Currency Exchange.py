import sys

def solve():
    # Read all tokens efficiently from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    P = 1000000007
    
    # Disjoint Set Union structures
    # parent[i] = parent of node i
    parent = list(range(N + 1))
    
    # weight[i] = exchange rate from i to parent[i], meaning W(i, parent[i])
    weight = [1] * (N + 1)
    
    # rank[i] = depth bound of tree rooted at i (used to keep tree shallow)
    rank = [0] * (N + 1)
    
    def find(x):
        # Base case: x is the root of its component
        if parent[x] == x:
            return x
        
        p = parent[x]
        root = find(p)
        
        # Path compression:
        # Update the weight to be relative directly to the root
        # W(x, root) = W(x, p) * W(p, root) (mod P)
        weight[x] = (weight[x] * weight[p]) % P
        parent[x] = root
        
        return root

    idx = 2
    out = []
    
    for _ in range(M):
        type = int(input_data[idx])
        
        if type == 1:
            u = int(input_data[idx+1])
            v = int(input_data[idx+2])
            p_val = int(input_data[idx+3])
            q_val = int(input_data[idx+4])
            idx += 5
            
            # Desired exchange rate: W(u, v) = p * q^-1 (mod P)
            R = (p_val * pow(q_val, P - 2, P)) % P
            
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                # They are already connected; verify if the implied rate aligns with R
                # W(u, v) = W(u, root) / W(v, root) (mod P)
                implied_rate = (weight[u] * pow(weight[v], P - 2, P)) % P
                if implied_rate == R:
                    out.append("OK")
                else:
                    out.append("CONTRADICTION")
            else:
                # Not connected; link the smaller rank tree under the larger rank tree
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                    # We need to set W(root_u, root_v). 
                    # W(u, v) = W(u, root_u) * W(root_u, root_v) * W(root_v, v)
                    # W(root_u, root_v) = R * weight[v] * weight[u]^-1 (mod P)
                    weight[root_u] = (R * weight[v] * pow(weight[u], P - 2, P)) % P
                else:
                    parent[root_v] = root_u
                    # We need to set W(root_v, root_u).
                    # W(v, u) = R^-1
                    # W(root_v, root_u) = R^-1 * weight[u] * weight[v]^-1 (mod P)
                    inv_R = pow(R, P - 2, P)
                    weight[root_v] = (inv_R * weight[u] * pow(weight[v], P - 2, P)) % P
                    
                    if rank[root_u] == rank[root_v]:
                        rank[root_u] += 1
                        
                out.append("OK")
                
        else:
            u = int(input_data[idx+1])
            v = int(input_data[idx+2])
            idx += 3
            
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                # Connected; compute and print the implied rate
                implied_rate = (weight[u] * pow(weight[v], P - 2, P)) % P
                out.append(str(implied_rate))
            else:
                # Disconnected; the relationship is unknown
                out.append("UNKNOWN")
                
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()