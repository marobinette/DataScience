# Data Science 1 - HW 1
**Date:** September 1, 2025  

---

## Dataset of World Refugee and Asylum Policies

### 1) What is the dataset?
[Dataset of World Refugee and Asylum Policies](https://datanalytics.worldbank.org/dwrap/)

> "The "Dataset of World Refugee and Asylum Policies (DWRAP)" offers a complete dataset of de jure asylum and refugee policies for all 193 countries for the 70 years from 1951-2022. Explore what policies are in place and how these policies have shifted over the past seven decades. The DWRAP index aggregates policies from 5 fields: Access; Services; Livelihoods; Movement, and Citizenship and Participation; with values ranging from 0 to 1, where values closer to 1 indicate more liberal policies."

**Citation:** World Bank; with Christopher W. Blair, Guy Grossman and Jeremy M. Weinstein. 2024. "Dataset of World Refugee and Asylum Policies." World Bank Development Data Hub.

I found this dataset in the 2025.04.30 edition of "Data is Plural".This selection was motivated by personal interest and practicality. From a practical standpoint, it's different than the other datasets I have selected in that it is a time series. In spanning seven decades and 193 countries, it provides a lovely historical record of how the world's borders have behaved over time. I really enjoyed examining different countries with respect to what was happening historically. For instance, Portugal was freed from a 50-year authoritarian regime in 1974 and began transitioning toward democracy. In 1980 Portugal's index moved from a value of 0 to 0.24.

I will say the data available for download is a bit limited. You can get data about the 5 policy index fields (i.e. Access, Services, Livelihoods, Movement, and Participation) in the year 2022 only, which makes comparing across these fields over time impossible.

### 2) Outside of the dataset
Of the 193 countries I downloaded and examined 4 (details below). The dataset is copyrighted and the details are available under the resources [tab](https://datanalytics.worldbank.org/dwrap/#).

**File Structure, Format & Size:**
- File: `Portugal_dwrap__mean_2025_09_01_08_40_50_868068_data.csv`
- No compression applied
- Standalone file with no accompanying documentation files
- **Format:** CSV (Comma-Separated Values)
- **File size:** 2.8 KB
- **Data dimensions:** 72 rows × 4 columns

- File: `Afghanistan_dwrap__mean_2025_08_31_06_44_53_752427_data.csv`
- No compression applied
- Standalone file with no accompanying documentation files
- **Format:** CSV (Comma-Separated Values)
- **File size:** 3.3 KB
- **Data dimensions:** 72 rows × 4 columns

- File: `Canada_dwrap__mean_2025_09_01_08_42_17_649223_data.csv`
- No compression applied
- Standalone file with no accompanying documentation files
- **Format:** CSV (Comma-Separated Values)
- **File size:** 3.1 KB
- **Data dimensions:** 72 rows × 4 columns

- File: `United_States_dwrap__mean_2025_09_01_08_42_40_783942_data.csv`
- No compression applied
- Standalone file with no accompanying documentation files
- **Format:** CSV (Comma-Separated Values)
- **File size:** 3.6 KB
- **Data dimensions:** 72 rows × 4 columns

### 3) Loading the dataset

From The World Bank's [homepage](https://datanalytics.worldbank.org/dwrap/#), navigate to the "ANALYSE" tab, select the desired country, and click "Download Data". I moved the CSV into the appropriate folder and used `read_csv` provided by the pandas library.

ex:
`df = pd.read_csv('./Portugal_dwrap__mean_2025_09_01_08_40_50_868068_data.csv')`

### 4) Inside the dataset
The dataset is a time series. It contains 4 variables. The dataset is very tidy!
- `country_policy`: the variable name is a bit confusing as it actually points to the country not the policy
- `year`: the year being examined
- `view_index`: the index from 0 to 1 where 1 is indicative of a more liberal policy
- `stateabb`: the abbreviation of the country

### 5) Questions
Questions I think this dataset could answer are as follows:
- Which countries in the world are the most liberal in their refugee and asylum policies today?
- What countries have progressed the most over the 70-year period in terms of their refugee and asylum policies?
- What countries have digressed the most over the 70-year period in terms of their refugee and asylum policies?

A question I think would be fun to answer and to create a visualization for:
- How have historic events (i.e. regime change, war, revolution) impacted refugee and asylum policies over the 70-year period?
