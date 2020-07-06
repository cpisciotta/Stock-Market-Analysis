"""
Filename: Driver.py

Authors: Charles Pisciotta and Brett Weyer

Date Created: June 01, 2020

This file contains all of the functions necessary to complete analysis.
"""

import DataLoader
import matplotlib.pyplot as plt
from datetime import datetime
from Helpers import predict_from_7_day_average_change


def plotStockHistory(dates: [str], first: [float], first_label: str, second: [float], second_label: str):

    # Plot high values
    plt.plot(dates, first, label=first_label)

    # Plot low values
    plt.plot(dates, second, label=second_label)

    # Define labels
    plt.xlabel('Date')
    plt.ylabel('Price (US Dollar)')
    plt.title('S&P Price Values Over Time (2019)')

    # Set x-axis tick mark frequency
    frequency = 10
    date_ticks = [datetime.strptime(day, '%Y-%m-%d').strftime('%b %d') for day in dates[::frequency]]

    plt.xticks(dates, date_ticks, rotation='vertical')
    plt.locator_params(axis='x', nbins=len(date_ticks))

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def plotLineGraphSingleValue(dates: [str], values: [float], label: str, title: str):

    # Plot high values
    plt.plot(dates, values, label=label)
    plt.plot(dates, [0] * len(dates))

    # Define labels
    plt.xlabel('Date')
    plt.ylabel('% Change')
    plt.title(title)

    # Set x-axis tick mark frequency
    frequency = 10
    date_ticks = [datetime.strptime(day, '%Y-%m-%d').strftime('%b %d') for day in dates[::frequency]]

    plt.xticks(dates, date_ticks, rotation='vertical')
    plt.locator_params(axis='x', nbins=len(date_ticks))

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

if __name__ == '__main__':
    values = DataLoader.load_stock_data('S&P 500 2019.csv')
    zipped_values = DataLoader.zip_columns(values)

    plotStockHistory(zipped_values[1], zipped_values[3], "High", zipped_values[4], "Low")
    plotStockHistory(zipped_values[1], zipped_values[2], "Open", zipped_values[5], "Close")

    high_changes = predict_from_7_day_average_change(zipped_values[3])
    low_changes = predict_from_7_day_average_change(zipped_values[4])
    open_changes = predict_from_7_day_average_change(zipped_values[2])
    close_changes = predict_from_7_day_average_change(zipped_values[5])

    plotLineGraphSingleValue(zipped_values[1][1:], high_changes, '% Change', 'Daily High % Changes (2019)')
    plotLineGraphSingleValue(zipped_values[1][1:], low_changes, '% Change', 'Daily Low % Changes (2019)')
    plotLineGraphSingleValue(zipped_values[1][1:], open_changes, '% Change', 'Daily Open % Changes (2019)')
    plotLineGraphSingleValue(zipped_values[1][1:], close_changes, '% Change', 'Daily Close % Changes (2019)')