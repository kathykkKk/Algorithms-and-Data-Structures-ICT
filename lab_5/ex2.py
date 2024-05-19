from collections import deque


def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None


# Пример ориентированного графа с весами на дугах
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

start = 'A'
end = 'E'

shortest_path = bfs_shortest_path(graph, start, end)

if shortest_path:
    print(f"Кратчайший путь из вершины {start} в вершину {end}:", shortest_path)
else:
    print(f"Пути из вершины {start} в вершину {end} не существует.")




