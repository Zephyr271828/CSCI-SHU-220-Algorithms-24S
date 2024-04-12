from math import floor

class Item:

    def __init__(self, w, v):
        self.w = w
        self.v = v

def KNAPSACK(m, W, I):
    # I is a list of (w, v)'s
    I = sorted(I, key=lambda x : x.v / x.w)
    w_max = max([item.w for item in I])
    DP = [[0 for w in range(w_max ** 2)] for idx in range(m + 1)] 
    # m+1 is set to handle boundary cases
    for idx in range(m - 1, 0, -1):
        for w in range(w_max ** 2 + 1):
            if w >= I[idx].w:
                DP[idx][w] = max(I[idx].v + DP[idx][w - I[idx].w], DP[idx + 1][w])
            else:
                DP[idx][w] = DP[idx + 1][w]
    ans = max([DP[1][w] + floor((W - w) / I[0].w) * I[0].v])
    return ans

class node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, other):
        if other not in self.neighbors:
            self.neighbors.append(other)
            other.neighbors.append(self)

def COUNT(G, s):

    cnt = {}
    queue = [s]
    while queue != []:
        L = len(queue)
        print(L)
        for u in queue[:L]: 
            cnt[u] = cnt.get(u, 0) + 1
            print(u.neighbors)
            for v in u.neighbors:
                if v not in cnt.keys():
                    queue.append(v)
        queue = queue[L:]

    L = [(item[0], item[1]) for item in cnt.items()]
    return L



if __name__ == '__main__':
    s = node('s')
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')

    a.add_neighbor(b)
    b.add_neighbor(c)
    c.add_neighbor(d)
    a.add_neighbor(d)
    s.add_neighbor(a)
    c.add_neighbor(e)

    #res = COUNT(None, s)
    #print(res)