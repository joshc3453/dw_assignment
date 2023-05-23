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
  <img src="https://i.imgur.com/TaCUdyy.png" alt="7 Day Rolling Average" style="width:400px; height:316px;">
</p>

- The 7-day rolling average number of new cases per day for the last 30 days shows promising results. The rolling average appears to be decreasing heavily, particularly since the first week of May. In order to find the rolling average of new cases per day, I first filtered the data to find all positive cases. I then grouped the data by date and summed up the `new_results_reported` column to get a count of how many positive cases there were for each day for the last 30 days. Next, I used the .rolling pandas method to calculate the average cases using a 7 day window and retrieved the last 30 days from the resulting dataset to get my results.

### 3. The 10 states with the highest test positivity rate (positive tests / tests performed) for tests performed in the last 30 days.
- To find this metric, I first retrieved a date 30 days prior to the current date. The code is dynamic, so it will subtract 30 days from the day that the code is run using a timedelta operation. I used that retrieved date to create a new DataFrame, `df3`, to filter data such that it only retrieves dates greater than or equal to the last 30 days date, effectively returning reports within the last 30 days.

- Next, I grouped the data in `df3` by state, and ran an aggregate operation to sum up the values in the `new_results_reported` column to get the total number of tests performed for each state.

- In a separate DataFrame, `df3_positive`, I filtered the data to only include positive cases and then did the same grouping and aggregation done in the previous step. This resulted in a DataFrame with a sum of total positive tests for each state.

- Finally, I combined the DataFrames so that the resulting DataFrame had the columns `state_name`, `total_positive_tests`, and `total_cases`. I then simply divided the total positive tests by the total cases for each state to calculate the positivty rate.

- Sorting by positivty rate in descending order results in the following output:
<p align="center">
  <img src="https://i.imgur.com/WNvKdhZ.png" alt="Delaware North Logo" style="width:478px; height:247px;">
</p>

## Caveats
There are many caveats that should be addressed with this project. Please keep in mind the following notes when interpreting the results:
### 56 States
- Traditionally, the United States has 50 states. Although this data was provided by the United States government, there are 56 unique states listed in the dataset. The six additional states include:
    1. District of Columbia
    2. Guam
    3. Marshall Islands
    4. Northern Mariana Islands
    5. Puerto Rico
    6. U.S. Virgin Islands

- Each of these entities has some level of political representation with the United States which is why they are included in this dataset.

### Small Sample Sizes
- Many states within the United States are small in population size relative to other states. Similarly, the six extra "states" previously mentioned have very small population sizes. States with smaller populations are more prone to outliers or skewed data since there is less data to analyze.  For example, the U.S. Virgin Islands has the highest positivty rate for tests performed in the last 30 days, but there have only been 177 tests performed in that time period with 50 total positive tests, resulting in a positivty rate of 28%, 10% higher than the second highest state. Interestingly, most states in the top 10 for positivity rate have somewhat smaller population sizes like South Dakota, Guam, Wyoming, Hawaii, and New Mexico.

### Change in Testing Patterns
- Covid-19 was rampant in 2020 and 2021, and so Covid testing sites were widespread, easily accessible, and strongly encouraged. As such, many Americans were getting tested for Covid proactively (especially because the virus could be present before symptoms even appear). This resulted in a lower positivity rate since a large population of the country was testing proactively, even when they felt healthy. Now in 2023, the pandemic has officially been declared over and the majority of the population have been vaccinated. Therefore, testing has been decreasing and those that do test are more likely to test reactively rather than proactively. 

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

The data used for this project is provided by the US Department of Health and Human Services and can be found [here](https://healthdata.gov/dataset/COVID-19-Diagnostic-Laboratory-Testing-PCR-Testing/j8mb-icvb).