# Poll Aggregation & Data Cleaning: "Should Pigs Be Able to Fly?

This project demonstrates how to ingest, clean, merge, and analyze weekly polling data using Python
and Pandas Library. Although the ballot initiative is fictional, the workflow reflects real-world
challenges related to inconsistent data formats, weekly updates, and summary reporting.

Project Overview

The program reads a master polling dataset and a weekly update file, cleans and merges the data, handles 
non-numeric formatting, calculates statistical summaries, and exports final results in both CSV and Excel formats.

Features
- Reads and validates encoded CSV files
- Detects and corrects formatting irregularities in input files
- Cleans percentage strings and converts them to float values
- Merges updated polling data while removing duplicates
- Sorts the dataset alphabetically and appends a row with average values
- Exports cleaned data to both CSV and Excel outputs

Technologies Used:
- Python 3
-  Pandas
-  openpyxl (for Excel output)

