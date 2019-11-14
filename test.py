from Weighting import *

# corpus_file = open("UD_English-EWT/en_ewt-ud-dev.conllu", "r")
corpus_file = "testPOStagged.conllu"
# corpus_file = "UD_English-EWT/en_ewt-ud-dev.conllu"
# corpus_file = "UD_English-EWT/en_ewt-ud-train.conllu"
# trainer(corpus_file, "Parser_train20mod2.dat")
parser(corpus_file, "Parser_train20mod2.dat")









# sentences = []
# for sent in corpus_file.read().split('\n\n'):
#     sentence = []
#     for token in sent.split('\n'):
#         if token.strip() == '':
#             continue
#         if token[0] == '#':
#             continue
#         sentence.append(tuple(token.strip().split('\t')))
#     sentences.append(sentence)

# START = ['-START-', '-START2-']
# END = ['-END-', '-END2-']

# def _normalise(word):
#     '''Normalisation used in pre-processing.

#     - All words are lower cased
#     - Digits in the range 0000-2100 are represented as !YEAR;
#     - Other digits are represented as !DIGITS

#     :rtype: str
#     '''
#     if '-' in word and word[0] != '-':
#         return '!HYPHEN'
#     elif word.isdigit() and len(word) == 4:
#         return '!YEAR'
#     elif word[0].isdigit():
#         return '!DIGITS'
#     else:
#         return word.lower()

# s = sentences[0]
# prev,prev2 = START
# context = START + [_normalise(w[1]) for w in s] + END
# word = s[1][1]

# def _get_features(i, word, context, prev, prev2):
#     '''Map tokens into a feature representation, implemented as a
#     {hashable: float} dict. If the features change, a new model must be
#     trained.
#     '''
#     def add(name, *args):
#         print(tuple(args))
#         features[' '.join((name,) + tuple(args))] += 1

#     i += len(START)
#     features = defaultdict(int)
#     # It's useful to have a constant feature, which acts sort of like a prior
#     add('bias')
#     add('i suffix', word[-3:])
#     add('i pref1', word[0])
#     add('i-1 tag', prev)
#     add('i-2 tag', prev2)
#     add('i tag+i-2 tag', prev, prev2)
#     add('i word', context[i])
#     add('i-1 tag+i word', prev, context[i])
#     add('i-1 word', context[i-1])
#     add('i-1 suffix', context[i-1][-3:])
#     add('i-2 word', context[i-2])
#     add('i+1 word', context[i+1])
#     add('i+1 suffix', context[i+1][-3:])
#     add('i+2 word', context[i+2])
#     #print(word, '|||', features)
#     return features

# print(_get_features(1, word, context, prev, prev2))