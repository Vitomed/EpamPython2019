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

    def __init__(self, bfs_graph, name):
        self.storage = deque(name)
        self.graph = bfs_graph
        # self.bfs(name, self.graph)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.storage:
            raise StopIteration
        return self.storage.popleft()

    # def bfs(self, name, bfs_graph):
    #     search_deque = deque()
    #     search_deque += bfs_graph[name]
    #     while search_deque:
    #         pop_element = search_deque.popleft()
    #         if pop_element not in self.storage:
    #             search_deque += bfs_graph[pop_element]
    #             self.storage += pop_element

    def bfs(self, name):
        search_deque = deque()
        search_deque += self.graph[name]
        while search_deque:
            pop_element = search_deque.popleft()
            if pop_element not in self.storage:
                search_deque += self.graph[pop_element]
                self.storage += pop_element


name = "A"
bfs_traversal = Graph(bfs_graph=E, name=name)
# bfs_graph = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
bfs_traversal.bfs(name)
for i in bfs_traversal:
    print(i)






