graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

def DFS(graph):
    queue = [next(iter(graph))]
    visited = []

    while (len(queue) != 0):
        node = queue.pop()

        if node not in visited:
            visited.append(node) # Sommet visité
            print("noeud: ",node, end="")
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                print("\nVoisin de ",node,": ",neighbour)
                queue.append(neighbour)
                
    return visited

# def DFSRecursive(node):
#     if node not in visited: 
#         visited.append(node) # Sommet visité
#         print("noeud: ",node, end="")
        
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 print("\nVoisin de ",node,": ",neighbour)
#                 DFS(neighbour) # parcours récursive 

# visited = []        
# DFS(next(iter(graph)))

        

print("\nListe du DFS:", DFS(graph))


