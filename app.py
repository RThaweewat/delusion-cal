import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def make_plot(probability):
    fig, ax = plt.subplots(figsize=(8, 8))  # Add a size for the figure to make it larger
    grid = np.zeros((100, 100))  # Adjust the grid size to 100x100
    num_red_boxes = round(probability * 10000)  # Calculate number of red boxes based on the new grid size
    red_boxes_indices = np.random.choice(10000, num_red_boxes, replace=False)  # Randomly select indices for red boxes

    # Change the color of selected boxes to red
    for index in red_boxes_indices:
        row = index // 100  # Adjust this line for the new grid size
        col = index % 100  # Adjust this line for the new grid size
        grid[row][col] = 1

    # Create a color map: 0 for white boxes and 1 for red boxes
    cmap = plt.cm.colors.ListedColormap(['white', 'red'])
    ax.imshow(grid, cmap=cmap)

    # Hide the grid lines
    ax.grid(False)

    # Hide the axes
    ax.axis('off')

    return fig

def get_age_proportion(age):
    if 18 <= age <= 24:
        return (12.48 / 10) * (24 - age + 1)
    elif 25 <= age <= 50:
        return (44.97 / 30) * (50 - age + 1)
    else:
        return 0

    
total_population = 71600000  # Total population

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
# Age range from 18 to 50 years
# User selects their age
age = st.slider("Select your age", min_value=18, max_value=50)

# Calculate the proportion of the user-selected age
p_age = get_age_proportion(age)

# Then use this p_age in your final probability calculation
# Height range from 140 to 200 cm
height = st.slider("Select your height in cm", min_value=140, max_value=200)
education_level = st.selectbox('Education Level', list(education_levels.keys()))
income_group = st.selectbox('Income Group', list(income_groups.keys()))
exercise_habit = st.selectbox('Exercise Habit', list(exercise_habits.keys()))
body_weight = st.selectbox('Body Weight', list(body_weights.keys()))
total_population = sum(val[1] if gender == 'male' else val[2] for val in age_groups.values())

p_education = education_levels[education_level]
p_income = income_groups[income_group]
p_exercise = exercise_habits[exercise_habit]
p_body_weight = body_weights[body_weight]

# For height, we use a normal distribution
if gender == 'male':
    p_height = stats.norm(mean_height_man, std_dev_height).pdf(height)
else:
    p_height = stats.norm(mean_height_woman, std_dev_height).pdf(height)
    
# Retrieve the population size of the selected age group
population_size = age_groups[age_group][1] if gender == 'male' else age_groups[age_group][2]

# Adjust the probability calculation
probability = p_age * p_education * p_income * p_exercise * p_body_weight * p_height

# Display the probability
st.write('Probability:', round(probability, 4))
perfect_partners = round(probability * total_population)
st.write('Estimated number of perfect partners:', perfect_partners)

# Call the function with the calculated probability
fig = make_plot(probability)
st.pyplot(fig)
