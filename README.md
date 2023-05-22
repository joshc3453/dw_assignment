<p align="center">
  <img src="https://cdn.phenompeople.com/CareerConnectResources/DELAA003Y/social/1200x630-1638972215979.jpg" alt="Delaware North Logo" style="width:300px; height:150px;">
</p>

# Delaware North Data and Analytics Recruiting Project

This project is part of the Delaware North Data and Analytics Recruiting Project. The goal of this project is to analyze COVID-19 testing data in the United States and provide insights into various metrics related to testing and patient outcomes.

## Project Overview

The US Department of Health and Human Services provides federal-level collection and publishing of COVID-19 testing and patient outcome data. The project aims to address the following metrics:

1. The total number of PCR tests performed as of yesterday in the United States.
2. The 7-day rolling average number of new cases per day for the last 30 days.
3. The 10 states with the highest test positivity rate (positive tests / tests performed) for tests performed in the last 30 days.

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



