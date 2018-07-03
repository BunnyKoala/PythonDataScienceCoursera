# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:40:00 2018

@author: zhen.liu
"""
import pandas as pd
import numpy as np

path = 'C:/Users/zhen.liu/Desktop/Data Science Course/assignment 3/'


energy = pd.read_excel(path + 'Energy Indicators.xls', index_col=1, skiprows=17, skip_footer=38, parse_cols = "B:G")
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
energy.dtypes
energy[['Energy Supply', 'Energy Supply per Capita']] = energy[['Energy Supply', 'Energy Supply per Capita']].replace('...', np.NaN)
energy['Energy Supply']= energy['Energy Supply'].astype(float)
energy['Energy Supply per Capita']= energy['Energy Supply per Capita'].astype(float)
energy['Energy Supply'] *= 1000000
energy['Country'] = energy['Country'].replace('...', np.NaN)
energy['Country'] = energy['Country'].replace({'Republic of Korea': 'South Korea','United States of America': 'United States','United Kingdom of Great Britain and Northern Ireland': 'United Kingdom','China, Hong Kong Special Administrative Region': 'Hong Kong'})
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")

energy['Country']


GDP = pd.read_csv(path + 'world_bank.csv', header =4)

GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})

GDP.rename(columns ={'Country Name' :'Country'}, inplace=True)

ScimEn = pd.read_excel(path + 'scimagojr-3.xlsx', header =0)


df_merged = ScimEn.merge(energy, on='Country', how='inner').merge(GDP, on='Country', how='inner')

df_merged = df_merged.set_index('Country')
df_final = df_merged[df_merged['Rank'] < 16]








def answer_one():
    return "ANSWER"
Question 2 (6.6%)
The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

This function should return a single number.



def answer_two():
    return "ANSWER"
Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by answer_one())
Question 3 (6.6%)
What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)

This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.


def answer_three():
    Top15 = answer_one()
    return "ANSWER"
Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

This function should return a single number.


def answer_four():
    Top15 = answer_one()
    return "ANSWER"
Question 5 (6.6%)
What is the mean Energy Supply per Capita?

This function should return a single number.


def answer_five():
    Top15 = answer_one()
    return "ANSWER"
Question 6 (6.6%)
What country has the maximum % Renewable and what is the percentage?

This function should return a tuple with the name of the country and the percentage.


def answer_six():
    Top15 = answer_one()
    return "ANSWER"
Question 7 (6.6%)
Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

This function should return a tuple with the name of the country and the ratio.


def answer_seven():
    Top15 = answer_one()
    return "ANSWER"
Question 8 (6.6%)
Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?

This function should return a single string value.


def answer_eight():
    Top15 = answer_one()
    return "ANSWER"
Question 9 (6.6%)
Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).

This function should return a single number.

(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)


def answer_nine():
    Top15 = answer_one()
    return "ANSWER"

def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])

#plot9() # Be sure to comment out plot9() before submitting the assignment!
Question 10 (6.6%)
Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.


def answer_ten():
    Top15 = answer_one()
    return "ANSWER"
Question 11 (6.6%)
Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']


def answer_eleven():
    Top15 = answer_one()
    return "ANSWER"
Question 12 (6.6%)
Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?

This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.


def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"
Question 13 (6.6%)
Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.

e.g. 317615384.61538464 -> 317,615,384.61538464

This function should return a Series PopEst whose index is the country name and whose values are the population estimate string.


def answer_thirteen():
    Top15 = answer_one()
    return "ANSWER"
Optional
Use the built in function plot_optional() to see an example visualization.


def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);
​
    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
​
    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!