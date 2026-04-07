import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        # ✅ Your exact file path
        file_path = "C:/Users/bhumi/Downloads/Task 5 Equality Table.xlsx"
        
        df = pd.read_excel(file_path)
        print("✅ Data loaded successfully!\n")
        print(df.head())  # show first rows
        
        return df

    except Exception as e:
        print("❌ Error loading file:", e)
        return None


def clean_data(df):
    print("\n🧹 Cleaning Data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values with 0 (or you can drop them)
    df = df.fillna(0)

    print("✅ Data cleaned!")
    return df


def analyze_data(df):
    print("\n📊 Summary Statistics:\n")
    print(df.describe())

    # Show column names
    print("\n📌 Columns in dataset:")
    print(df.columns)


def filter_data(df):
    print("\n🔍 Filtering Data...")

    # Example: filter numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        col = numeric_cols[0]  # take first numeric column
        filtered = df[df[col] > df[col].mean()]
        
        print(f"\n✅ Rows where {col} > average:\n")
        print(filtered.head())
    else:
        print("⚠️ No numeric column found!")


def group_data(df):
    print("\n📊 Grouping Data...")

    # Try grouping if any column has few unique values
    for col in df.columns:
        if df[col].nunique() < 10:
            grouped = df.groupby(col).size()
            print(f"\n✅ Grouped by {col}:\n")
            print(grouped)
            break


def plot_data(df):
    print("\n📈 Generating Graph...")

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        df[numeric_cols[0]].plot(kind='hist')
        plt.title(f"{numeric_cols[0]} Distribution")
        plt.xlabel(numeric_cols[0])
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("⚠️ No numeric data to plot!")


def main():
    df = load_data()

    if df is not None:
        df = clean_data(df)
        analyze_data(df)
        filter_data(df)
        group_data(df)

        choice = input("\nDo you want to see graph? (y/n): ")
        if choice.lower() == 'y':
            plot_data(df)


if __name__ == "__main__":
    main()