from Stacks_and_Queues import Stack_and_Queue as SQ


class Node:
    def __init__(self, data):
        self.name = data
        self.neighbours = []


class Graph:
    def __init__(self, arr):
        self.visited = []
        self.maper = dict()
        if not arr:
            return
        self.start = Node(arr[0][0])
        node = Node(arr[0][1])
        self.start.neighbours.append(node)
        node.neighbours.append(self.start)
        self.maper[str(self.start.name)] = self.start
        self.maper[str(node.name)] = node
        for pair in arr:
            # print("Pair -> " + pair[0] + " " + pair[1])
            if self.maper.get(pair[0]) and self.maper.get(pair[1]):
                # print("in IF")
                node1 = self.maper[pair[0]]
                node2 = self.maper[pair[1]]
                if node1 not in node2.neighbours:
                    node1.neighbours.append(node2)
                    node2.neighbours.append(node1)

            elif self.maper.get(pair[0]) or self.maper.get(pair[1]):
                # print("in ELIF 1")
                if self.maper.get(pair[0]):
                    # print("in ELIF 1 IF")
                    node1 = Node(pair[1])
                    node2 = self.maper[pair[0]]
                    if node1 not in node2.neighbours:
                        node2.neighbours.append(node1)
                        node1.neighbours.append(node2)
                    self.maper[node1.name] = node1

                else:
                    # print("in ELIF 1 ELSE")
                    node1 = Node(pair[0])
                    node2 = self.maper[pair[1]]
                    if node1 not in node2.neighbours:
                        node2.neighbours.append(node1)
                        node1.neighbours.append(node2)
                    self.maper[node1.name] = node1

            elif not self.maper.get(pair[0]) and not self.maper.get(pair[1]):
                # print("in ELIF 2")
                node1 = Node(pair[0])
                node2 = Node(pair[1])
                node1.neighbours.append(node2)
                node2.neighbours.append(node1)
                self.maper[str(node1.name)] = node1
                self.maper[str(node2.name)] = node2

    def __str__(self):
        reprs = ""
        for name in self.maper.keys():
            reprs = reprs + name + "--> "
            for child in self.maper[name].neighbours:
                reprs = reprs + child.name + ", "
            reprs = reprs + "\n"
        return reprs

    def DFS(self, start):
        self.visited.append(start)
        for child in start.neighbours:
            if child not in self.visited:
                self.DFS(child)

    def BFS(self):
        PriQ = SQ.Queue()
        PriQ.enque(self.start)
        while not PriQ.is_empty():
            currentnode = PriQ.deque()
            print(currentnode.name)
            for child in currentnode.neighbours:
                PriQ.enque(child)
        return


class GraphDirected:
    def __init__(self, arr):
        self.maper = dict()
        self.visited = []
        if not arr:
            return
        self.start = Node(arr[0][0])
        node = Node(arr[0][1])
        self.start.neighbours.append(node)
        self.maper[str(self.start.name)] = self.start
        self.maper[str(node.name)] = node
        for pair in arr:
            if self.maper.get(pair[0]) and self.maper.get(pair[1]):
                # print("in IF")
                node1 = self.maper[pair[0]]
                node2 = self.maper[pair[1]]
                if node2 not in node1.neighbours:
                    node1.neighbours.append(node2)

            elif self.maper.get(pair[0]) or self.maper.get(pair[1]):
                # print("in ELIF 1")
                if self.maper.get(pair[0]):
                    # print("in ELIF 1 IF")
                    node1 = Node(pair[1])
                    node2 = self.maper[pair[0]]
                    if node1 not in node2.neighbours:
                        node2.neighbours.append(node1)
                    self.maper[node1.name] = node1

                else:
                    # print("in ELIF 1 ELSE")
                    node1 = Node(pair[0])
                    node2 = self.maper[pair[1]]
                    if node2 not in node1.neighbours:
                        node1.neighbours.append(node2)
                    self.maper[node1.name] = node1

            elif not self.maper.get(pair[0]) and not self.maper.get(pair[1]):
                # print("in ELIF 2")
                node1 = Node(pair[0])
                node2 = Node(pair[1])
                if node2 not in node1.neighbours:
                    node1.neighbours.append(node2)
                self.maper[str(node1.name)] = node1
                self.maper[str(node2.name)] = node2

    def __str__(self):
        reprs = ""
        for name in self.maper.keys():
            reprs = reprs + name + "--> "
            for child in self.maper[name].neighbours:
                reprs = reprs + child.name + ", "
            reprs = reprs + "\n"
        return reprs

    def DFS(self, start):
        self.visited.append(start)
        for child in start.neighbours:
            if child not in self.visited:
                self.DFS(child)

    def BFS(self):
        self.visited.clear()
        PriQ = SQ.Queue()
        PriQ.enque(self.start)
        while not PriQ.is_empty():
            currentnode = PriQ.deque()
            print(currentnode.name, end=" ")
            self.visited.append(currentnode)
            for child in currentnode.neighbours:
                '''
                 We need to ensure that the node that we put in queue is NOT visited and also not Present in Queue
                '''
                if child not in self.visited and child not in PriQ.items:
                    # print(child.name)
                    PriQ.enque(child)
        return
