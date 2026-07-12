import sys
from collections import Counter

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Parse the visitor IDs and count their frequencies efficiently
    # Python's Counter is a specialized dictionary for counting hashable objects
    counts = Counter(int(x) for x in input_data[1:n+1])
    
    best_id = None
    max_freq = -1
    
    # Iterate through the unique visitors and their attendance counts
    for visitor_id, freq in counts.items():
        # If we find a strictly higher frequency, update our best
        if freq > max_freq:
            max_freq = freq
            best_id = visitor_id
        # If frequencies are tied, choose the smaller visitor ID
        elif freq == max_freq:
            if visitor_id < best_id:
                best_id = visitor_id
                
    # Print the most active visitor ID and their frequency
    print(f"{best_id} {max_freq}")

if __name__ == "__main__":
    main()