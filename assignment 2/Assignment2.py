# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:58:57 2018

@author: zhen.liu
"""

import pandas as pd
import numpy

path = 'C:/Users/zhen.liu/Desktop/Data Science Course/assignment 1/'

df = pd.read_csv(path + 'olympics.csv', index_col=0, skiprows=1)

df.head
for col in df.columns:
    #print (col, len(col))
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)
    #print (col, len(col))

names_ids = df.index.str.split('\s\(') # split the index by '('\s\(
print(names_ids)

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
print (df.index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
print (df['ID'])
df = df.drop('Totals')
df.head()

#Q0 What is the first country in df?
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 

#PART1
#Question 1
#Which country has won the most gold medals in summer games?

def answer_one():
    return df['Gold'].argmax()
answer_one() 

#Question 2
#EWhich country had the biggest difference between their summer and winter gold medal counts?
#EThis function should return a single string value.
def answer_two():
    return  (df['Gold'] - df['Gold.1']).abs().argmax()
answer_two()


#Question 3
#Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
#(Summer Gold−Winter Gold)/Total Gold
#Only include countries that have won at least 1 gold in both summer and winter.
#This function should return a single string value.

def answer_three():
    have_gold = df[(df['Gold']> 0 ) & (df['Gold.1'] > 0)]
    return  ((have_gold['Gold'] - have_gold['Gold.1'])/(have_gold['Gold'] + have_gold['Gold.1'])).abs().argmax()
answer_three()


#Question 4
#Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
#This function should return a Series named Points of length 146
def answer_four():
    points = (df['Gold.2']* 3 + df['Silver.2'] * 2 + df['Bronze.2']*1 )
    return points
answer_four()


#PART2

#Question 5
#Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
census_df = pd.read_csv(path + 'census.csv')
census_df.head()


def answer_five():
    return census_df['STNAME'].value_counts().argmax()

answer_five()
#Question 6
#Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.

def answer_six():
    #df_agg = census_df.groupby(['STNAME','CTYNAME']).agg({'CENSUS2010POP':sum}).head(3)
    no_agg = census_df[census_df['SUMLEV'] > 40]
    df_top3 = no_agg.groupby(['STNAME'])['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
    #df_top3 = no_agg.groupby(['STNAME','CTYNAME'])['CENSUS2010POP'].nlargest(3)
    #grouped = df_agg['CENSUS2010POP'].groupby(level=0, group_keys=False).apply(lambda x : x.nlagest(3))
    return df_top3

answer_six()



#Question 7
#Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#This function should return a single string value.



def answer_seven():
    #df_agg = census_df.groupby(['STNAME','CTYNAME']).agg({'CENSUS2010POP':sum}).head(3)
    no_agg = census_df[census_df['SUMLEV'] > 40]
    col_keep= ['STNAME', 'CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    no_agg_new = no_agg[col_keep]
    changes = (no_agg_new.max(axis=1,) - no_agg_new.min(axis=1)).argmax()
    #changes= changes
    #df_top3 = no_agg.groupby(['STNAME','CTYNAME'])['CENSUS2010POP'].nlargest(3)
    #grouped = df_agg['CENSUS2010POP'].groupby(level=0, group_keys=False).apply(lambda x : x.nlagest(3))
    return census_df.loc[changes]['CTYNAME']

answer_seven()

#Question 8
#In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).


def answer_eight():
    #df_agg = census_df.groupby(['STNAME','CTYNAME']).agg({'CENSUS2010POP':sum}).head(3)
    census_df_new = census_df[(census_df['REGION'] <=2 )  &  (census_df['CTYNAME'].str.startswith('Washington')) & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'] ) ]
    col_keep= ['STNAME', 'CTYNAME']
    census_df_index = census_df_new[col_keep]
    return census_df_index 

answer_eight()












