# -*- coding: utf-8 -*-
"""
Name: Vessels, Jadyn
Date: 01/21/2024
Course: SDEV 220
Instructor: Francis,Christopher
Assignment: M01 Programming Assignment
"""

seconds = 60
minutes = 60
hours = 24

seconds_per_hour = seconds * minutes
seconds_per_day = seconds_per_hour * hours

float_point = seconds_per_day/seconds_per_hour
int_div = seconds_per_day//seconds_per_hour


print(f"Seconds per hour: {seconds_per_hour}\n")
print(f"Seconds per day: {seconds_per_day}\n")

print (f"Floating-point Division: {float_point}\n")
print (f"Integer Division: {int_div}\n")