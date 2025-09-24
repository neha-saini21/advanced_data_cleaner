import pandas as pd
import matplotlib.pyplot as plt
import datetime

def load_data(filename):
    return pd.read_csv(filename)

def remove_missing(data):
    return data.dropna()

def fill_missing(data):
    return data.fillna(data.mean(numeric_only=True))

def remove_duplicates(data):
    return data.drop_duplicates()

def generate_report(original, cleaned):
    report = {
        "Original Rows": len(original),
        "Cleaned Rows": len(cleaned),
        "Rows Removed": len(original) - len(cleaned),
        "Generated On": str(datetime.datetime.now())
    }
    with open("report.txt", "w") as f:
        for k, v in report.items():
            f.write(f"{k}: {v}\n")
    return report

def visualize_missing(data):
    missing = data.isnull().sum()
    missing.plot(kind="bar", title="Missing Values Per Column")
    plt.savefig("missing_values_chart.png")
    plt.close()

def main():
    print("🚀 Welcome to Advanced Data Cleaner")
    filename = input("Enter CSV file name: ")
    data = load_data(filename)

    while True:
        print("\nChoose an option:")
        print("1. Remove Missing Values")
        print("2. Fill Missing Values with Mean")
        print("3. Remove Duplicates")
        print("4. Visualize Missing Data")
        print("5. Export Cleaned Data & Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = remove_missing(data)
            print("✅ Missing values removed.")
        elif choice == "2":
            data = fill_missing(data)
            print("✅ Missing values filled with mean.")
        elif choice == "3":
            data = remove_duplicates(data)
            print("✅ Duplicates removed.")
        elif choice == "4":
            visualize_missing(data)
            print("📊 Missing data chart saved as missing_values_chart.png")
        elif choice == "5":
            data.to_excel("cleaned_data.xlsx", index=False)
            report = generate_report(load_data(filename), data)
            print("📂 Cleaned data saved as cleaned_data.xlsx")
            print("📑 Report generated as report.txt")
            print("📝 Report:", report)
        elif choice == "6":
            print("👋 Exiting tool. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
