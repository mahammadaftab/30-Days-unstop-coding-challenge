import sys

# Prevent recursion depth issues for deep segments
sys.setrecursionlimit(300000)

def main():
    # Read entire input block rapidly
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    q = int(input_data[1])
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input_data[1 + i])
        
    # We use flat arrays to represent our Segment Tree nodes instead of objects
    # to significantly speed up memory allocation and property lookups in Python.
    tree_sum = [0] * (4 * n + 5)
    tree_max1 = [0] * (4 * n + 5)
    tree_max2 = [0] * (4 * n + 5)
    tree_max_cnt = [0] * (4 * n + 5)
    
    def push_up(node):
        left = 2 * node
        right = 2 * node + 1
        tree_sum[node] = tree_sum[left] + tree_sum[right]
        
        l_m1 = tree_max1[left]
        r_m1 = tree_max1[right]
        
        # Merge highest values and second-highest values
        if l_m1 == r_m1:
            tree_max1[node] = l_m1
            # Avoid the max() function for speed
            tree_max2[node] = tree_max2[left] if tree_max2[left] > tree_max2[right] else tree_max2[right]
            tree_max_cnt[node] = tree_max_cnt[left] + tree_max_cnt[right]
        elif l_m1 > r_m1:
            tree_max1[node] = l_m1
            tree_max2[node] = tree_max2[left] if tree_max2[left] > r_m1 else r_m1
            tree_max_cnt[node] = tree_max_cnt[left]
        else:
            tree_max1[node] = r_m1
            tree_max2[node] = l_m1 if l_m1 > tree_max2[right] else tree_max2[right]
            tree_max_cnt[node] = tree_max_cnt[right]

    def apply(node, v):
        # Ignore ceilings that are higher than our peak brightness
        if tree_max1[node] <= v:
            return
        # Lower the overall sum by pulling down all the peaks
        tree_sum[node] -= tree_max_cnt[node] * (tree_max1[node] - v)
        tree_max1[node] = v

    def push_down(node):
        apply(2 * node, tree_max1[node])
        apply(2 * node + 1, tree_max1[node])

    def build(node, l, r):
        if l == r:
            val = a[l]
            tree_sum[node] = val
            tree_max1[node] = val
            tree_max2[node] = -1
            tree_max_cnt[node] = 1
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        push_up(node)

    def update(node, l, r, ql, qr, v):
        # Stop early if the ceiling won't touch anything in this range
        if tree_max1[node] <= v:
            return
            
        # If the ceiling only affects our absolute highest peaks, apply lazily
        if ql <= l and r <= qr and tree_max2[node] < v:
            apply(node, v)
            return
            
        # Recursive deep dive if the ceiling cuts into our second-highest peaks
        push_down(node)
        mid = (l + r) // 2
        if ql <= mid:
            update(2 * node, l, mid, ql, qr, v)
        if qr > mid:
            update(2 * node + 1, mid + 1, r, ql, qr, v)
        push_up(node)

    def query(node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return tree_sum[node]
            
        push_down(node)
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += query(2 * node, l, mid, ql, qr)
        if qr > mid:
            res += query(2 * node + 1, mid + 1, r, ql, qr)
        return res

    build(1, 1, n)
    
    idx = n + 2
    out = []
    
    for _ in range(q):
        type = int(input_data[idx])
        if type == 1:
            ql = int(input_data[idx+1])
            qr = int(input_data[idx+2])
            v = int(input_data[idx+3])
            update(1, 1, n, ql, qr, v)
            idx += 4
        else:
            ql = int(input_data[idx+1])
            qr = int(input_data[idx+2])
            out.append(str(query(1, 1, n, ql, qr)))
            idx += 3
            
    # Print output all at once to save I/O time
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()