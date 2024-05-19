from collections import deque


def make_table(mas):
    n = len(mas)
    table = {}
    for i in range(n):
        for j in range(n):
            if mas[i][j] == 0:
                name = f"({i}, {j})"
                table[name] = []
                if j + 1 < n:
                    if mas[i][j + 1] == 0:
                        table[name].append(f"({i}, {j + 1})")
                if i - 1 >= 0:
                    if mas[i - 1][j] == 0:
                        table[name].append(f"({i - 1}, {j})")
                if i + 1 < n:
                    if mas[i + 1][j] == 0:
                        table[name].append(f"({i + 1}, {j})")
    return table


def bfs(graph, start, end):
    queue = deque()
    visited = set()
    queue.append([start])
    visited.add(start)
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.add(neighbor)
    return None


def shortest_path(mas, start):
    ends = []
    n = len(mas)
    for i in range(n):
        if mas[i][n - 1] == 0:
            ends.append(f"({i}, {n - 1})")
    path, arr = None, None
    if ends:
        graph = make_table(mas)
        min_len = n * n
        for end in ends:
            arr = bfs(graph, start, end)
            if len(arr) < min_len and arr:
                min_len = len(arr)
                path = arr
    return path


mas = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


start = '(7, 0)'
cnt = 1
path = shortest_path(mas, start)
if path:
    print("Кратчайший путь выхода из лабиринта:")
    for i in path:
        if cnt != len(path):
            print(i, ' --> ', end=' ') if cnt % 5 != 0 else print(i, ' --> ')
        else:
            print(i)
        cnt += 1
else:
    print("Выхода из лабиринта нет!")
