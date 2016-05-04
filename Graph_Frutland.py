import networkx as nx
import matplotlib.pyplot as plt
import random as rnd


def show(graph, path=[]):
    pos = nx.shell_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=500)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), width=1)
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family='serif')
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i
                                                 in range(len(path) - 1)], width=6)
    plt.axis('off')
    plt.show()


def read_G(fname):
    G = nx.Graph()
    with open(fname) as f:
        for line in f:
            if line:
                a, b, w = line.split()
                G.add_edge(a, b, weight=rnd.randint(1, 30))
    return G
    


def bfs(G, start, return_used = False):
    queue = [start]
    res = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    used = {start}
    while queue:
        curr = queue.pop(0)
        for n in G[curr]:
            if n not in used:
                used.add(n)
                res.add_edge(curr, n, weight=G[curr][n]['weight'])
                queue.append(n)
    return res if not return_used else (res, used)
    
def dfs(G, start):
    stack = [start]
    res = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    used = {start}
    while stack:
        curr = stack.pop()
        for n in G[curr]:
            if n not in used:
                used.add(n)
                res.add_edge(curr, n, weight=G[curr][n]['weight'])
                stack.append(n)
    return res


def connectivity(G):
    g = nx.to_dict_of_dicts(G)
    used = set()
    res = set()
    for curr in g:
        if curr not in used:
            comp, u = bfs(G, curr, return_used=True)
            used |= u
            res.add(comp)
    return res
    


def Dijkstra(G, root):
    g = nx.to_dict_of_dicts(G)
    D = {n: (float('inf'),None) for n in g}
    D[root] = (0, None)
    used =set()
    while len(used) < len(g):
        mn = min((i for i in g.items() if i[0] not in used), key=lambda x: D[x[0]][0])
        for n in mn[1]:
            new = D[mn[0]][0] + mn[1][n]['weight']
            if new < D[n][0]:
                D[n] = (new, mn[0])
        used.add(mn[0])
    return D

def find_way(G, From, To):
    D = Dijkstra(G, From)
    t = To
    path=[]
    while t:
        path.append(t)
        t = D[t][1]
    return path[::-1]
    

gr = read_G("input.txt")

"""
show(gr, ['1', '3', '5'])
"""

"""
show(bfs(gr, 1))
"""

"""
show(dfs(gr, 1))
"""


"""
C = connectivity(gr)
for t in C:
    nx.draw_shell(t) 
plt.show() 
"""

"""
djstr = Dijkstra(gr, '1')
way = find_way(gr, '2', '6')
print(way)
"""
