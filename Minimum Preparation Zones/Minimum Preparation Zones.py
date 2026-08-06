import sys

def main():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # We will separate the start times and end times into two independent lists
    starts = [0] * n
    ends = [0] * n
    
    idx = 1
    for i in range(n):
        starts[i] = int(input_data[idx])
        ends[i] = int(input_data[idx+1])
        idx += 2
        
    # Sort both lists independently
    starts.sort()
    ends.sort()
    
    zones = 0
    end_ptr = 0
    
    # Traverse through all the start times
    for start in starts:
        # If a team's start time is earlier than the earliest finishing time,
        # it means they overlap, and we absolutely need a new zone.
        if start < ends[end_ptr]:
            zones += 1
        else:
            # If a team's start time is >= the earliest finishing time,
            # a previous team has finished! We can reuse their zone.
            # We don't increase the zone count, but we advance the end pointer
            # to look at the next earliest finishing time.
            end_ptr += 1
            
    # The maximum number of simultaneous zones we needed is the answer
    print(zones)

if __name__ == "__main__":
    main()