import pandas as pd

# load dataset once
df = pd.read_excel("data/indian_food_dataset_expanded.xlsx", dtype={"Barcode": str})

def get_product(barcode):
    barcode = str(barcode)

    result = df[df["Barcode"] == barcode]

    if not result.empty:
        row = result.iloc[0]

        return {
            "name": row.get("Product_Name", "N/A"),
            "sugar": float(row.get("Sugar", 0)),
            "fat": float(row.get("Fat", 0))
        }

    return None