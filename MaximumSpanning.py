def adjacentT(V, E):
    adjacent = {}
    for v in V:
        adjacent[v] = []
    
    # print(adjacent)
    for e in E:
        if e[0] in V and e[1] in V:
            # print(e[0])
            adjacent[e[0]] += [e[1]]

    return adjacent

def weight(E):
    w = {}
    for e in E:
        w[(e[0],e[1])] = e[2]
    return w

def sumWeight(C, E):
    w = weight(E)
    sumW = 0
    for c in C:
        for c2 in C:
            if (c,c2) in w:
                sumW += w[(c,c2)]
    return sumW

def predecessor(c, V, E):
    """
    return predecessor p in V of c
    c: current node

    """
    adjacent = adjacentT(V,E)
    for v in V:
        if c in adjacent[v]:
            return v

def cyclehelp(a, visited, adjacent):
    """
    detcycle helper
    recursive function which keeps looking for cycles
    a: current vertex
    visited: a list of already visited vertecies
    adjacent: a dictionary for adjacency

    return cycles if found
    otherwise return False
    """
    # print(a,visited,adjacent)
    if a in visited:
        # print("CYCLE: ", visited)
        # visited += [a]
        return visited
    elif adjacent[a] == []:
        # print("NO ADJACENT")
        return False
    else:
        visited += [a]
        res = []
        for n in adjacent[a]:
            tmp = cyclehelp(n, visited, adjacent)
            if tmp:
                res += [tmp]
        return res

def detcycle(V,E):
    """
    Detect cycles

    V: vertices[0...n]
    E: adges (i,j,w) where i is the head, j is the dependent, w is the weight

    return True, cycles if any cycles is found
    otherwise, return False
    """
    # creating adjacent list
    # adjacent = {}
    # for v in V[1:]:
    #     adjacent[v] = []

    # for e in E:
    #     print(e)
    #     adjacent[e[0]] += [e[1]]
    # print(adjacent)
    # print("function: ")
    # print(adjacent(V,E))
    adjacent = adjacentT(V,E)

    # Cycle detection by DFS
    res = []
    for v in V[1:]:
        for a in adjacent[v]:
            tmp = cyclehelp(a,[v], adjacent)
            if tmp:
                res += tmp
    if res:
        return True, res
    else:
        return False, []

def contraction(V,E,C):
    """
    Contraction procedure in Chi-Liu-Edmonds
    V: verticies
    E: edges with weights
    C: a cycle

    1.Excluding vertices in C from V
    2.Add a node c to V to represent the cycle
    3.For v in V-C, if (a, v) in E for a in C
        add (c,v) to E with weight max(y in C)weight(y,v)
    4.For v in V-C, if (v,a) in E for a in C
        add (v,c) to E with weight max(y in C)[W(v,y)-W(a(y),y) + W(C)]
        where a(y) is the predecessor of y in C
        W(C) is sum of all weights in C
    """
    adjacent = adjacentT(V,E)
    # print(adjacent)
    w = weight(E)
    for c in C:
        V.remove(c)
    
    for v in V:
        for c in C:
            if v in adjacent[c]:
                maxW = 0
                for c2 in C:
                    if maxW < w[(c,v)]:
                        maxW = w[(c,v)]
                E += [["c",v, maxW]]
                break
    
    for v in V:
        for c in C:
            if c in adjacent[v]:
                maxW = 0
                for c2 in C:
                    tmp = w[v,c2] - w[predecessor(c2, C, E),c2] + sumWeight(C,E)
                    if maxW < tmp:
                        maxW = tmp
                E += [[v,"c",maxW]]
                break

    V += ["c"]
    return V,E
                

def maxspan(V,E):
    """
    Find maximum spanning tree

    V: vertices[0...n]
    E: adges (i,j,w) where i is the head, j is the dependent, w is the weight
    """
    #1 find the highest scoring incomming edge for each word
    M = []
    for v in V[1:]:
        tmp = []
        highest = 0
        for e in E:
            if v == e[1]:
                if highest < e[2]:
                    highest = e[2]
                    tmp = e
        M += [tmp]

    c, cycles = detcycle(V, M)
    # if there are cycles
    if c:
        # continue
        print(cycles)
        newV, newE = contraction(V,E,cycles[0])
        print(adjacentT(newV,newE))
    return M

if __name__ == "__main__":
    V = [0,1,2,3]
    E = [
        [0,1,9],
        [0,2,10],
        [0,3,9],
        [1,2,20],
        [1,3,3],
        [2,1,30],
        [2,3,30],
        [3,1,11],
        [3,2,0]
    ]
    print(maxspan(V,E))