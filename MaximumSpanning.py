import sys
# sys.stderr = open("maxspan.log", "w")

def adjacentT(V, E):
    adjacent = {}
    for v in V:
        adjacent[v] = []
    
    # # print(adjacent)
    for e in E:
        if e[0] in V and e[1] in V:
            # # print(e[0])
            adjacent[e[0]] += [e[1]]
    
    for k in adjacent.keys():
        adjacent[k] = sorted(adjacent[k])

    return adjacent
# def adjacentT(V, E):
#     adjacent = {}
#     for v in V:
#         adjacent[v] = []
    
#     # # print(adjacent)
#     for e in E:
#         if e[0] in V and e[1] in V:
#             # # print(e[0])
#             adjacent[e[0]] += [e[1]]

#     return adjacent

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
    # # print(a,visited,adjacent)
    if a in visited:
        # # print("CYCLE: ", visited)
        # visited += [a]
        return visited
    elif adjacent[a] == []:
        # # print("NO ADJACENT")
        return False
    else:
        visited += [a]
        res = []
        for n in adjacent[a]:
            tmp = cyclehelp(n, visited, adjacent)
            if tmp:
                return tmp
                # print("tmp in help =================\n", tmp,  file=sys.stderr)
        # return res

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
    res = None
    for v in V[1:]:
        for a in adjacent[v]:
            res = cyclehelp(a,[v], adjacent)
            # if tmp:
            #     res += tmp
            #     print("tmp in main ====================\n", tmp, file=sys.stderr)
            #     print("res in main ====================\n", res, file=sys.stderr)
            if res:
                return True, res
    if not res:
        return False, []

# def cyclehelp(a, visited, adjacent):
#     """
#     detcycle helper
#     recursive function which keeps looking for cycles
#     a: current vertex
#     visited: a list of already visited vertecies
#     adjacent: a dictionary for adjacency

#     return cycles if found
#     otherwise return False
#     """
#     # # print(a,visited,adjacent)
#     if a in visited:
#         # # print("CYCLE: ", visited)
#         # visited += [a]
#         return visited
#     elif adjacent[a] == []:
#         # # print("NO ADJACENT")
#         return False
#     else:
#         visited += [a]
#         res = []
#         for n in adjacent[a]:
#             tmp = cyclehelp(n, visited, adjacent)
#             if tmp:
#                 res += [tmp]
#                 print("tmp in help =================\n", tmp,  file=sys.stderr)
#         return res

# def detcycle(V,E):
#     """
#     Detect cycles

#     V: vertices[0...n]
#     E: adges (i,j,w) where i is the head, j is the dependent, w is the weight

#     return True, cycles if any cycles is found
#     otherwise, return False
#     """
#     adjacent = adjacentT(V,E)

