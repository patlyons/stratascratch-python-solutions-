#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data from stratascratch.com

# Import your libraries
import pandas as pd

# Start writing code

# Create column showing duration of membership
signups['duration'] = (signups['signup_stop_date'] - signups['signup_start_date']).dt.days

# Join transactions and memberships tables
df_1 = transactions.merge(signups, on = 'signup_id', how = 'left')

# Find average duration by location sorted most to least
avg_durations = signups.groupby(['location'])['duration'].mean().reset_index().sort_values( by = ['duration'] , ascending  = False)

# Find average transactions amount by location
avg_transactions = df_1.groupby(['location'])['amt'].mean().reset_index()

# Join average duration and transaction by location
df_2 = avg_durations.merge(avg_transactions , on = 'location' , how = 'left')

# Create column showing average transaction amount to average duration. Sort most to least
df_2['ratio'] = df_2['duration'] / df_2['amt']
df_2.sort_values( by = ['ratio'] , ascending = False)

