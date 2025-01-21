# Automated-Gene-Pathway-Enrichment-Analysis-with-STRING-API
This Python script automates the process of gene pathway enrichment analysis by integrating with the STRING Database API. It reads a list of genes from an input Excel file, queries the STRING database for biological enrichment data, filters relevant results, and outputs the findings into a new Excel file for downstream analysis.


# Gene Pathway Enrichment Analysis with STRING API

## Overview

This Python script automates the process of gene pathway enrichment analysis by integrating with the **STRING Database API**. It reads a list of genes from an input Excel file, queries the STRING database for biological enrichment data, filters relevant results, and outputs the findings into a new Excel file for downstream analysis.

## Key Features:
<ul>
    <li><strong>Input/Output</strong>: Reads gene data from an input Excel file and saves the enrichment results into a new Excel file.</li>
    <li><strong>API Integration</strong>: Uses the <strong>STRING Database API</strong> to retrieve pathway enrichment data for each gene.</li>
    <li><strong>Data Filtering</strong>: Filters results based on significance (FDR &lt; 0.05) and relevant pathway categories such as Gene Ontology (GO), KEGG, Reactome, and WikiPathways.</li>
    <li><strong>Automation</strong>: Automates the enrichment analysis for multiple genes, saving valuable research time.</li>
    <li><strong>Data Merging</strong>: Merges the original gene list with the enrichment results, providing a comprehensive view of each gene’s involvement in various biological processes.</li>
</ul>

## Script Workflow:
<ol>
    <li><strong>Input</strong>: The script takes an Excel file with a column of gene names.</li>
    <li><strong>API Call</strong>: For each gene, a request is sent to the STRING API to fetch enrichment data.</li>
    <li><strong>Data Processing</strong>: Filters are applied to ensure only relevant and statistically significant data (FDR &lt; 0.05) is included.</li>
    <li><strong>Output</strong>: The final results are saved in an Excel file, showing the enrichment terms, descriptions, categories, and statistical significance.</li>
</ol>

## How to Use:
<ol>
    <li>Download the script and ensure you have Python installed.</li>
    <li>Install necessary dependencies:
        <pre><code>pip install requests pandas</code></pre>
    </li>
    <li>Modify the input file path (`genes.xlsx`) and output file path (`genes_enrichment.xlsx`) to match your local paths.</li>
    <li>Run the script:
        <pre><code>python gene_enrichment_analysis.py</code></pre>
    </li>
</ol>
