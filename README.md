# graph-parser
graph-based parser

To clone, run the following command in your terminal once you are in your target folder:
git clone https://github.com/MrEvrgreen/graph-parser.git

Will use conll format and output each word tagged with part of speech and the root in the correctly formatted columns.

## Dependency
1. https://github.com/ftyers/conllu-perceptron-tagger.git

## Data (UD tree bank)
1. ex. https://github.com/UniversalDependencies/UD_English-EWT.git

## Weights
{'bias': -5.0, 'i suffix rom': -1.0, 'i pref1 F': -1.0, 'i-1 tag ROOT': -1.0, 'i-2 tag START': -1.0, 'i tag+i-2 tag ROOT START': -1.0, 'head POS ROOT': -5.0, 'head word ROOT': -5.0, 'dependent POS ADP': -1.0, 'dependent word From': -1.0, 'i suffix the': -1.0, 'i pref1 t': -2.0, 'i-1 tag ADP': -1.0, 'i-2 tag ROOT': -1.0, 'i tag+i-2 tag ADP ROOT': -1.0, 'dependent POS DET': -2.0, 'dependent word the': -1.0, 'i suffix AP': -1.0, 'i pref1 A': -1.0, 'i-1 tag DET': -2.0, 'i-2 tag ADP': -1.0, 'i tag+i-2 tag DET ADP': -1.0, 'dependent POS PROPN': -1.0, 'dependent word AP': -1.0, 'i suffix mes': 1.0, 'i pref1 c': 1.0, 'i-1 tag PROPN': 1.0, 'i-2 tag DET': 0.0, 'i tag+i-2 tag PROPN DET': 1.0, 'dependent POS VERB': 1.0, 'dependent word comes': 1.0, 'i suffix his': -1.0, 'i-1 tag VERB': -1.0, 'i-2 tag PROPN': -1.0, 'i tag+i-2 tag VERB PROPN': -1.0, 'dependent word this': -1.0, 'i suffix ory': -1.0, 'i pref1 s': -1.0, 'i-2 tag VERB': -1.0, 'i tag+i-2 tag DET VERB': -1.0, 'dependent POS NOUN': -1.0, 'dependent word story': -1.0, 'i suffix :': -1.0, 'i pref1 :': -1.0, 'i-1 tag NOUN': -1.0, 'i tag+i-2 tag NOUN DET': -1.0, 'dependent POS PUNCT': -1.0, 'dependent word :': -1.0}