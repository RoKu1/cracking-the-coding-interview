from Trees_and_Graphs import Graph as GR

"""
4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). Ail of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error
"""
"""
In our solution first we will establish a graph of the projects using their dependancies as input and dependents as 
output. We will store the solved nodes in buildorder list

"""
ar = ['a', 'b', 'c', 'd', 'e', 'f']
depen = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]
# depen = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c'], ['c', 'f']]

graph = GR.GraphDirected(depen)

buildorder = []
dependents = dict()
toprocess = []


for pair in depen:
    if dependents.get(pair[1]):
        dependents[pair[1]].append(pair[0])
    else:
        dependents[pair[1]] = [pair[0]]


for proj in ar:
    if not dependents.get(proj):
        toprocess.append(proj)


for x in toprocess:
    if x in graph.maper.keys():
        for y in graph.maper[x].neighbours:
            dependents[y.name].remove(x)
            if not dependents[y.name]:
                toprocess.append(y.name)
    buildorder.append(x)


if len(buildorder) == len(ar):
    print("Build Order is -->" + str(buildorder))
else:
    raise RuntimeError("No Valid Build order exist\n")


