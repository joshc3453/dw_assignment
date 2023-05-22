<p align="center">
  <img src="https://cdn.phenompeople.com/CareerConnectResources/DELAA003Y/social/1200x630-1638972215979.jpg" alt="Delaware North Logo" style="width:300px; height:150px;">
</p>

# Delaware North Data and Analytics Project

This project is part of the Delaware North Data and Analytics Project. The goal of this project is to analyze COVID-19 testing data in the United States and provide insights into metrics related to testing and patient outcomes.

## Project Overview

The US Department of Health and Human Services provides federal-level collection and publishing of COVID-19 testing and patient outcome data. The project aims to address the following metrics:

1. The total number of PCR tests performed as of yesterday in the United States.
2. The 7-day rolling average number of new cases per day for the last 30 days.
3. The 10 states with the highest test positivity rate (positive tests / tests performed) for tests performed in the last 30 days.

## Key Findings

### 1. The total number of PCR tests performed as of yesterday in the United States.
- As of yesterday, there have been 1,043,290,261 PCR tests reported in the United States. This number was found by taking the sum of all entries in the `new_results_reported` column of the dataset. Each new result represents a PCR test, regardless of the outcome (positive, negative, or uncertain).

### 2. The 7-day rolling average number of new cases per day for the last 30 days.
<p align="center">
  <img src="https://i.imgur.com/TaCUdyy.png" alt="Delaware North Logo" style="width:400px; height:316px;">
</p>
The 7-day rolling average number of new cases per day for the last 30 days shows promising results. The rolling average appears to be decreasing heavily, particularly since the first week of May. In order to find the rolling average of new cases per day, I first filtered the data to find all positive cases. I then grouped the data by date and summed up the new_results_reported column to get a count of how many positive cases there were for each day for the last 30 days. Next, I used the .rolling pandas method to calculate the average cases using a 7 day window and grabbed the last 30 days from the resulting dataset to get my results.


## Project Structure

The repository has the following structure:

- `get_data.py`: This script pulls the data and puts it into `dataset.csv`.
- `dataset.csv`: This file is generated using the `get_data.py` script and contains the COVID-19 testing data.
- `analysis.ipynb`: This Jupyter Notebook contains the exploratory data analysis and answers to the project's questions.
- `requirements.txt`: This file lists the project dependencies.

## Instructions

To reproduce the project results, follow these steps:

1. Run the `get_data.py` script to pull the data and generate the `dataset.csv` file.
2. Install the required dependencies specified in the `requirements.txt` file by running the following command:

   ```bash
   pip install -r requirements.txt
    ```
3. Run the analysis.ipynb notebook in Jupyter Notebook or JupyterLab. This notebook contains the data analysis and addresses the project's metrics.

## Data Source

The data used for this project can be found [here](https://healthdata.gov/dataset/COVID-19-Diagnostic-Laboratory-Testing-PCR-Testing/j8mb-icvb).