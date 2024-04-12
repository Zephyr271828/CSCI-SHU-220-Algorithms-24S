class Vertex:

    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, other):
        self.neighbors.append(other)

def GAME(n):
    V = [Vertex(i) for i in range(n)]
    # Type A edge
    for i in range(n - 1):
        V[i].add_neighbor(V[i + 1])
    # Type B edge
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                V[i].add_neighbor(V[j])
    # Type C edge
    for i in range(2, n):
        if i ** 2 % n != i:
            V[i].add_neighbor(V[i ** 2 % n])

    for i in range(n):
        print('vertex: {} neighbors: {}'.format(i, [each.val for each in V[i].neighbors]))

    # BFS
    visited = [0 for i in range(n)]
    prev = [-1 for i in range(n)]
    queue = [2]
    while queue != []:
        head = queue[0]
        queue = queue[1:]
        visited[head] = 1
        if head == 1:
            break
        for n in V[head].neighbors:
            if not visited[n.val]:
                queue.append(n.val)
                if prev[n.val] == -1:
                    prev[n.val] = head 

    sol = [1]
    while sol[-1] != -1:
        sol.append(prev[sol[-1]])
    return sol[-2::-1]

if __name__ == '__main__':

    res = GAME(91)
    print(res)

