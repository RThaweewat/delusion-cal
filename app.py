import streamlit as st
import numpy as np
import pandas as pd

# Define the statistical data
age_data = {'14 years or younger': 0.1605, '15-24 years': 0.1248, '25-54 years': 0.4497, '55-64 years': 0.1344, '65 years or older': 0.1307}
education_data = {'Below Bachelor Degree': 0.305, 'Bachelor Degree': 0.634, 'More than Bachelor Degree': 0.07}
height_data = {'Mean Women Height': 160, 'Mean Men Height': 170}
income_data = {'Less than 175,000 THB': 0.19, '175,001 - 350,000 THB': 0.4, '350,001 - 525,000 THB': 0.22, '525,001 - 875,000 THB': 0.13, 'More than 875,000 THB': 0.06}
exercise_data = {'Exercise': 0.261, 'No Exercise': 0.739}
fat_data = {'Fat': 0.472, 'Not Fat': 0.528}

# Define the Streamlit app
def app():
    st.title('Dream Partner Probability Calculator')
    st.write('Please select the following options to calculate the probability of finding your dream partner.')
    
    # Age selection
    age = st.selectbox('Select your age range:', list(age_data.keys()))
    
    # Education selection
    education = st.selectbox('Select your education level:', list(education_data.keys()))
    
    # Height selection
    height = st.slider('Select your height (cm):', min_value=140, max_value=200, step=1)
    
    # Income selection
    income = st.selectbox('Select your annual income (THB):', list(income_data.keys()))
    
    # Exercise selection
    exercise = st.radio('Do you exercise regularly?', list(exercise_data.keys()))
    
    # Fat selection
    fat = st.radio('Are you overweight?', list(fat_data.keys()))
    
    # Calculate the probability
    probability = age_data[age] * education_data[education] * np.exp(-((height-height_data['Mean Men Height'])**2)/(2*10**2)) * income_data[income] * exercise_data[exercise] * fat_data[fat]
    
    # Display the result
    st.write('The probability of finding your dream partner is:', round(probability*100, 2), '%')

    if __name__ == '__main__':
        app()
