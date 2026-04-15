import streamlit as st

st.title("My first Streamlit app", anchor = False)

st.write("Hello World")

st.header("Content 1", divider = True)

st.subheader("Sub content 1")

st.text("This is a text")

st.markdown("*This* is a :red[**markdown**] text")

st.markdown(":orange-background[*This* is a :red[**markdown**] text] :world_map:")

a = 10
b = 20
st.write("The sum of a and b is", a + b)