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
        
    n = int(input_data[0])
    if n == 0:
        return
        
    root = None
    
    # 1. Iteratively construct the Binary Search Tree
    for i in range(1, n + 1):
        val = int(input_data[i])
        
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
                # Value belongs in the right subtree
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
                else:
                    # Ignore duplicate artifact numbers
                    break
                    
    if root is None:
        return
        
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