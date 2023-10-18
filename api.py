import argparse
import pandas as pd
import matplotlib.pyplot as plt

def getOccurrence(data_file, keywords):
    data = pd.read_csv(data_file)
    filtered_data = data[data["diffusion_standfirst"].str.contains('|'.join(keywords), case=False, na=False, regex=True)]
    return len(filtered_data["diffusion_standfirst"]) if not filtered_data.empty else 1

def getFirstValue(data_file, keywords):
    data = pd.read_csv(data_file)
    filtered_data = data[data["diffusion_standfirst"].str.contains('|'.join(keywords), case=False, na=False, regex=True)]
    return filtered_data["diffusion_title"].iloc[0] if not filtered_data.empty else "" 

def main():
    parser = argparse.ArgumentParser(description="Calculate and plot climate-related program occurrences in different radio stations.")
    parser.add_argument("--keywords", nargs='+', help="List of keywords to search for in program descriptions", required=True)
    args = parser.parse_args()
    
    radio_data = [
        {"name": "France Culture", "file": "./data/grid/franceculture.csv"},
        {"name": "France Info", "file": "./data/grid/franceinfo.csv"},
        {"name": "France Inter", "file": "./data/grid/franceinter.csv"}
    ]
    keywords = args.keywords

    labels = [radio["name"] for radio in radio_data]
    sizes = [getOccurrence(radio["file"], keywords) for radio in radio_data]
    titles = [getFirstValue(radio["file"], keywords) for radio in radio_data]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis("equal")
    plt.title("Occurences of shows per radio related to the keywords")
    plt.figtext(0.5, 0.1, "Show suggestions:", ha="center", fontsize=12, weight="bold")
    for i, (label, title) in enumerate(zip(labels, titles)):
        plt.text(0, -1.2 - 0.06 * i, f"{label}: {title}", ha="center", fontsize=8)

    plt.savefig("climate_occurrences.png")
    plt.close()

if __name__ == "__main__":
    main()
