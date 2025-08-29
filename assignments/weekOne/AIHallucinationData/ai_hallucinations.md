# Data Science 1 - HW 1
**Date:** August 29, 2025  

---

## AI Hallucination Cases

### What is the dataset?
[AI Hallucination Cases ](https://www.damiencharlotin.com/hallucinations/)

This is a dataset that looks at "legal decisions in cases where generative AI produced hallucinated content - typically fake citations, but also other types of arguments." I find adoption of AI to be a crucial topic in all settings - professional, educational, professional, etc. However, I found this dataset to be exceptionally interesting given that legal proceedings are typically environments of rigorous preparation. In infiltrating this environment, it really gets at the heart of the idea that AI might be reducing the quality of human thought and work.

### Outside of the dataset

**File Structure:**
- Single file dataset: `Charlotin-hallucination_cases.csv`
- No compression applied
- Standalone file with no accompanying documentation files

**File Format & Size:**
- **Format:** CSV (Comma-Separated Values)
- **File size:** 293.8 KB
- **Data dimensions:** 309 rows × 14 columns

### Loading the dataset

I [downloaded](https://www.damiencharlotin.com/hallucinations/) the CSV and moved it into the appropriate folder and used `read_csv` provided by the pandas library.

`df = pd.read_csv('./Charlotin-hallucination_cases.csv')`

### Inside the dataset

The dataset contains 309 rows and 14 columns. In looking at whether or not the data is tidy we can say the following.

Each variable forms a column with a corresponding observation:

- **Case Name** - The legal case identifier
- **Court** - The court where the case was heard | observations included court locations around the world from USA to New Zealand and Zimbabwe
- **State(s)** - Geographic jurisdiction
- **Date** - When the case occurred
- **Party(ies)** - Who was involved (Lawyer, Pro Se Litigant, etc.)
- **AI Tool** - Which AI system was used (ChatGPT, Claude AI, etc.)
- **Hallucination** - Type of AI error (fabricated citations, false quotes, etc.)
- **Outcome** - Court's decision
- **Monetary Penalty** - Financial consequences
- **Professional Sanction** - Professional disciplinary actions
- **Key Principle** - Legal principle established
- **Pointer** - Reference to specific legal authority
- **Source** - Source document
- **Details** - Detailed description of the case

| Variable | Description | Observations|
|---|---|---|
| Case Name | The legal case identifier | 307 unique observations, which is expected as the only repetition that occurs is in an effort to anonymize data ex: Giacomino y Otros v. Montserrat y Otros Rosario CA |
| Court | The court where the case was heard | 198 Unique observations ex: Rosario CA |
| State(s) | Geographic jurisdiction | 18 Unique observations ex: Argentina|
| Date | When the case occurred | Formatted YYYY-MM-DD ex: 2023-07-19 |
| Party(ies) | Who was involved (Lawyer, Pro Se Litigant, etc.) | 10 Unique observations ex: Lawyer, Pro Se Litigant |
| AI Tool | Which AI system was used (ChatGPT, Claude AI, etc.) | 41 unique observations - some rows contained multiple tools. Also "implied" and "unidentified" were options. |
| Hallucination | Type of AI error (fabricated citations, false quotes, etc.) | 199 unique observations with "Fabricated citation(s)" being the most frequent |
| Outcome | Court's decision | 208 unique observations ranging from "Warning" as most frequent at 74 occurrences to Monetary Sanctions |
| Monetary Penalty | Financial consequences | 39 unique observations with units varying depending on location |
| Professional Sanction | Professional disciplinary actions | Yes or no observations |
| Key Principle | Legal principle established | 58 unique observations ex: Use of AI does not excuse failure to verify; attorneys must personally check all citations under Rule 11 and professional conduct rules |
| Pointer | Reference to specific legal authority | 7 unique observations ex: Natural & Artificial Intelligence in Law |
| Source | Source document | 281 ex: /documents/722/G.C.A._Y_OTROS_c._M.F.D_Y_OTROS_Argentina_August_2025.pdf |
| Details | Detailed description of the case | 215 unique observations ex: The case at bar epitomizes the concern. Inordinate judicial resources were expended on reviewing cases cited by Plaintiff that did not exist. No doubt Plaintiff’s opponent in this litigation was forced to expend similar energies. Here, too, as noted, certain cases Plaintiff cited in support of her arguments stood for the opposite result from that which Plaintiff stated in her briefs. This kind of activity not only wastes precious and limited judicial resources, but it also drives up the cost of litigation unnecessarily for those who must defend against or seek to prosecute claims on behalf of paying clients, given the underpinnings of the American Rule that attaches to most civil litigation in this country. |

Is the data tidy? I would say no. For instance, the Monetary Penalty column could have been handled better. It combines the amount and currency - violating the principle of multiple variables are stored in one column. 

### Questions
Questions I think this dataset could at least begin to answer are as follows:
    - What countries are seeing the most cases?
    - What countries have seen the highest monetary penalties?

Related to questions above, it would be interesting to see if the rate of cases is substantially higher when English is not the language used in interacting with the model. 