#     # Cycle detection by DFS
#     res = []
#     for v in V[1:]:
#         for a in adjacent[v]:
#             tmp = cyclehelp(a,[v], adjacent)
#             if tmp:
#                 res += tmp
#                 print("tmp in main ====================\n", tmp, file=sys.stderr)
#                 print("res in main ====================\n", res, file=sys.stderr)
#     if res:
#         return True, res
#     else:
#         return False, []



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
    # print("Contraction -------------------------", file=sys.stderr)
    ep = {}

    # newNode = ["c","b", "a", "d", "e", "f"]
    # for n in newNode:
    #     # print(n)
    #     if not n in V:
    #         new_v = n
    #         break
    new_v = V[-1] + 1
    # print("new_v = ",new_v)
    adjacent = adjacentT(V,E)
    # # print(adjacent)
    w = weight(E)
    print("V ================\n", V, file=sys.stderr)
    print("E ================\n", E, file=sys.stderr)
    print("C ================\n", C, file=sys.stderr)
    for c in C:
        print(c, file=sys.stderr)
        V.remove(c)
    
    # print("(c,v)", file=sys.stderr)
    for v in V:
        for c in C:
            if v in adjacent[c]:
                # print(c,v, file=sys.stderr)
                maxW = None
                ep_tmp = None
                for c2 in C:
                    if maxW == None or maxW < w[(c2,v)]:
                        maxW = w[(c2,v)]
                        ep_tmp = c2
                E += [[new_v,v, maxW]]
                ep[(new_v,v)] = ep_tmp
                break
    
    # print("(v,c)", file=sys.stderr)
    for v in V:
        for c in C:
            if c in adjacent[v]:
                # print(v,c, file=sys.stderr)
                maxW = None
                ep_tmp = None
                for c2 in C:
                    tmp = w[v,c2] - w[predecessor(c2, C, E),c2] + sumWeight(C,E)
                    if maxW == None or maxW < tmp:
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
    
    # print("Current M ===========", file=sys.stderr)
    # print(M, file=sys.stderr)
    c, cycle = detcycle(V, M)
    # if there are cycles
    if c:
        # continue
        print("Cycle ==================", file=sys.stderr)
        print(cycle, file=sys.stderr)
        newV, newE, new_v, ep = contraction(V,E,cycle)
        # print("Adjacency after contraction", file=sys.stderr)
        # print(adjacentT(newV,newE), file=sys.stderr)
        print("======================Contraction=====================", file=sys.stderr)
        print("Cycle ==================", cycle, file=sys.stderr)
        print("newV =========================\n",newV, file=sys.stderr)
        print("newE ===========================\n", newE, file=sys.stderr)
        # print("ep =============================\n", ep, file=sys.stderr)

        # print("================ Next maxspan call =====================", file=sys.stderr)
        M = maxspan(newV, newE)
        # print("M ================================\n", M, file=sys.stderr)

        #  For the arc (wi,wc) ∈ A where ep(wi,wc) = wj ,
        # # identify the arc (wk,wj ) ∈ C for some wk
        wkwj = []
        # retrive adjacency in cycles
        # AND adding edges for the cycle,
        ad = {}
        i = 0
        while i < len(cycle):
            if i == len(cycle) - 1:
                head = cycle[i]
                dep = cycle[0]
            else:
                head = cycle[i]
                dep = cycle[i+1]
            M += [(head,dep)]
            ad[head] = [dep]
            i += 1
        # print("\n\n=========================== Post Processing =========================", file=sys.stderr)
        # print("ADJACENT ====================\n", ad, file=sys.stderr)
        # print("new_v ====================\n", new_v, file=sys.stderr)
        # print("M ====================\n", M, file=sys.stderr)
        for m in M:
            if m[1] == new_v:
                wj = ep[m]
                for wk in cycle:
                    if wj in ad[wk]:
                        wkwj.append((wk,wj))
        # print("wkwj ===================\n", wkwj, file=sys.stderr)

        # adding j,v where j = ep[c,v]
        keepE = []
        # print("ep ============\n",ep, file=sys.stderr)
        for i in M:
            if i[0] == new_v:
                e_tmp = (ep[i[0], i[1]],i[1])
                # print(e_tmp, file=sys.stderr)
                M += [e_tmp]
            elif i[1] == new_v:
                e_tmp = (i[0],ep[i[0], i[1]])
                # print(e_tmp, file=sys.stderr)
                M += [e_tmp]
                # keepE += [ep[i[0], i[1]]]
        
        # # adding edges for the cycle,
        # i = 0
        # while i < len(cycles[0]):
        #     if i == len(cycles[0]) - 1:
        #         head = cycles[0][i]
        #         dep = cycles[0][0]
        #         # if not dep in keepE:
        #     else:
        #         head = cycles[0][i]
        #         dep = cycles[0][i+1]
        #     M += [(head,dep)]
        #     i += 1
        
        # removing (wk, wj)
        for r in wkwj:
            M.remove(r)
        
        # removing edges with contracted nodes
        M_tmp = []
        for e in M:
            if not new_v in e:
                M_tmp += [e]

        M = M_tmp

        # print("======================Contraction=====================", file=sys.stderr)
        # print("Current V =========\n", V, file=sys.stderr)
        # print("Current M ===========", file=sys.stderr)
        # print(M, file=sys.stderr)
        # print("Cycles ==================", file=sys.stderr)
        # print(cycles, file=sys.stderr)
        # print("newV =========================\n",newV, file=sys.stderr)
        # print("ep =============================\n", ep, file=sys.stderr)

    # removing weights
    noWM = []
    for m in M:
        noWM.append((m[0],m[1]))
    # print("noWM =========================\n", noWM, file=sys.stderr)
    # print("======================END=====================", file=sys.stderr)
    return noWM

