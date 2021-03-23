import pandas as pd
import re
import numpy as np

def entry_correction(data):
    df = data
    df = df.replace(np.nan, '', regex = True)
    
    df['droot'] = df['root'].apply(lambda x: '√' + str(x))
    df['abaza'] = df['abaza'].apply(lambda x: re.sub('-', '', str(x) ))
    df['wordform'] = df['preverb'] + "-" + df['droot'] + "-" + df['suffix'] + df['msd']
    df['abaza'] = df['abaza'].apply(lambda x: re.sub('--', '-', str(x) ))

    df['value'] = df['wordform'] + "\n" + df['category'] + "\n" + df['translation'] + "\n" + df['examples'] + "\n" + df['section_name'] + "\n" + "Клычев, с. page" + "\n" + df['entry_id']
    
    return df

def main():
    df = pd.read_csv('klychev_ocr_preparated.tsv', sep='\t')
    done_df = entry_correction(df)
    done_df.to_csv('result.tsv', sep="\t")

if __name__ == '__main__':
    main()
