import streamlit as st

st.title("Chai Taste Poll")

col1,col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image("https://cdn.shopify.com/s/files/1/0758/6929/0779/files/Masala_Tea_-_Annams_Recipes_Shop_2_480x480.jpg?v=1732347934", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://static.toiimg.com/thumb/87098868.cms?imgsize=108058&width=800&height=800",width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai",["Masala","Adrak"])
st.write(f"Welcome {name} and your {tea} chai is getting.")

with st.expander("Show Chai Making Instructions"):
    st.write(""" 
    1.Boil Water with tea leaves
    2.Add Milk
    3.Add Sugar
    4.Wait until boil
    5.Serve the tea
""")

st.markdown('# Welcome to Chai App')
