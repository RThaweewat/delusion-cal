import streamlit as st
from scipy.stats import norm

# Define data
population = 71.6 * 10**6  # Total population
height_mean = {'men': 170, 'women': 160}
height_std = 5.5

# Define age distribution for men and women
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


education_levels = {
    'Below Bachelor': 0.305,
    'Bachelor': 0.634,
    'Above Bachelor': 0.07,
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
car_ratio = 0.227
smoke_ratio = 0.191
drink_ratio = 0.28
pet_ratio = 0.49
male_vrigin = 14.3
female_virgin = 12.3

# Begin Streamlit
st.title("Dream Partner Probability Calculator")
st.caption("aka Delusion Calculator (TH Edition)")

# Layout columns
col1, col2 = st.columns(2)

with col1:
    # Inputs
    age_range = st.slider("Age Range", 18, 50, (24, 30))
    height_range = st.slider("Height Range (cm)", 140, 240, (170, 180))
    gender = st.radio("Your partner gender", ['men', 'women'], index=0)
    car = st.radio("Have private car or not", ['Yes', 'No', 'Any'], index=2)
    smoke = st.radio("Smoke", ['Yes', 'No', 'Any'], index=2)
    pet = st.radio("Fine to have pet", ['Yes', 'No', 'Any'], index=2)

with col2:
    education = st.selectbox("Education Level", list(education_levels.keys()), index=1)
    income = st.selectbox("Annual Income (in baht)", list(income_brackets.keys()), index=3)
    exercise = st.radio("Exercise regularly", ['Yes', 'No', 'Any'], index=2)
    overweight = st.radio("Overweight or not", ['Yes', 'No', 'Any'], index=2)
    drink = st.radio("Drink", ['Yes', 'No', 'Any'], index=2)
    virgin = st.radio("Still a virgin", ['Yes', 'No', 'Any'], index=2)

# Button
# Button
if st.button('Calculate'):
    # Calculate based on inputs
    age_prob = sum(v for k, v in age_distribution[gender].items() if age_range[0] <= k <= age_range[1])

    # Calculating height probability for range
    height_low_prob = norm.cdf(height_range[0], loc=height_mean[gender], scale=height_std)
    height_high_prob = norm.cdf(height_range[1], loc=height_mean[gender], scale=height_std)
    height_prob = height_high_prob - height_low_prob
    education_level = education_levels[education]
    income_bracket = income_brackets[income]
    exercise_mult = exercise_ratio if exercise == 'Yes' else (1 - exercise_ratio if exercise == 'No' else 1)
    overweight_mult = fat_ratio if overweight == 'Yes' else (1 - fat_ratio if overweight == 'No' else 1)
    car_mult = car_ratio if car == 'Yes' else (1 - car_ratio if car == 'No' else 1)
    smoke_mult = smoke_ratio if smoke == 'Yes' else (1 - smoke_ratio if smoke == 'No' else 1)
    drink_mult = drink_ratio if drink == 'Yes' else (1 - drink_ratio if drink == 'No' else 1)
    pet_mult = pet_ratio if pet == 'Yes' else (1 - pet_ratio if pet == 'No' else 1)

    # Virginity probability
    virginity_probs = {'men': male_vrigin/100, 'women': female_virgin/100}
    if virgin == 'Yes':
        virgin_prob = virginity_probs[gender]
    elif virgin == 'No':
        virgin_prob = 1 - virginity_probs[gender]
    else:  # 'Any'
        virgin_prob = 1

    # Combine all factors
    probability = age_prob * height_prob * education_level * income_bracket * exercise_mult * overweight_mult * car_mult * smoke_mult * drink_mult * pet_mult * virgin_prob

    # Calculate the number of people this represents
    num_people = population * probability

    # Display the results
    # Define color and text styles
    red_bold_text = '<p style="color:#F79327; font-size: 20px; font-weight: bold">'
    small_grey_text = '<p style="color:Grey; font-size: 15px">'

    # Use Streamlit's markdown function to display the styled text
    st.markdown(small_grey_text + 'Chances you meet your partner (Avg. 20 strangers/day)' + '</p>', unsafe_allow_html=True)
    st.markdown(red_bold_text + f'{probability * 100 * 20:.4f}%' + '</p>', unsafe_allow_html=True)
    st.markdown(small_grey_text + 'Total number of partners in Thailand:' + '</p>', unsafe_allow_html=True)
    st.markdown(red_bold_text + f'{int(num_people)}' + '</p>', unsafe_allow_html=True)
