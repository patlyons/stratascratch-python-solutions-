# Revenue Trend Analysis with Rolling Averages

## Overview

This project analyzes purchase revenue over time and calculates a three-month rolling average of monthly sales. Rolling averages help smooth short-term fluctuations and reveal longer-term business trends.

## Business Problem

Monthly revenue can fluctuate due to seasonality, promotions, or customer behavior. A rolling average provides a more stable view of business performance and helps stakeholders identify overall trends.

## Approach

The dataset was filtered to include only positive purchase amounts. Monthly revenue totals were calculated and aggregated before applying a three-month rolling average calculation.

Key steps included:

* Filtering invalid or negative transactions
* Aggregating revenue by month
* Creating lagged revenue values using shifted observations
* Calculating a three-month rolling average across monthly sales totals

## Technologies Used

* Python
* Pandas

## Key Pandas Concepts

* Data filtering
* `groupby()`
* Aggregations
* `shift()`
* Time-based analysis
* Rolling calculations

## Outcome

The analysis generated a smoothed revenue trend that highlights overall business performance while reducing the impact of month-to-month volatility.

## Skills Demonstrated

* Revenue analytics
* Financial reporting
* Time-series analysis
* Business intelligence
* Python data analysis
