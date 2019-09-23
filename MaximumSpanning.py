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
        visited += [a]
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
    adjacent = {}
    for v in V[1:]:
        adjacent[v] = []

    for e in E:
        adjacent[e[0]] += [e[1]]
    # print(adjacent)

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
        print(c,cycles)
    return M

if __name__ == "__main__":
    V = [0,1,2,3]
    E = [
        [0,1,9],
        [0,2,10],
        [0,3,9],
        [1,2,20],
        [1,2,3],
        [2,1,30],
        [2,3,30],
        [3,1,11],
        [3,2,0]
    ]
    print(maxspan(V,E))