import sys

def main():
    # Read all input simultaneously for maximum I/O speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    num_guardians = 2 * n
    
    # Parse the compatibility matrix
    comp = []
    idx = 1
    for _ in range(num_guardians):
        row = []
        for _ in range(num_guardians):
            row.append(int(input_data[idx]))
            idx += 1
        comp.append(row)
        
    # The ultimate goal is the state where EVERY guardian has been paired.
    # This is a bitmask consisting of '2N' ones.
    full_mask = (1 << num_guardians) - 1
    
    # dp[mask] will store the max compatibility score for the paired guardians in `mask`
    # We initialize with -1 to indicate unreachable states.
    dp = [-1] * (full_mask + 1)
    
    # Base case: 0 guardians paired yields 0 compatibility
    dp[0] = 0
    
    # Create a fast lookup array to translate a single set bit back to its index
    # The maximum bit we can encounter is (1 << (2N - 1)), which fits easily in memory
    bit_to_idx = [0] * (1 << num_guardians)
    for i in range(num_guardians):
        bit_to_idx[1 << i] = i
        
    # Iterate through all possible subsets of paired guardians
    for mask in range(full_mask):
        current_score = dp[mask]
        
        # If this state is unreachable (or invalid), skip it
        if current_score == -1:
            continue
            
        # Find all guardians that have NOT been paired yet
        inv = full_mask ^ mask
        
        # Get the LOWEST unset bit (the first unpaired guardian)
        # By forcing the first available guardian to pair, we skip evaluating 
        # identical duplicate sets in different orders!
        lowest_unset = inv & -inv
        i = bit_to_idx[lowest_unset]
        
        # Cache the row for the selected guardian to speed up lookups
        row_i = comp[i]
        
        # The remaining available guardians to pair with guardian 'i'
        remaining = inv ^ lowest_unset
        
        # Try pairing guardian 'i' with every other available guardian 'j'
        while remaining:
            # Extract the next lowest available guardian from the remaining pool
            j_bit = remaining & -remaining
            j = bit_to_idx[j_bit]
            
            # Form the pair and transition to the new state
            nxt_mask = mask | lowest_unset | j_bit
            nxt_score = current_score + row_i[j]
            
            # Update the DP table if this pairing combination yields a higher score
            if nxt_score > dp[nxt_mask]:
                dp[nxt_mask] = nxt_score
                
            # Clear the bit we just processed to move on to the next available guardian
            remaining ^= j_bit
            
    # Output the absolute maximum compatibility score once all guardians are paired
    print(dp[full_mask])

if __name__ == '__main__':
    main()