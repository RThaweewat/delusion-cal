import streamlit as st
import numpy as np
import scipy.stats as stats


# Define the options
age_groups = {
    '14 years': (0.1605, 5454539, 5151825),
    '15-24 years': (0.1248, 4221749, 4023668),
    '25-54 years': (0.4497, 14712579, 15005961),
    '55-64 years': (0.1344, 4136063, 4748248),
    '65 years and over': (0.1307, 3745685, 4890158)
}

education_levels = {
    'Below bachelor degree': 0.305,
    'Bachelor degree': 0.634,
    'More than bachelor degree': 0.07
}

income_groups = {
    '< 175,000': 0.19,
    '175,001 - 350,000': 0.40,
    '350,001 - 525,000': 0.22,
    '525,001 - 875,000': 0.13,
    '> 875,000': 0.06
}

exercise_habits = {
    'Exercise': 0.261,
    'No exercise': 0.739
}

body_weights = {
    'Fat': 0.472,
    'Not fat': 0.528
}

# Define mean and standard deviation for height
mean_height_woman = 160
mean_height_man = 170
std_dev_height = 5.5  # Assuming standard deviation

st.title('Find Your Dream Partner')

gender = st.selectbox('Gender', ['male', 'female'])

age_group = st.selectbox('Age Group', list(age_groups.keys()))
education_level = st.selectbox('Education Level', list(education_levels.keys()))
income_group = st.selectbox('Income Group', list(income_groups.keys()))
exercise_habit = st.selectbox('Exercise Habit', list(exercise_habits.keys()))
body_weight = st.selectbox('Body Weight', list(body_weights.keys()))
height = st.number_input('Height (in cm)', min_value=100, max_value=250)
total_population = sum(val[1] if gender == 'male' else val[2] for val in age_groups.values())

p_age = age_groups[age_group][0]
p_education = education_levels[education_level]
p_income = income_groups[income_group]
p_exercise = exercise_habits[exercise_habit]
p_body_weight = body_weights[body_weight]

# For height, we use a normal distribution
if gender == 'male':
    p_height = stats.norm(mean_height_man, std_dev_height).pdf(height)
else:
    p_height = stats.norm(mean_height_woman, std_dev_height).pdf(height)

probability = p_age * p_education * p_income * p_exercise * p_body_weight * p_height

# Display the probability
st.write('Probability:', probability)
