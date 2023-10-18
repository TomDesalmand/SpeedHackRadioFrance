import argparse
import pandas as pd
import matplotlib.pyplot as plt

def getOccurrence(data_file, keywords):
    data = pd.read_csv(data_file)
    filtered_data = data[data["diffusion_standfirst"].str.contains('|'.join(keywords), case=False, na=False, regex=True)]
    return len(filtered_data["diffusion_standfirst"])

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

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("Occurrences of climate-related programs in different radios")
    plt.savefig('climate_occurrences.png')
    plt.close()

if __name__ == "__main__":
    main()