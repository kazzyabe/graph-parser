def maxspan(V,E):
    """
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
    
    # if M has no cycle, it's the max spanning tree so return M
    #....
    #else cycle
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