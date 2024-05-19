import pickle


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        current_node = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    return distances


# пример
with open('spb_streets_voc.pkl', 'rb') as f:
    graph = pickle.load(f)
start_node = 'Ломоносова'
result = dijkstra(graph, start_node)
for i in result:
    if i in ['Садовая', 'Восстания', 'Гастелло', 'Чайковского']:
        print(f"{i} --> {result[i]}")
