# import streamlit as st

# st.title("Age Checker App")
# st.subheader("Welcome to age checker app.")
# st.write("Choose your date of birth:")
# dob = st.date_input("Your DOB").year
# if dob:
#     st.write(f"You choose your date of birth {dob}")

# curr_year = st.date_input("Current Date").year
# st.write(f"Current year : {curr_year}")

# st.success(f"Your age is {curr_year - dob}")

import streamlit as st
from datetime import date

st.title("🎂 Age Checker App")
st.subheader("Welcome to the Age Checker App!")

# Date of Birth
dob = st.date_input(
    "Choose your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# Current Date
current_date = st.date_input(
    "Current Date",
    value=date.today()
)

# Calculate Button
if st.button("Calculate Age"):
    age = current_date.year - dob.year

    # Check if birthday has occurred this year
    if (current_date.month, current_date.day) < (dob.month, dob.day):
        age -= 1

    st.success(f"🎉 Your age is **{age} years**")