#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:29:27 2021

@author: nicoleyu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
# -----------------------------------------------
# Train data set
# -----------------------------------------------
train = pd.read_csv("project_data/application_train.csv")
train = pd.DataFrame(train)

train.head  # 307511 rows x 122 columns
train.columns  # return a list of variables' name 

# To aviod running too large data set, randomly select 10000 row
train = train.sample(n = 10000)
# id that being randomly select
curr_id = train["SK_ID_CURR"].unique().tolist()

# Identify quantitative and qualitative variable
# Total of 106 numeric variables, 16 cat_vars
num_vars = train._get_numeric_data().columns
cat_vars = list(set(train.columns)- set(num_vars))


# Missing value rate of each column
na = train.isna().sum()/train.shape[0]
na = na.to_frame()
na = na.rename(columns = {0 :'na_rate'})

# Keep only those with zero missing rate


train['AMT_ANNUITY']
train['AMT_CREDIT']

1293502.5/ 35698.5

train[['AMT_GOODS_PRICE', 'AMT_CREDIT', 'TARGET']]

# -----------------------------------------------
# Previous application
# -----------------------------------------------
previous = pd.read_csv('project_data/previous_application.csv')

t = previous[['RATE_INTEREST_PRIMARY', 'RATE_INTEREST_PRIVILEGED', 
          'NAME_YIELD_GROUP']]

s = t.dropna()

previous.columns
date = previous[['DAYS_DECISION', 'DAYS_TERMINATION']]
date.describe()

previous['NAME_CONTRACT_STATUS']
# -----------------------------------------------
# Bureau 
# -----------------------------------------------
bureau = pd.read_csv("project_data/bureau.csv")
bureau_id = bureau["SK_ID_BUREAU"].unique().tolist()

# -----------------------------------------------
# Bureau Balance
# -----------------------------------------------
bureau_b = pd.read_csv("project_data/bureau_balance.csv")
bureau_b_id = bureau_b["SK_ID_BUREAU"].unique().tolist()

bureau_b.loc[bureau_b["SK_ID_BUREAU"] == bureau_b_id[2]]
    
bureau_b[0: 40]

#===========================================================================
# Question: I want to know how many previous loan does each application has
# DataSet: train, bureau
# Variales: train["SK_ID_CURR"], bureau["SK_ID_BUREAU", "SK_ID_CURR"] 

curr_bureau_id = bureau["SK_ID_CURR"].unique().tolist()
bureau_id = bureau["SK_ID_BUREAU"].unique().tolist()

# Not every applicant has previous loan record in credit bureau, assume those
# people has 0 previous loan
false = 0
for i in curr_id:
    if i in curr_bureau_id:
        false = false
    else:
        false = false + 1
# 1443 don't have previous loan record in credit bureau


train['NUM_PREVIOUS_CB'] = ""
for i in curr_id:
    if i  in curr_bureau_id:
        train.loc[train["SK_ID_CURR"] == i, 'NUM_PREVIOUS_CB'] = \
            len(bureau.loc[bureau["SK_ID_CURR"]== i]["SK_ID_BUREAU"].unique())
    else:
        train.loc[train["SK_ID_CURR"] == i, 'NUM_PREVIOUS_CB'] = 0

# Density plot
max(train["NUM_PREVIOUS_CB"]) # 47
plt.hist(x = train["NUM_PREVIOUS_CB"], bins = 'stone', density = True)
plt.title("Density of number of previous loan \n \
          in credit bureau's record")
plt.xlabel("Number of previous insurance")
plt.ylabel("Density")


#===========================================================================
# Question 2: Distribution of target variable.

good = train[train['TARGET' ]== 0].shape[0]
default = train[train['TARGET' ]== 1].shape[0]
total = 10000
 # 9238 good applicant, 762 default
sizes = [good/total, default/total]
labels = ['Good', 'Default']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')

#==========================================================================

#

    



