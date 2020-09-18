from Trees_and_Graphs import Graph as GP

"""
4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
"""
We will traverse the garpgh from given node using DFS and if we find the end node in visited we will say that
the route is available 
"""


def checkifroute(g, pair):
    g.DFS(g.maper[pair[0]])
    if g.maper[pair[1]] in g.visited:
        print("Route is Possible\n")
    else:
        print("Route is not Posible\n")


ardire = [['0', '1'], ['0', '4'], ['0', '5'], ['1', '3'], ['1', '4'], ['2', '1'], ['3', '2'], ['3', '4']]
g = GP.GraphDirected(ardire)
pair = ['0', '5']  # pair of start and end node
checkifroute(g, pair)
