# Geelong City Recycling Instructions Repository

This repository contains Python code to scrape recycling instructions from the City of Greater Geelong website and a dataset of recycling instructions for various materials. Additionally, it includes an edited version of the dataset with a new column 'bin' that categorizes materials into red, yellow, green, or dropoff based on the provided instructions.

**Note**: This README has been generated by an AI model.

## Repository Structure

- `scrape_recycling_instructions.py`: Python script for scraping recycling instructions from the City of Greater Geelong website and exporting the dataset.
- `recycling_instructions.csv`: The original dataset containing recycling instructions.
- `recycling_instructions_edited.csv`: The edited dataset with the 'bin' column added.

## Code Overview

The Python script, `scrape_recycling_instructions.py`, performs the following steps:

1. Imports necessary libraries, including BeautifulSoup for web scraping and pandas for data manipulation.
2. Retrieves recycling instructions data from the City of Greater Geelong website.
3. Parses the HTML content of the website to extract recycling instructions.
4. Stores the scraped data in a DataFrame.
5. Exports the DataFrame to a CSV file, `recycling_instructions.csv`.

## Edited Dataset ('recycling_instructions_edited.csv')

The edited dataset, `recycling_instructions_edited.csv`, contains the following columns:

- `material`: The type of material to be recycled.
- `sub_material`: A more specific description of the material.
- `instructions`: Recycling instructions for the material.
- `bin`: A classification of where the material should be disposed of. Possible values are:
  - `red`: Indicates that the material should be placed in a red bin.
  - `yellow`: Indicates that the material should be placed in a yellow bin.
  - `green`: Indicates that the material should be placed in a green bin.
  - `dropoff`: Indicates that the material should be dropped off at an appropriate authority or processing organization, and there may be associated costs.
 
 - **Note**: In the edited dataset (`recycling_instructions_edited.csv`), only the first instruction for each material was considered to determine the bin / action to take, even if there were multiple instructions provided. This simplification was made to keep the dataset straightforward and avoid potential confusion in recycling recommendations.

## How to Use the Edited Dataset

You can use the `recycling_instructions_edited.csv` dataset in whatever way you prefer. Please make sure to credit City of Greater Geelong [website](https://www.geelongaustralia.com.au/recycling/guide/default.aspx) while doing so. 

## Contributing

If you wish to contribute to this repository, feel free to fork it, make changes, and submit a pull request. Contributions, bug reports, and suggestions are welcome!

---

*Generated by ChatGPT on 11th Sep 2023*
