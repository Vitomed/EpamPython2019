"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""

from collections import deque

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}


class Graph:
    """The class encapsulates the bfs method in itself,
    which performs a breadth-first traversal

    The implementation below uses the deque data-structure
    to build-up and return a set of vertices that are accessible
    within the subjects connected component.
    """

    def __init__(self):
        self.storage = deque()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.storage:
            raise StopIteration
        return self.storage.popleft()

    def bfs(self, bfs_graph, name):
        self.storage += name
        search_deque = deque()
        search_deque += bfs_graph[name]
        while search_deque:
            pop_element = search_deque.popleft()
            if pop_element not in self.storage:
                search_deque += bfs_graph[pop_element]
                self.storage += pop_element


name = "A"
bfs_traversal = Graph()
bfs_traversal.bfs(bfs_graph=E, name=name)
for i in bfs_traversal:
    print(i)






