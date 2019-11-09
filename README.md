# graph-parser
graph-based parser

To clone, run the following command in your terminal once you are in your target folder:
git clone https://github.com/MrEvrgreen/graph-parser.git

Will use conll format and output each word tagged with part of speech and the root in the correctly formatted columns.

## Dependency
1. https://github.com/ftyers/conllu-perceptron-tagger.git

## Data (UD tree bank)
1. ex. https://github.com/UniversalDependencies/UD_English-EWT.git

## dev evaluation
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     62.59 |     62.59 |     62.59 |     62.59
LAS        |     62.59 |     62.59 |     62.59 |     62.59
```