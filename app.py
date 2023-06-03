import streamlit as st

# Define data
population = 71.6 * 10**6  # Total population

age_distribution = {
    'men': {
        18: 0.0132, 19: 0.0128, 20: 0.0128, 21: 0.0129, 22: 0.0135, 23: 0.0135, 24: 0.0144,
        25: 0.0156, 26: 0.0159, 27: 0.0157, 28: 0.0151, 29: 0.0152, 30: 0.0154, 31: 0.0153,
        32: 0.015, 33: 0.0144, 34: 0.0141, 35: 0.014, 36: 0.0144, 37: 0.0149, 38: 0.015,
        39: 0.0153, 40: 0.0158, 41: 0.0158, 42: 0.0161, 43: 0.016, 44: 0.0154, 45: 0.0161,
        46: 0.0158, 47: 0.0155, 48: 0.0157, 49: 0.0153, 50: 0.0156
    },
    'women': {
        18: 0.0119, 19: 0.0116, 20: 0.0117, 21: 0.0117, 22: 0.0124, 23: 0.0123, 24: 0.0132,
        25: 0.0143, 26: 0.0146, 27: 0.0144, 28: 0.0139, 29: 0.0141, 30: 0.0143, 31: 0.0142,
        32: 0.014, 33: 0.0135, 34: 0.0132, 35: 0.0132, 36: 0.0137, 37: 0.0142, 38: 0.0143,
        39: 0.0147, 40: 0.0152, 41: 0.0153, 42: 0.0156, 43: 0.0156, 44: 0.0152, 45: 0.016,
        46: 0.0158, 47: 0.0155, 48: 0.0159, 49: 0.0156, 50: 0.0161
    },
}

# other data remain the same ...

# Begin Streamlit
st.title("Your Dream Partner Probability Calculator")

# Layout columns
col1, col2 = st.columns(2)

with col1:
    # Inputs
    age_range = st.slider("Age Range", 18, 50, (20, 30))
    min_height = st.slider("Min Height", 140, 240)
    gender = st.radio("Your partner gender", ['men', 'women'])
    car = st.radio("Have private car or not", ['Yes', 'No', 'Any'])
    smoke = st.radio("Smoke", ['Yes', 'No', 'Any'])
    pet = st.radio("Fine to have pet", ['Yes', 'No', 'Any'])

with col2:
    education = st.selectbox("Education Level", list(education_levels.keys()))
    income = st.selectbox("Annual Income (in baht)", list(income_brackets.keys()))
    exercise = st.radio("Exercise regularly", ['Yes', 'No', 'Any'])
    overweight = st.radio("Overweight or not", ['Yes', 'No', 'Any'])
    drink = st.radio("Drink", ['Yes', 'No', 'Any'])

# Button
if st.button('Calculate'):
    # Calculate based on inputs
    age_prob = sum(v for k, v in age_distribution[gender].items() if age_range[0] <= k <= age_range[1])
    education_level = education_levels[education]
    height_mean = height_dist[gender]
    income_bracket = income_brackets[income]
    exercise_mult = exercise_ratio if exercise == 'Yes' else (1 - exercise_ratio if exercise == 'No' else 1)
    overweight_mult = fat_ratio if overweight == 'Yes' else (1 - fat_ratio if overweight == 'No' else 1)
    car_mult = car_ratio if car == 'Yes' else (1 - car_ratio if car == 'No' else 1)
    smoke_mult = smoke_ratio if smoke == 'Yes' else (1 - smoke_ratio if smoke == 'No' else 1)
    drink_mult = drink_ratio if drink == 'Yes' else (1 - drink_ratio if drink == 'No' else 1)
    pet_mult = pet_ratio if pet == 'Yes' else (1 - pet_ratio if pet == 'No' else 1)

    # Calculate height probabilities
    height_prob = 1 - norm.cdf(min_height, loc=height_mean, scale=height_std)

    # Combine all factors
    probability = age_bracket * height_prob * education_level * income_bracket * exercise_mult * overweight_mult * car_mult * smoke_mult * drink_mult * pet_mult

    # Calculate the number of people this represents
    num_people = population * probability

    # Display the results
    st.write(f"Chances you meet your dream partner: {probability*100:.2f}%")
    st.write(f"Number of your dream partners in Thailand: {int(num_people):,}")


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
