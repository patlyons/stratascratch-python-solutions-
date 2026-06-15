#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Data from stratascratch.com
#Consecutive Days User Activity

import pandas as pd
import numpy as np
sf_events

# Drop duplicates and sort values by user and date
sf_events = sf_events.drop_duplicates(keep=False)
sf_sorted = sf_events.sort_values(by = ['user_id' , 'record_date'], ascending = [True, True])

# Create two new columns for previous times used
sf_sorted['second_date'] = np.where(sf_sorted['user_id'] == sf_sorted['user_id'].shift(1), sf_sorted['record_date'].shift(1), np.datetime64('NaT'))
sf_sorted['third_date'] = np.where(sf_sorted['user_id'] == sf_sorted['user_id'].shift(1), sf_sorted['record_date'].shift(2), np.datetime64('NaT'))

# Filter for only users with three uses
sf_sorted_filtered = sf_sorted[sf_sorted['third_date'].notna()]

# Create new column showing difference between first and third date
sf_sorted_filtered['days_between_3_and_1'] = (sf_sorted['third_date'] - sf_sorted['record_date']).dt.days

# Filter for only users with three consecutive days
sf_sorted_filtered[sf_sorted_filtered['days_between_3_and_1'] == -2][['user_id']]

