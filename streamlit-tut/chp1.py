import streamlit as st

st.title("This is streamlit")
st.subheader("Welcome on streamlit!!")
st.write("Choose any one programming language")
favlang = st.selectbox("Languages: ",["Java","C","C++","Python","Rust","JS"])
st.write(f"You choose {favlang}. Excellent choice!")
st.success("You have choosen the lang.")