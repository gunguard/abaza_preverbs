import pandas as pd
import re


def entry_correction():
    lexemes = []
    morphemes = []
    keys = []
    values = []
    #    with open('klychev_ocr_preparated.tsv', newline='', encoding = 'utf-8') as csvfile:
    #        reader = csv.reader(csvfile)
    #        for row in reader:
    data = pd.read_csv('klychev_ocr_preparated.tsv', sep='\t')
    # print(type(data))
    for root in data['root']:
        rootd = '√'+ root
        print(rootd)
    for item in data['abaza']:
        morphemes = []
        element = item.split('-')
        for morpheme in element:
            if morpheme.endswith(')') and morpheme.startswith('('):
                morpheme1 = morpheme[1 : -1]
            morphemes.append(morpheme1)
            print(morpheme1)
        word = ''.join(morphemes)
        print(word)
        # for root in data['root']:
            # root = ('√')+ root
            # print(root)


        # morphchain = data['preverb'] + '\n' + root
       # value = word + '\n' +
        # print(element)
        # print(item)
    # print(root)
    # print(data['category'])


def main():
    entry_correction()


if __name__ == '__main__':
    main()
