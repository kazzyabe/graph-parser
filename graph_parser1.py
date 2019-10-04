class graph_based_parser:
    def load_data(self, f):
        '''
        load a training data(UD)

        return V,E 
        where 
        V = verticies for each training data eg. V[0] = verticies for the first sentence
        E = edges for each training data eg. E[0] = edges for the first sentence
        '''
        f = open(f, "r")
        # Gold standard graphs in training eg V[0], E[0] = first graph
        V = []
        E = []
        # tmp storage for v and e
        v_tmp = []
        e_tmp = []

        flag = False
        l = f.readline()
        while l:
            if "#" in l:
                # mark the begining of a graph
                flag = True
            elif l == "\n":
                # end of a graph
                flag = False
                V.append(v_tmp)
                e_tmp.sort()
                E.append(e_tmp)
                v_tmp = []
                e_tmp = []
            elif flag == True:
                l = l.split("\t")
                v_tmp.append(int(l[0]))
                e_tmp.append([int(l[6]),int(l[0]),l[7]])
            l = f.readline()
        return V, E

if __name__ == "__main__":
    gparse = graph_based_parser()
    V, E = gparse.load_data("/Users/kazuyabe/Documents/IU/courses/Codes/Python3/L545/01_Tokenisation/UD_Japanese-GSD-master/ja_gsd-ud-train.conllu")

    print("V = ")
    print(V[55])
    print("E = ")
    print(E[55])