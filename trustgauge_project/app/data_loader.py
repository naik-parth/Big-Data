import pandas as pd

def load_data(filepath="data/sample_reviews.csv"):
    df = pd.read_csv(filepath)
    return df
