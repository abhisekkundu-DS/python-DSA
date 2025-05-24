def add_node(v1):
    if v1 in Graph:
        print("this node already present ")
    else:
        Graph[v1] = []


def add_edge(v1,v2):
    if v1 not in Graph:
        print("this vertex not present in this Graph")
    elif v2 not in Graph:
        print("This vertex not in ")
    else:
        Graph[v1].append(v2)
        Graph[v2].append(v1)

#for undirected  weight graph

def add_edge(v1,v2,cost):
    if v1 not in Graph:
        print("this vertex not present in this Graph")
    elif v2 not in Graph:
        print("This vertex not in ")
    else:
        List1 = [v2,cost]
        List2 = [V1,cost]
        Graph[v1].append(List1)
        Graph[v2].append(List2)

Graph ={ }
add_node("A")
add_node("B")
add_edge("A","B")
print(Graph)
