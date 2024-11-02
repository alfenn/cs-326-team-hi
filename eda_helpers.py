import pandas as pd
import pandas as np
from collections import Counter

def col_details(df: pd.DataFrame):
    '''
    Display all column names, data types, and unique values for categorical columns
    '''
    for col in df.columns:
        dtype = df[col].dtype
        if dtype in ['object', 'category']:
            val_counts = Counter()
            for x in df[col]:
                val_counts[x] += 1
            print(f"- {col}: {dtype} ({len(val_counts)} unique values)")
            for x in sorted(list(val_counts.items()), key=lambda x: x[1], reverse=True)[:10]:
                print(f'  - {x[0]} ({x[0].__class__.__name__}): {x[1]}')
        else:
            print(f"- {col}: {dtype}")
    