"""
Filename: Helpers.py

Authors: Charles Pisciotta and Brett Weyer

Date Created: June 02, 2020

This file contains all of the helper functions necessary to complete analysis.
"""


def predict_from_7_day_average_change(values: [float]):

    return [100 * (b - a) / a for a, b in zip(values[::1], values[1::1])]

