import requests
import json
import pandas as pd

# Input file path
input_file = r'genes.xlsx'

# Output file path
output_file = r'genes_enrichment.xlsx'

# Read the input Excel file
df = pd.read_excel(input_file)

# Make sure the 'Gene' column exists
if 'Gene' not in df.columns:
    raise Exception("The input file must contain a 'Gene' column.")

# Extract the genes from the first column
genes = df['Gene'].tolist()

# API parameters
string_api_url = "https://string-db.org/api"
output_format = "json"
method = "enrichment"
request_url = "/".join([string_api_url, output_format, method])

# Prepare a list to store the enrichment results
results_list = []

# Call the API for each gene
for gene in genes:
    params = {
        "identifiers": gene,
        "species": 9606,  # NCBI species identifier for humans
        "caller_identity": "Jarvis"
    }

    # Make the API request
    response = requests.post(request_url, data=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        # Parse the results
        for row in data:
            term = row["term"]
            preferred_names = ",".join(row["preferredNames"])
            fdr = float(row["fdr"])
            description = row["description"]
            category = row["category"]

            # Filter to include relevant categories: Gene Ontology, KEGG, Reactome, WikiPathways, etc.
            if category in ["Process", "KEGG", "Reactome", "WikiPathways", "Pfam", "InterPro", "SMART"] and fdr < 0.05:
                # Append the results to the list
                results_list.append({
                    'Gene': gene,
                    'Term': term,
                    'Preferred Names': preferred_names,
                    'FDR': fdr,
                    'Description': description,
                    'Category': category  # New: Add a column for category type
                })
    else:
        print(f"Failed to fetch data for {gene}. Status code: {response.status_code}")

# Convert the list to a DataFrame
results_df = pd.DataFrame(results_list)

# Merge the results with the original data
merged_df = pd.merge(df, results_df, how='left', on='Gene')

# Save the results to a new Excel file
merged_df.to_excel(output_file, index=False)

print(f"Enrichment analysis results have been saved to {output_file}.")
