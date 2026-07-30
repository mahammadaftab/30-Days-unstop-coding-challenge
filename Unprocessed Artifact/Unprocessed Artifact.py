import sys

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    
    unprocessed_artifact_id = 0
    
    # XOR all the registration IDs together.
    # Duplicate pairs will cancel out to 0.
    # The unique ID will remain.
    for i in range(1, n + 1):
        unprocessed_artifact_id ^= int(input_data[i])
        
    # Print the ID of the artifact that appears only once
    print(unprocessed_artifact_id)

if __name__ == "__main__":
    main()