import sys

def solve():
    # Read all tokens efficiently from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    M = int(input_data[0])
    masks = [int(x) for x in input_data[1:M+1]]
    S = int(input_data[M+1])
    T = int(input_data[M+2])
    
    # We want to find a subset of masks that XOR together to produce target_xor
    target_xor = S ^ T
    
    # Meet-in-the-Middle approach to minimize the subset size
    M1 = M // 2
    
    def get_combinations(masks_subset):
        # Maps an achieved XOR sum to the minimum number of switches used
        res = {0: 0}
        
        for m in masks_subset:
            updates = {}
            for xor_sum, sz in res.items():
                new_xor = xor_sum ^ m
                new_sz = sz + 1
                
                # Update if this XOR sum is newly discovered or reached with fewer switches
                if new_xor not in res or new_sz < res[new_xor]:
                    updates[new_xor] = new_sz
                    
            # Safely merge updates into the main dictionary
            res.update(updates)
            
        return res
        
    # Generate all optimal reachable states for both halves
    res_left = get_combinations(masks[:M1])
    res_right = get_combinations(masks[M1:])
    
    ans = float('inf')
    
    # Find the optimal pairing that forms the target_xor
    for xor_right, sz_right in res_right.items():
        needed = xor_right ^ target_xor
        
        if needed in res_left:
            total_switches = sz_right + res_left[needed]
            if total_switches < ans:
                ans = total_switches
                
    # Output result or -1 if impossible
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()