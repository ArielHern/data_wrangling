import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# contained all the car information
filename = 'imports-85.data'

# cars are missing headers
headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-type', 'drive-wheels', 'engine-location', 'wheel-base',
           'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinder', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio',
           'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

df = pd.read_csv(filename, names=headers)


# convert ? to numpy nan
df.replace('?', np.nan, inplace=True)


def cal_mean(column_name, data_type='float', axis_type=0):
    """Calculate mean"""
    average = df[column_name].astype(data_type).mean(axis=axis_type)
    return average


def replace(column_name, average):
    """replece NaN using mean"""
    df[column_name].replace(np.nan, average, inplace=True)


def change_data_format(new_type, *column_name):
    """convert data types into a proper format for each column using the "astype()" method"""
    df[[*column_name]] = df[[*column_name]].astype(new_type)


# normalized-losses: 41 missing data, replace them with mean
replace('normalized-losses', cal_mean('normalized-losses'))

# stroke: 4 missing data, replace them with mean
replace('stroke', cal_mean('stroke'))

# bore: 4 missing data, replace them with mean
replace('bore', cal_mean('bore'))

# horsepower: 2 missing data, replace them with mean
replace('horsepower', cal_mean('horsepower'))

# peak-rpm: 2 missing data, replace them with mean
replace('peak-rpm', cal_mean('peak-rpm'))

# calculate the most common type
df['num-of-doors'].value_counts()
df['num-of-doors'].value_counts().idxmax()

replace('num-of-doors', 'four')

# drop row without price tag
df.dropna(subset=['price'], axis=0, inplace=True)

# reset index, because we two rows were dropped
df.reset_index(drop=True, inplace=True)

# print(df.head(20))

# checking and making sure that all data is in the correct format (int, float, text or other).
# check data type
# print(df.dtypes)

# change data type using a function
# bore, stoke, price, peak-rmp  = float
change_data_format('float', 'bore', 'stroke', 'price', 'peak-rpm')

# normalized-losses, hosepower = int
change_data_format(int, 'normalized-losses', 'horsepower')

# check data type with update formats
# print(df.dtypes)

# horsepower coloumn value count
df['horsepower'].value_counts()

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)

group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)

print(df["horsepower-binned"].value_counts())

plt.bar(group_names, df["horsepower-binned"].value_counts())
# plt.show()

# Indicator variable (or dummy variable) for fuel
dummy_fuel_variable = pd.get_dummies(df["fuel-type"])
print(dummy_fuel_variable.head())

# change column names to clafify
dummy_fuel_variable.rename(columns={'gas': 'fuel-type-gas', 'diesel': 'fuel-type-diasel'}, inplace=True)
print(dummy_fuel_variable.head())

# merge data frame "df" and "dummy_fuel_variable"
df = pd.concat([df, dummy_fuel_variable], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis=1, inplace=True)

print(df.head())

df.to_csv('clean_df.csv')
