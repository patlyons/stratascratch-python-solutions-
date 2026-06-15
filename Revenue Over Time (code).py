#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data from stratascratch.com

# Import your libraries
import pandas as pd

# Start writing code

# Filter out return purchases
amazon_purchases = amazon_purchases[amazon_purchases['purchase_amt'] > 0 ]

# Find total sales per month
amazon_purchases = amazon_purchases.groupby(amazon_purchases['created_at'].dt.strftime('%Y-%m'))['purchase_amt'].sum().reset_index()

# Create two new columns for previous months total sales
amazon_purchases['previous_month'] = amazon_purchases['purchase_amt'].shift(1)
amazon_purchases['previous_two_months'] = amazon_purchases['purchase_amt'].shift(2)

# Identify rolling three months average sales per month
amazon_purchases['rolling_3_months_sales_avg'] = amazon_purchases[['purchase_amt', 'previous_month', 'previous_two_months']].mean(axis=1)
amazon_purchases[['created_at' , 'rolling_3_months_sales_avg']]

