from Weighting import PerceptronWeighter
from tagger import PerceptronTagger

class graph_based_parser:
    def __init__(self, mPOS="model.dat",loadPOS=True, mw="model", loadw=True):
        # POS
        self.tagger = PerceptronTagger(mPOS,loadPOS)

        # weighter
        self.weighter = PerceptronWeighter(mw,loadw)
    
    def parse(self, corpus):
        '''
        Parse the given corpus
        '''
        

    def load_data(self, f):
        '''
        load a training data(UD)

        return V,E 
        where 
        V = verticies for each training data eg. V[0] = verticies for the first sentence
        E = edges for each training data eg. E[0] = edges for the first sentence
        POS = universal part of speech tag
        '''
        f = open(f, "r")
        # Gold standard graphs in training eg V[0], E[0] = first graph
        V = []
        E = []
        POS = []
        # tmp storage for v and e
        v_tmp = []
        e_tmp = []
        pos_tmp = []

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
                POS.append(pos_tmp)
                v_tmp = []
                e_tmp = []
                pos_tmp = []
            elif flag == True:
                l = l.split("\t")
                v_tmp.append(int(l[0]))
                e_tmp.append([int(l[6]),int(l[0]),l[7]])
                pos_tmp.append(l[3])
            l = f.readline()
        return V, E, POS

if __name__ == "__main__":
    gparse = graph_based_parser()
    V, E, POS = gparse.load_data("/Users/kazuyabe/Documents/IU/courses/Codes/Python3/L545/01_Tokenisation/UD_Japanese-GSD-master/ja_gsd-ud-train.conllu")

    print("V = ")
    print(V[55])
    print("E = ")
    print(E[55])
    print("POS = ")
    print(POS[55])