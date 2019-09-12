"""
Graph-based Parser
Authors: Ata, Everett, Kazuki
"""

"""
// Tagger from the 500 line parser article

class PerceptronTagger(object):
    '''Greedy Averaged Perceptron tagger'''
    model_loc = os.path.join(os.path.dirname(__file__), 'tagger.pickle')
    def __init__(self, classes=None, load=True):
        self.tagdict = {}
        if classes:
            self.classes = classes
        else:
            self.classes = set()
        self.model = Perceptron(self.classes)
        if load:
            self.load(PerceptronTagger.model_loc)
"""

if __name__ == "__main__":
    
    # opens sample file
    with open('example_parser_in_out.txt') as data:
        file = data.readlines()
    
    # prints each line of the sample file
    for i in range(len(file)):
        print(file[i])

