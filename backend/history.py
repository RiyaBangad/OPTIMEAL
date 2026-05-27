import pandas as pd
import os

FILE_PATH = "data/history.csv"

# -------- LOAD HISTORY --------
def load_history():
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["Product", "Sugar", "Fat", "Score"])
        df.to_csv(FILE_PATH, index=False)
        return df

    try:
        df = pd.read_csv(FILE_PATH)
        return df
    except:
        return pd.DataFrame(columns=["Product", "Sugar", "Fat", "Score"])


# -------- SAVE HISTORY --------
def save_history(product, sugar, fat, score):
    df = load_history()

    new_row = pd.DataFrame([{
        "Product": product,
        "Sugar": sugar,
        "Fat": fat,
        "Score": score
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)