# FIFA Player Attribute Analysis

## 1. Project Overview

This project analyzes FIFA player statistics from 2017 to 2022 to uncover insights about what makes a top-rated footballer. The goal is to explore attribute trends, relationships between skills, and track player performance evolution over time using data visualization, statistical analysis, and dimensionality reduction techniques.

Key questions explored include:
- What attributes are most predictive of high overall ratings?
- How do player performances evolve over the years?
- How do legends like Messi and Ronaldo compare across different editions?
- Which countries and positions dominate FIFA ratings?
- Are there hidden clusters or relationships between player attributes?

## 2. Set Up the Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

## 3. Prepare the Data
The project uses a merged dataset (output/fifa_merged.csv). If this file is not already present, run the following script to generate it:

python scripts/load_and_merge.py

This script reads all CSV files in the data/ directory, tags them by year, merges them, and saves the result in the output/ folder.

## 4. Launch the Notebook
jupyter notebook notebooks/FIFA_Analysis_Project.ipynb
You can now step through the analysis, visualizations, and insights inside the notebook.
