"""
Filename: DataLoader.py

Authors: Charles Pisciotta and Brett Weyer

Date Created: May 29, 2020

This file contains all of the helper functions necessary to load the data.
"""

from csv import reader
from datetime import datetime


# This function takes in a csv and returns a 2-dimensional array of stock market data.
def load_stock_data(filename: str) -> [[]]:

    if not isinstance(filename, str):
        raise TypeError('Filename expected to be type string.')

    assert str(filename).lower().endswith('.csv'), 'File not valid format. Expected `.csv`'

    stock_data = []

    with open(filename, mode='r') as file:

        # Skip header row
        next(file)

        # Read in all lines of stock data
        for line in reader(file):

            # Get day of week from date string
            date_string = line[0]
            day_of_week = datetime.strptime(date_string, "%Y-%m-%d").strftime('%A')

            # Add day of week and string to beginning of list
            line_values = [day_of_week,  date_string]

            # Cast stock numerical values to float and append to line list
            line_values.extend([float(val) for val in line[1:]])

            # Append line values list to 2-d stock data list
            stock_data.append(line_values)

    return stock_data


def zip_columns(listsToZip):
    return list(zip(*listsToZip))
