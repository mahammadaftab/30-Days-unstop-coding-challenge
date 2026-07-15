import sys
import bisect

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Extract the scores into a list
    scores = [int(x) for x in input_data[1:n+1]]
    
    # 'tails' will store the smallest tail elements of increasing subsequences
    tails = []
    
    for score in scores:
        # Find the index of the first element in 'tails' that is >= 'score'
        # bisect_left performs a fast binary search in O(log N) time
        idx = bisect.bisect_left(tails, score)
        
        # If score is greater than all elements currently in tails,
        # we can extend our longest sequence.
        if idx == len(tails):
            tails.append(score)
        else:
            # Otherwise, we replace the existing element. This keeps the potential 
            # tails as small as possible, allowing for easier future extensions.
            tails[idx] = score
            
    # The length of the tails array is the length of the Longest Increasing Subsequence
    print(len(tails))

if __name__ == "__main__":
    main()