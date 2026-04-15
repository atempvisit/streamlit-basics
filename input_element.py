import streamlit as st

st.title("Input Elements")

st.divider()

name = st.text_input("Enter your name")

# st.write("Hello", name)

# print(type(name))

st.divider()

age = st.number_input("Enter your age", value=0, placeholder="Age")

# st.write("Your age is", age)

# print(type(age))

pressed = st.button("Submit", type="primary")

if pressed:
    st.write("Hello", name, "Your age is", age)

st.divider()

password = st.text_input("Enter your password", type="password")

st.write("Password:", password)

# print(type(password))


selected = st.selectbox("Select your profession", ("Developer", "Designer", "Manager", "Other"), index=None, accept_new_options=True)

print(type(selected))

st.write("You selected:", selected)