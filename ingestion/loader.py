import pandas as pd
# from pathlib import Path


def loader_csv(csv_file):
    
    df = pd.read_csv(csv_file)
    # df_name = Path(csv_file).stem
    return df