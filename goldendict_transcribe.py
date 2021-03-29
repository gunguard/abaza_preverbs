import pandas as pd
import re
import numpy as np

def fix_doubles(df):
    memo_keys = []
    memo_doubles = []
    for index, row in df.iterrows():
        if row["abaza"] in memo_keys:
            memo_doubles.append(row["abaza"])
        memo_keys.append(row["abaza"])
    memo_doubles = set(memo_doubles)
    print(memo_doubles)
    for m in memo_doubles:
        counter = 1
        for index, row in df.iterrows():
            if row["abaza"] == m:
                df.at[index, "abaza"] = str(row["abaza"]) + " (" + str(counter) + ")"
                counter += 1
    return df
        
        

def entry_correction(data):
    df = data

    df = df.replace(np.nan, '', regex = True)

    df['droot'] = df['root'].apply(lambda x: '[' + str(x) + ']')
    df['abaza'] = df['abaza'].apply(lambda x: re.sub('-', '', str(x) ))
    df['wordform'] = df['preverb'] + "-" + df['droot'] + "-" + df['suffix'] + df['msd']
    df['abaza'] = df['abaza'].apply(lambda x: re.sub('--', '-', str(x) ))
    df['value'] = df['wordform'] + '\\n' + df['category'] + '\\n' + df['translation'] + '\\n' + df['examples'] + '\\n' + df['section_name'] + '\\n' + "Клычев, с. page" + '\\n' + df['entry_id']
    dictionary = df[["abaza", "value"]]
    dictionary = fix_doubles(dictionary)
    return dictionary

def main():
    df = pd.read_csv('klychev_ocr_preparated.tsv', sep='\t')
    done_df = entry_correction(df)
    done_df.to_csv('result-value.tsv', sep="\t", encoding='utf-8')

if __name__ == '__main__':
    main()