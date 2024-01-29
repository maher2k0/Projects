import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(
    page_title = "Hello",
    page_icon="👋",
    layout="wide")


st.title("My website")

st.header("Header")
st.subheader("Sub Header")
st.text("text Text text dfposjdf asdpom")


col1, col2, = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")


with col1:
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))

    # Display a chat input widget.
st.chat_input("Say something")

st.text('Stopppp')

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# col1, col2, = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")

# with col1:
#     st.radio("Select one:", [1, 2])