if __name__ == "__main__":
    # V = [0,1,2,3]
    # E = [
    #     [0,1,9],
    #     [0,2,10],
    #     [0,3,9],
    #     [1,2,20],
    #     [1,3,3],
    #     [2,1,30],
    #     [2,3,30],
    #     [3,1,11],
    #     [3,2,0]
    # ]
    # V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # E = [[0, 1, -19.0], [0, 2, -16.0], [0, 3, -16.0], [0, 4, -18.0], [0, 5, -14.0], [0, 6, -20.0], [0, 7, -17.0], [0, 8, -18.0], [0, 9, -14.0], [0, 10, -15.0], [0, 11, -18.0], [0, 12, -18.0], [0, 13, -16.0], [0, 14, -16.0], [0, 15, -17.0], [0, 16, -22.0], [0, 17, -20.0], [0, 18, -14.0], [0, 19, -18.0], [1, 2, -6.0], [1, 3, -6.0], [1, 4, -8.0], [1, 5, -4.0], [1, 6, -10.0], [1, 7, -7.0], [1, 8, -8.0], [1, 9, -4.0], [1, 10, -5.0], [1, 11, -8.0], [1, 12, -8.0], [1, 13, -6.0], [1, 14, -6.0], [1, 15, -7.0], [1, 16, -12.0], [1, 17, -10.0], [1, 18, -4.0], [1, 19, -8.0], [2, 3, -6.0], [2, 4, -8.0], [2, 5, -4.0], [2, 6, -10.0], [2, 7, -7.0], [2, 8, -8.0], [2, 9, -4.0], [2, 10, -5.0], [2, 11, -8.0], [2, 12, -8.0], [2, 13, -6.0], [2, 14, -6.0], [2, 15, -7.0], [2, 16, -12.0], [2, 17, -10.0], [2, 18, -4.0], [2, 19, -8.0], [2, 1, -9.0], [3, 4, -8.0], [3, 5, -4.0], [3, 6, -10.0], [3, 7, -7.0], [3, 8, -8.0], [3, 9, -4.0], [3, 10, -5.0], [3, 11, -8.0], [3, 12, -8.0], [3, 13, -6.0], [3, 14, -6.0], [3, 15, -7.0], [3, 16, -12.0], [3, 17, -10.0], [3, 18, -4.0], [3, 19, -8.0], [3, 1, -9.0], [3, 2, -6.0], [4, 5, -4.0], [4, 6, -10.0], [4, 7, -7.0], [4, 8, -8.0], [4, 9, -4.0], [4, 10, -5.0], [4, 11, -8.0], [4, 12, -8.0], [4, 13, -6.0], [4, 14, -6.0], [4, 15, -7.0], [4, 16, -12.0], [4, 17, -10.0], [4, 18, -4.0], [4, 19, -8.0], [4, 1, -9.0], [4, 2, -6.0], [4, 3, -6.0], [5, 6, -10.0], [5, 7, -7.0], [5, 8, -8.0], [5, 9, -4.0], [5, 10, -5.0], [5, 11, -8.0], [5, 12, -8.0], [5, 13, -6.0], [5, 14, -6.0], [5, 15, -7.0], [5, 16, -12.0], [5, 17, -10.0], [5, 18, -4.0], [5, 19, -8.0], [5, 1, -9.0], [5, 2, -6.0], [5, 3, -6.0], [5, 4, -8.0], [6, 7, -7.0], [6, 8, -8.0], [6, 9, -4.0], [6, 10, -5.0], [6, 11, -8.0], [6, 12, -8.0], [6, 13, -6.0], [6, 14, -6.0], [6, 15, -7.0], [6, 16, -12.0], [6, 17, -10.0], [6, 18, -4.0], [6, 19, -8.0], [6, 1, -9.0], [6, 2, -6.0], [6, 3, -6.0], [6, 4, -8.0], [6, 5, -4.0], [7, 8, -8.0], [7, 9, -4.0], [7, 10, -5.0], [7, 11, -8.0], [7, 12, -8.0], [7, 13, -6.0], [7, 14, -6.0], [7, 15, -7.0], [7, 16, -12.0], [7, 17, -10.0], [7, 18, -4.0], [7, 19, -8.0], [7, 1, -9.0], [7, 2, -6.0], [7, 3, -6.0], [7, 4, -8.0], [7, 5, -4.0], [7, 6, -10.0], [8, 9, -4.0], [8, 10, -5.0], [8, 11, -8.0], [8, 12, -8.0], [8, 13, -6.0], [8, 14, -6.0], [8, 15, -7.0], [8, 16, -12.0], [8, 17, -10.0], [8, 18, -4.0], [8, 19, -8.0], [8, 1, -9.0], [8, 2, -6.0], [8, 3, -6.0], [8, 4, -8.0], [8, 5, -4.0], [8, 6, -10.0], [8, 7, -7.0], [9, 10, -5.0], [9, 11, -8.0], [9, 12, -8.0], [9, 13, -6.0], [9, 14, -6.0], [9, 15, -7.0], [9, 16, -12.0], [9, 17, -10.0], [9, 18, -4.0], [9, 19, -8.0], [9, 1, -9.0], [9, 2, -6.0], [9, 3, -6.0], [9, 4, -8.0], [9, 5, -4.0], [9, 6, -10.0], [9, 7, -7.0], [9, 8, -8.0], [10, 11, -8.0], [10, 12, -8.0], [10, 13, -6.0], [10, 14, -6.0], [10, 15, -7.0], [10, 16, -12.0], [10, 17, -10.0], [10, 18, -4.0], [10, 19, -8.0], [10, 1, -9.0], [10, 2, -6.0], [10, 3, -6.0], [10, 4, -8.0], [10, 5, -4.0], [10, 6, -10.0], [10, 7, -7.0], [10, 8, -8.0], [10, 9, -4.0], [11, 12, -8.0], [11, 13, -6.0], [11, 14, -6.0], [11, 15, -7.0], [11, 16, -12.0], [11, 17, -10.0], [11, 18, -4.0], [11, 19, -8.0], [11, 1, -9.0], [11, 2, -6.0], [11, 3, -6.0], [11, 4, -8.0], [11, 5, -4.0], [11, 6, -10.0], [11, 7, -7.0], [11, 8, -8.0], [11, 9, -4.0], [11, 10, -5.0], [12, 13, -6.0], [12, 14, -6.0], [12, 15, -7.0], [12, 16, -12.0], [12, 17, -10.0], [12, 18, -4.0], [12, 19, -8.0], [12, 1, -9.0], [12, 2, -6.0], [12, 3, -6.0], [12, 4, -8.0], [12, 5, -4.0], [12, 6, -10.0], [12, 7, -7.0], [12, 8, -8.0], [12, 9, -4.0], [12, 10, -5.0], [12, 11, -8.0], [13, 14, -6.0], [13, 15, -7.0], [13, 16, -12.0], [13, 17, -10.0], [13, 18, -4.0], [13, 19, -8.0], [13, 1, -9.0], [13, 2, -6.0], [13, 3, -6.0], [13, 4, -8.0], [13, 5, -4.0], [13, 6, -10.0], [13, 7, -7.0], [13, 8, -8.0], [13, 9, -4.0], [13, 10, -5.0], [13, 11, -8.0], [13, 12, -8.0], [14, 15, -7.0], [14, 16, -12.0], [14, 17, -10.0], [14, 18, -4.0], [14, 19, -8.0], [14, 1, -9.0], [14, 2, -6.0], [14, 3, -6.0], [14, 4, -8.0], [14, 5, -4.0], [14, 6, -10.0], [14, 7, -7.0], [14, 8, -8.0], [14, 9, -4.0], [14, 10, -5.0], [14, 11, -8.0], [14, 12, -8.0], [14, 13, -6.0], [15, 16, -12.0], [15, 17, -10.0], [15, 18, -4.0], [15, 19, -8.0], [15, 1, -9.0], [15, 2, -6.0], [15, 3, -6.0], [15, 4, -8.0], [15, 5, -4.0], [15, 6, -10.0], [15, 7, -7.0], [15, 8, -8.0], [15, 9, -4.0], [15, 10, -5.0], [15, 11, -8.0], [15, 12, -8.0], [15, 13, -6.0], [15, 14, -6.0], [16, 17, -10.0], [16, 18, -4.0], [16, 19, -8.0], [16, 1, -9.0], [16, 2, -6.0], [16, 3, -6.0], [16, 4, -8.0], [16, 5, -4.0], [16, 6, -10.0], [16, 7, -7.0], [16, 8, -8.0], [16, 9, -4.0], [16, 10, -5.0], [16, 11, -8.0], [16, 12, -8.0], [16, 13, -6.0], [16, 14, -6.0], [16, 15, -7.0], [17, 18, -4.0], [17, 19, -8.0], [17, 1, -9.0], [17, 2, -6.0], [17, 3, -6.0], [17, 4, -8.0], [17, 5, -4.0], [17, 6, -10.0], [17, 7, -7.0], [17, 8, -8.0], [17, 9, -4.0], [17, 10, -5.0], [17, 11, -8.0], [17, 12, -8.0], [17, 13, -6.0], [17, 14, -6.0], [17, 15, -7.0], [17, 16, -12.0], [18, 19, -8.0], [18, 1, -9.0], [18, 2, -6.0], [18, 3, -6.0], [18, 4, -8.0], [18, 5, -4.0], [18, 6, -10.0], [18, 7, -7.0], [18, 8, -8.0], [18, 9, -4.0], [18, 10, -5.0], [18, 11, -8.0], [18, 12, -8.0], [18, 13, -6.0], [18, 14, -6.0], [18, 15, -7.0], [18, 16, -12.0], [18, 17, -10.0], [19, 1, -9.0], [19, 2, -6.0], [19, 3, -6.0], [19, 4, -8.0], [19, 5, -4.0], [19, 6, -10.0], [19, 7, -7.0], [19, 8, -8.0], [19, 9, -4.0], [19, 10, -5.0], [19, 11, -8.0], [19, 12, -8.0], [19, 13, -6.0], [19, 14, -6.0], [19, 15, -7.0], [19, 16, -12.0], [19, 17, -10.0], [19, 18, -4.0]]
    V = [0, 1, 2, 3, 4, 5, 6, 7]
    E = [[0, 1, -66121.58400000002], [0, 2, -74716.48300000001], [0, 3, -67031.391], [0, 4, -68710.495], [0, 5, -73258.33600000001], [0, 6, -74382.447], [0, 7, -74086.293], [1, 2, -72744.098], [1, 3, -65059.006], [1, 4, -66738.11], [1, 5, -71285.951], [1, 6, -72410.062], [1, 7, -72113.908], [2, 3, -65109.263], [2, 4, -66788.367], [2, 5, -71336.208], [2, 6, -72460.319], [2, 7, -72164.16500000001], [2, 1, -64199.456000000006], [3, 4, -66796.396], [3, 5, -71344.23700000001], [3, 6, -72468.348], [3, 7, -72172.19400000002], [3, 1, -64207.485], [3, 2, -72802.384], [4, 5, -71307.225], [4, 6, -72431.336], [4, 7, -72135.182], [4, 1, -64170.473000000005], [4, 2, -72765.372], [4, 3, -65080.28], [5, 6, -72455.014], [5, 7, -72158.86000000002], [5, 1, -64194.151000000005], [5, 2, -72789.05], [5, 3, -65103.958], [5, 4, -66783.06199999999], [6, 7, -72144.31300000001], [6, 1, -64179.60400000001], [6, 2, -72774.50300000001], [6, 3, -65089.411], [6, 4, -66768.515], [6, 5, -71316.35600000001], [7, 1, -64185.722], [7, 2, -72780.621], [7, 3, -65095.528999999995], [7, 4, -66774.63299999999], [7, 5, -71322.474], [7, 6, -72446.58499999999]]

    print(maxspan(V,E))