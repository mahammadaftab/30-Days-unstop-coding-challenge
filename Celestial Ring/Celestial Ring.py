import sys

def main():
    # Read all data from standard input instantaneously
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    q = int(input_data[1])
    
    arr = [0] * n
    idx = 2
    for i in range(n):
        arr[i] = int(input_data[idx])
        idx += 1
        
    # Parse queries
    queries = []
    for i in range(q):
        # Convert 1-based indices to 0-based for array access
        l = int(input_data[idx]) - 1
        r = int(input_data[idx+1]) - 1
        queries.append((l, r, i))
        idx += 2
        
    # Mo's Algorithm Block Size
    # N / sqrt(Q) is mathematically optimal for minimizing pointer movements
    s = max(1, int(n / (q ** 0.5)))
    
    # Sort queries:
    # Group by block (L // S)
    # Even blocks sort R ascending, Odd blocks sort R descending
    # This zig-zag optimization drastically reduces the R pointer's travel distance!
    queries.sort(key=lambda x: (x[0] // s, x[1] if (x[0] // s) % 2 == 1 else -x[1]))
    
    ans = [0] * q
    
    # Max frequency code is 10^6. We flat-allocate it for maximum memory speed.
    count = [0] * 1000005 
    current_ans = 0
    
    L, R = 0, -1
    
    # Process queries using sliding window
    for qL, qR, q_idx in queries:
        
        # Expand R
        while R < qR:
            R += 1
            x = arr[R]
            c = count[x]
            current_ans += (c << 1) + 1
            count[x] = c + 1
            
        # Expand L
        while L > qL:
            L -= 1
            x = arr[L]
            c = count[x]
            current_ans += (c << 1) + 1
            count[x] = c + 1
            
        # Shrink R
        while R > qR:
            x = arr[R]
            c = count[x] - 1
            current_ans -= (c << 1) + 1
            count[x] = c
            R -= 1
            
        # Shrink L
        while L < qL:
            x = arr[L]
            c = count[x] - 1
            current_ans -= (c << 1) + 1
            count[x] = c
            L += 1
            
        # Record the answer for this specific query
        ans[q_idx] = current_ans
        
    # Print all answers rapidly
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

if __name__ == '__main__':
    main()