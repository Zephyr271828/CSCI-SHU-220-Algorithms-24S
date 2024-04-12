class Node:

    def __init__(self, val):
        self.val = val
        self.neighbors = [[], []]
        # 0 for in, 1 for out

    def add_neighbor(self, other):
        self.neighbors[1].append(other)
        other.neighbors[0].append(self)
        # add a edge from self to other

def SCC(G, s):
    (V, E) = G
    for (u, v) in E:
        u.add_neighbor(v)
    
    res = [set(), set()]
    # res[0] for all the nodes can be reached from s;
    # res[1] for all the nodes that can reach s
    def DFS(u, direction = 0):
    # direction = 0 for in-neighbors, 1 for out-neighbors
        res[direction].add(u)
        for v in u.neighbors[direction]:
            if v not in res[direction]:
                DFS(v, direction = direction)
    
    DFS(s, 0)
    DFS(s, 1)
    ans = res[0].intersection(res[1])
    ans.remove(s)
    return ans

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')

    V = [a, b, c]
    E = [(a, b), (a, c), (c, a), (b, a)]
    G = (V, E)

    res = SCC(G, a)
    print([each.val for each in res])

    
