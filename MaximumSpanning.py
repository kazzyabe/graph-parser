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
    ep = {}

    newNode = ["c","b", "a", "d", "e", "f"]
    for n in newNode:
        if not n in V:
            new_v = n
            break
    # print("newV = ",newV)
    adjacent = adjacentT(V,E)
    # print(adjacent)
    w = weight(E)
    for c in C:
        V.remove(c)
    
    print("(c,v)")
    for v in V:
        for c in C:
            if v in adjacent[c]:
                print(c,v)
                maxW = 0
                ep_tmp = None
                for c2 in C:
                    if maxW < w[(c2,v)]:
                        maxW = w[(c2,v)]
                        ep_tmp = c2
                E += [[new_v,v, maxW]]
                ep[(new_v,v)] = ep_tmp
                break
    
    print("(v,c)")
    for v in V:
        for c in C:
            if c in adjacent[v]:
                print(v,c)
                maxW = 0
                ep_tmp = None
                for c2 in C:
                    tmp = w[v,c2] - w[predecessor(c2, C, E),c2] + sumWeight(C,E)
                    if maxW < tmp:
                        maxW = tmp
                        ep_tmp = c2
                E += [[v,new_v,maxW]]
                ep[(v,new_v)] = ep_tmp
                break
                
    V += [new_v]
    return V,E, new_v,ep
                

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
        highest = None
        for e in E:
            if v == e[1] and e[0] in V:
                if highest == None:
                    highest = e[2]
                    tmp = e
                if highest < e[2]:
                    highest = e[2]
                    tmp = e
        M += [tmp]
    
    print("Current M ===========")
    print(M)
    c, cycles = detcycle(V, M)
    # if there are cycles
    if c:
        # continue
        print("Cycles ==================")
        print(cycles)
        newV, newE, new_v, ep = contraction(V,E,cycles[0])
        print("Adjacency after contraction")
        print(adjacentT(newV,newE))
        # print("newV: ",newV)
        # print("newE: ", newE)
        # print("ep: ", ep)

        print("Next maxspan call -----------------------")
        M = maxspan(newV, newE)
        # print(M)

        # adding j,v where j = ep[c,v]
        keepE = []
        for i in M:
            if i[0] == new_v:
                M += [[ep[i[0], i[1]],i[1], None]]
            elif i[1] == new_v:
                M += [[i[0],ep[i[0], i[1]], None]]
                keepE += [ep[i[0], i[1]]]
        
        # adding edges for the cycle,
        i = 0
        while i < len(cycles[0]):
            if i == len(cycles[0]) - 1:
                head = cycles[0][i]
                dep = cycles[0][0]
                if not dep in keepE:
                    M += [[head,dep,None]]
            i += 1
        
        # removing edges with contracted nodes
        M_tmp = []
        for e in M:
            if not new_v in e:
                M_tmp += [e]

        M = M_tmp

    # removing weights
    noWM = []
    for m in M:
        noWM.append((m[0],m[1]))
    return noWM

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