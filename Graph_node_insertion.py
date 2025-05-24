def add_node(v):
    if v in nodes :
        global node_count
        print(v,"is alredy present in the graph")
    else :
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for r in range(node_count):
            temp.append(0)
        graph.append(temp)



nodes = []
graph = []
node_count = 0

print("Befor adding the graph ")
print(nodes)
print(graph)

add_node("B")
print("After adding nodes ")
print(nodes)
print(graph)

add_node("B")
print("After adding nodes ")
print(nodes)
print(graph)

add_node("C")
print("After adding nodes ")
print(nodes)
print(graph)

add_node("D")
print("After adding nodes ")
print(nodes)
print(graph)

