import pandas as pd
import matplotlib.pyplot as plt

def getOccurenceFranceCulture():
    dataFranceCulture = pd.read_csv("./data/grid/franceculture.csv")
    filteredDataFranceCulture = dataFranceCulture[dataFranceCulture["diffusion_standfirst"].str.contains("développement durable|réchauffement climatique|crise énergétique", case=False, na=False, regex=True)]
    return len(filteredDataFranceCulture["diffusion_standfirst"])

def getOccurenceFranceInfo():
    dataFranceInfo = pd.read_csv("./data/grid/franceinfo.csv")
    filteredDataFranceInfo = dataFranceInfo[dataFranceInfo["diffusion_standfirst"].str.contains("développement durable|réchauffement climatique|crise énergétique", case=False, na=False, regex=True)]
    return len(filteredDataFranceInfo["diffusion_standfirst"])

def getOccurenceFranceInter():
    dataFranceInter = pd.read_csv("./data/grid/franceinter.csv")
    filteredDataFranceInter = dataFranceInter[dataFranceInter["diffusion_standfirst"].str.contains("développement durable|réchauffement climatique|crise énergétique", case=False, na=False, regex=True)]
    return len(filteredDataFranceInter["diffusion_standfirst"])

def main():
    labels = ['France Culture', 'France Info', 'France Inter']
    sizes = [getOccurenceFranceCulture(), getOccurenceFranceInfo(), getOccurenceFranceInter()]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("Occurrences of climate-related programms in different radios")
    plt.savefig('climate_occurrences.png')
    plt.close()

if __name__ == "__main__":
    main()