# Graph needs MIN 3 classes


# Adjacency List
class GraphList:
    def __init__(self, V):
        # Array
        self.vertices = [None] * len(V)

        # Initiate a Vertex object for each item in self.vertices
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string += "Vertex " + str(vertex) + "\n"
        return return_string

    def bfs(self, source):
        """
            Function for BFS, starting from source
            Basic BFS (Assignment should be modified)
        :param source:
        :return:
        """
        return_bfs = []
        # Implement our own queue; discovered is a queue, FIFO
        # discovered = Queue()
        discovered = [source]
        while len(discovered) > 0:
            # Still have vertex that has not been discovered
            # Serve from queue; pop(0) same as serve
            # v = discovered.serve()
            u = discovered.pop(0)
            u.visited = True
            return_bfs.append(u)
            for edge in u.edges:
                # look at the neighbor
                v = edge.v
                # Only add if not discovered
                if v.discovered is False:
                    discovered.append(v)
                    v.discovered = True     # discovered v, adding it to queue

        # NOT SHOWN: Adding edges and vertices to graph (Implement ourselves)
        # NOT COMPLETED
        return return_bfs

    def dfs(self, source):
        """
            Function for DFS, starting from source
            Basic DFS (Assignment should be modified)
        :param source:
        :return:
        """
        return_dfs = []
        # Implement our own stack; discovered is a stack, LIFO
        # discovered = Stack()
        discovered = [source]
        while len(discovered) > 0:

            # Still have vertex that has not been discovered
            u = discovered.pop()
            u.visited = True
            return_dfs.append(u)

            for edge in u.edges:
                # look at the neighbor
                v = edge.v
                # Only add if not discovered
                if v.discovered is False:
                    discovered.append(v)        # change to push; append = push
                    v.discovered = True     # discovered v, adding it to queue

        # NOT SHOWN: Adding edges and vertices to graph (Implement ourselves)
        # NOT COMPLETED
        return return_dfs

    def dfs_recursive(self, current_vertex):
        current_vertex.visited = True
        for next_vertex in current_vertex.adjacent:
            if not next_vertex.visited:
                self.dfs_recursive(neaxt_vertex)

    def bfs_distance(self, source):
        """
            Function for BFS distance, starting from source
        """
        # Implement our own queue; discovered is a queue, FIFO
        # discovered = Queue()
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            # Still have vertex that has not been discovered
            # Serve from queue; pop(0) same as serve
            # v = discovered.serve()
            u = discovered.pop(0)
            u.visited = True
            for edge in u.edges:
                # look at the neighbor
                v = edge.v
                # Only add if not discovered
                if v.discovered is False:
                    discovered.append(v)
                    v.discovered = True     # discovered v, adding it to queue
                    v.distance = u.distance + 1
                    v.previous = u          # backtracking
                    # implement backtracking!

    def bfs_distance(self, source):
        """
            Function for BFS distance, starting from source
        """
        # Implement our own queue; discovered is a queue, FIFO
        # discovered = Queue()
        discovered = [source]
        while len(discovered) > 0:
            # Still have vertex that has not been discovered
            # Serve from queue; pop(0) same as serve
            # v = discovered.serve()
            u = discovered.pop(0)
            u.visited = True
            for edge in u.edges:
                # look at the neighbor
                v = edge.v
                # Only add if not discovered
                if v.discovered is False:
                    discovered.append(v)
                    v.discovered = True     # discovered v, adding it to queue
                    v.distance = u.distance + 1
                    v.previous = u          # backtracking
                    # implement backtracking!

    def dijkstra(self, source, destination, total):
        """
            Function for Dijkstra algorithm
        """
        # Dijkstra: Priority queue = min heap
        discovered = MinHeap(total)
        source.distance = 0

        # append(key, data)
        discovered.add(source.distance, source)        # append is different bc we are using MinHeap()

        while len(discovered) > 0:
            # Still have vertex that has not been discovered
            # Serve from queue; pop(0) same as serve [implement after we have MinHeap()]
            u = discovered.get_min()      # get smallest child at root
            u.visited = True        # visited u, distance is finalised

            # Terminate early when we reached destination vertex
            if u == destination:
                return

            # Perform edge relaxation on all adjacent vertices
            for edge in u.edges:
                v = edge.v
                # Only add if not discovered
                if v.discovered is False:   # distance is still \inf (neighbour not discovered yet)
                    # discovered.add(v)
                    v.discovered = True     # discovered v, adding it to queue
                    v.distance = u.distance + edge.w
                    v.previous = u          # backtracking (implemented using previous)
                    discovered.add(v.distance, v)    # add to MinHeap() with updated distance

                # in heap but distance not yet finalised
                elif not v.visited:
                    # if we find a shorter route, change it
                    if v.distance > u.distance + edge.w:
                        # update distance
                        v.distance = u.distance + edge.w
                        v.previous = u      # W8 Slide 268
                        # update Heap
                        # code this!!
                        # discovered.rise(v.distance)

                        # update vertex v in heap, with distance v.distance (smaller)
                        discovered.update(v.distance, v)        # perform up-heap


