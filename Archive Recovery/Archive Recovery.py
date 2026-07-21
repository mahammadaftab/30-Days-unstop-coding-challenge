import sys

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
            
        # 2. Iterative Post-Order Traversal
        # We traverse the tree in Root -> Right -> Left order using a stack, 
        # and reverse the resulting list at the end. This is faster than recursion
        # and strictly prevents deep-tree Stack Overflow errors.
        stack = [root]
        post_order_result = []
        
        while stack:
            node = stack.pop()
            post_order_result.append(str(node.val))
            
            # We push left first, so right is popped first in the next iteration
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        # Reverse the array to achieve Left -> Right -> Root (Standard Post-Order)
        print(" ".join(post_order_result[::-1]))

if __name__ == '__main__':
    main()