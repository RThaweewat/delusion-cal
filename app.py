import streamlit as st
from scipy.stats import norm

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
height_std = 5.5
income_brackets = {
    '<175k': 0.19,
    '175k-350k': 0.40,
    '350k-525k': 0.22,
    '525k-875k': 0.13,
    '>875k': 0.06,
}
exercise_ratio = 0.261
fat_ratio = 0.472
car_ratio = 0.227

# Begin Streamlit
st.title("Your Dream Partner Probability Calculator")

# Layout columns
col1, col2 = st.columns(2)

with col1:
    # Inputs
    age = st.slider("Age", 18, 50)
    height = st.slider("Height", 140, 240)
    gender = st.radio("Your partner gender", ['men', 'women'])
    car = st.radio("Have private car or not", ['Yes', 'No'])
    
with col2:
    education = st.selectbox("Education Level", list(education_levels.keys()))
    income = st.selectbox("Annual Income (in baht)", list(income_brackets.keys()))
    exercise = st.radio("Exercise regularly", ['Yes', 'No'])
    overweight = st.radio("Overweight or not", ['Yes', 'No'])

# Button
if st.button('Calculate'):
    # Calculate based on inputs
    age_bracket = next((value for key, value in age_brackets.items() if int(key.split('-')[0]) <= age <= int(key.split('-')[-1])), 0)
    education_level = education_levels[education]
    height_mean = height_dist[gender]
    income_bracket = income_brackets[income]
    exercise_mult = exercise_ratio if exercise == 'Yes' else 1 - exercise_ratio
    overweight_mult = fat_ratio if overweight == 'Yes' else 1 - fat_ratio
    car_mult = car_ratio if car == 'Yes' else 1 - car_ratio

    # Calculate age and height probabilities
    height_prob = norm.pdf(height, loc=height_mean, scale=height_std) # Use Probability Density Function for height

    # Combine all factors
    probability = age_bracket * height_prob * education_level * income_bracket * exercise_mult * overweight_mult * car_mult

    # Calculate the number of people this represents
    num_people = population * probability

    # Display the results
    st.write(f"overweight_multChances: {overweight_mult*100:.2f}%")
    st.write(f"car_multChances: {car_mult*100:.2f}%")
    st.write(f"income_bracket Chances: {income_bracket*100:.2f}%")
    st.write(f"education Chances: {education_level*100:.2f}%")
    st.write(f"height Chances: {height_prob*100:.2f}%")
    st.write(f"age Chances: {age_bracket*100:.2f}%")
    st.write(f"exercise_mult: {exercise_mult*100:.2f}%")
    st.write(f"Chances you meet your dream partner: {probability*100:.2f}%")
    st.write(f"Number of your dream partners in Thailand: {num_people:.0f}")