# Adjacency Matrix
class GraphMatrix:
    def __init__(self, V):
        self.matrix = [None] * len(V)

        # Create matrix
        for i in range(len(V)):
            self.matrix[i] = [None] * len(V)

        # Implement: add into the matrix
        # We've only created matrix but not yet updated it

    def __str__(self):
        return_string = ""
        for vertex in self.matrix:
            return_string += "Vertex " + str(vertex) + "\n"
        return return_string


class Vertex:
    def __init__(self, id):
        # List
        self.edges = []
        self.id = id

        # For traversal of BFS
        self.discovered = False
        self.visited = False

        # No need to maintain the list since we already have flags
        # Unless we need the output of BFS

        # Distance
        self.distance = 0


    def added_to_queue(self):
        # Update when added to queue
        self.discovered = True

    def visit_node(self):
        self.visited = True

    def __str__(self):
        return_string = str(self.id)
        return return_string


class Edge:
    def __init__(self, u, v, w):
        # vertex: u and v
        # weight: w
        self.u = u
        self.v = v
        self.w = w


class MinHeap:
    def __init__(self, size: int):
        self.array = [None] * (size + 1)
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def is_full(self) -> bool:
        return self.count + 1 == len(self.array)

    def add(self, key, value) -> bool:
        # +1 bc leave one spot for index 0
        has_space = not self.is_full()
        if has_space:
            self.array[self.count + 1] = (key, value)  # skip 0 index
        else:
            raise ValueError("Heap is full")

        # do resizing here
        self.count += 1
        self.rise(self.count)  # rising swap to check if order is broken
        return has_space

    def update(self, new_dis, v):
        """
            Function that updates the distance of vertex in MinHeap

        :param new_dis:     (int)   new updated distance
        :param v:           (int)   vertex to be updated

        :return:    None

        :time complexity:   Best = Worse Case: O(log V),
                            where V is the number of items currently in MinHeap
        """

        # get index position of vertex in MinHeap
        index = v.heap_index
        old_dis = self.array[index][0]
        self.array[index] = (new_dis, v)

        # perform sink if new_dis is greater: O(log V)
        if old_dis < new_dis:
            self.sink(index)
        # perform rise if new_dis is lesser: O(log V)
        elif old_dis > new_dis:
            self.rise(index)

    def rise(self, node):
        # rise when child < parent
        # parent = node // 2
        # node is NOT root          (key, value) -> check the key
        # while child < parent
        while node > 1 and self.array[node][0] < self.array[node // 2][0]:
            self.swap(node, node // 2)
            node = node // 2

    def get_min(self):
        # precondition: check if heap is empty
        if self.count == 0:
            raise ValueError("Heap is empty")
        ret = self.array[1]  # access root at index 1
        self.swap(1, self.count)  # swap max and last element
        self.count -= 1
        self.sink(1)  # sink swap the swapped element at index 1
        return ret

    def sink(self, node):
        # stop sinking if node does not have child
        while node * 2 <= self.count:
            # sink to the larger child (left / right)
            chosen_child = self._get_smallest_child(node)
            if self.array[node] < self.array[chosen_child]:
                break  # already in right order, no need to continue sinking
            self.swap(node, chosen_child)
            node = chosen_child  # check again the node that sinked

    def _get_smallest_child(self, node):
        # check if left child < right child
        # doesnt matter which to return if child is equal
        # left child = count -> no right child
        if node * 2 == self.count or self.array[node * 2] < self.array[node * 2 + 1]:
            return node * 2  # ret left
        return node * 2 + 1  # ret right

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __str__(self) -> str:
        res = ""
        for i in range(1, self.count + 1):
            res += str(self.array[i]) + " "
        return res


# Create a graph with 5 vertices
if __name__ == "__main__":
    vertices = [0, 1, 2, 3, 4]
    my_graph = GraphList(vertices)
    print(my_graph)
    # my_graph_matrix = GraphMatrix(vertices)
    # print(my_graph_matrix)

