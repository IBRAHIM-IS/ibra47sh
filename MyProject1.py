import numpy as np
import pandas as pd
import streamlit as st

st.title("WORK HARD FOR YOUR PROJECT")
st.write("ALL OF YOU ARE REALLY NICE")

data = pd.DataFrame({
    "Name":["Abdullah Al-Qahtani", "Ali", "Ahmed", "Hussain"],
    "mMarks":[95,99,99,100]
})

st.write("Below is a dataframe of student marks")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns = ["A","B","C","D"]
)

st.line_chart(chart_data)