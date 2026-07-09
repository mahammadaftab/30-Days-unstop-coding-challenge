from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
queue = deque([(1, 0)])  # (city, distance)
visited[1] = True

max_distance = 0

while queue:
    node, dist = queue.popleft()
    max_distance = max(max_distance, dist)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append((neighbor, dist + 1))

print(max_distance)