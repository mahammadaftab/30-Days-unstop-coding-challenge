import sys
from bisect import bisect_left

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Extract the manuscript inscriptions
    strings = input_data[1 : n + 1]
    
    # Sort the strings lexicographically
    # This naturally groups all strings that share the same prefix together in a continuous block
    strings.sort()
    
    q = int(input_data[n + 1])
    queries = input_data[n + 2 :]
    
    out = []
    
    # Process each scholar's request
    for query in queries:
        # Find the first string that is lexicographically >= the query
        left_idx = bisect_left(strings, query)
        
        # Find the first string that is >= query + '{'
        # Since '{' is the character immediately following 'z' in ASCII,
        # this perfectly identifies the strict upper boundary of strings starting with `query`.
        right_idx = bisect_left(strings, query + '{')
        
        # The number of matching manuscripts is the size of the block
        k = right_idx - left_idx
        
        # Calculate the number of unordered pairs: K * (K - 1) / 2
        pairs = k * (k - 1) // 2
        out.append(str(pairs))
        
    # Print all answers separated by a newline rapidly
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()