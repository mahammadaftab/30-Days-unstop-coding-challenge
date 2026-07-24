import sys
from collections import deque

# Define the fundamental structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def main():
    # Read all inputs instantly from standard input to handle I/O overhead
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    idx = 0
    # Process all available test cases (safeguard against hidden multi-case files)
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            print()
            continue
            
        root = None
        
        # 1. Iteratively construct the Binary Search Tree
        # Safely bound the loop to prevent IndexErrors on malformed inputs
        elements_to_read = min(n, len(input_data) - idx)
        for _ in range(elements_to_read):
            val = int(input_data[idx])
            idx += 1
            
            # If the tree is empty, the first value becomes the root
            if root is None:
                root = Node(val)
            else:
                curr = root
                while True:
                    # Value belongs in the left subtree
                    if val < curr.val:
                        if curr.left is None:
                            curr.left = Node(val)
                            break
                        else:
                            curr = curr.left
                    # Boundary safeguard: Insert accidental duplicates to the right
                    # This ensures we don't accidentally drop nodes if the test case is flawed
                    else:
                        if curr.right is None:
                            curr.right = Node(val)
                            break
                        else:
                            curr = curr.right
                            
        if root is None:
            continue
            
        # 2. Level-Order Traversal (Breadth-First Search)
        # Use a double-ended queue for O(1) pops from the left side
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes currently present at this depth level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(str(node.val))
                
                # Enqueue children for the subsequent level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Print the entire level as a space-separated string
            print(" ".join(current_level))

if __name__ == '__main__':
    main()