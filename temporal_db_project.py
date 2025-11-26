import pandas as pd

def main():
    db_path = "project_db_2025.xlsx"

    # טעינת הקובץ
    df = pd.read_excel(db_path)

    # ----------------------
    # ✨ הסרת העמודות המיותרות
    # ----------------------

    # קודם מורידים רווחים משמות עמודות:
    df.columns = df.columns.str.strip()

    # בוחרים רק את העמודות החשובות:
    valid_columns = [
        "First name",
        "Last name",
        "LOINC-NUM",
        "Value",
        "Unit",
        "Valid start time",
        "Transaction time"
    ]

    df = df[valid_columns]

    # הדפסה לבדיקה
    print("5 השורות הראשונות אחרי סינון:")
    print(df.head())

if __name__ == "__main__":
    main()
