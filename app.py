import streamlit as st
import numpy as np
import pandas as pd

# Define data
population = 71.6 * 10**6  # Total population

age_brackets = {
    '14-24': 0.1405,
    '25-54': 0.4497,
    '55-64': 0.1344,
    '65+': 0.1307,
}
education_levels = {
    'Below Bachelor': 0.305,
    'Bachelor': 0.634,
    'Above Bachelor': 0.07,
}
height_dist = {
    'women': 160,
    'men': 170,
}
income_brackets = {
    '<175k': 0.19,
    '175k-350k': 0.40,
    '350k-525k': 0.22,
    '525k-875k': 0.13,
    '>875k': 0.06,
}
exercise_ratio = 0.261
fat_ratio = 0.472

# Begin Streamlit
st.title("Your Dream Partner Probability Calculator")

# Inputs
age = st.slider("Age", 18, 50)
height = st.slider("Height", 140, 240)
gender = st.radio("Your partner gender", ['men', 'women'])
exercise = st.radio("Exercise regularly", ['Yes', 'No'])
overweight = st.radio("Overweight or not", ['Yes', 'No'])

# Calculate based on inputs
age_bracket = next((value for key, value in age_brackets.items() if str(age) in key), 0)
education_level = education_levels['Bachelor']  # example
height_mean = height_dist[gender]
income_bracket = income_brackets['175k-350k']  # example
exercise_mult = exercise_ratio if exercise == 'Yes' else 1 - exercise_ratio
overweight_mult = fat_ratio if overweight == 'Yes' else 1 - fat_ratio

# Combine all factors
probability = age_bracket * education_level * income_bracket * exercise_mult * overweight_mult

# Calculate the number of people this represents
num_people = population * probability

# Display the results
st.write(f"Chances you meet your dream partner: {probability*100:.2f}%")
st.write(f"Number of your dream partners in Thailand: {num_people:.0f}")
