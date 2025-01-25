### Day 40 of the 66-Day Python Project Challenge 📅

**Today's Learning Topic:** Streamlit Core Concepts

**Explanation:**

Today, I reviewed lessons from the past 7 days and started a project. While working on the project, I am learning the topics, and today, I learned some important concepts of Streamlit.  
(Some things I learned in my project are not included in this post because they were new to me, and I feel I haven't fully grasped them yet.)  
Although these new concepts are fascinating, I feel I need more practice to solidify them in my mind.

###### What I Learned:

```python
import streamlit as st
import numpy as np
import pandas as pd

st.write("This method displays the content on the page")
st.slider("select value", 0, 25, 12.5) 
# This code throws an error because all values must be either float or integer.
# It works by creating a slider that can be moved to select a value.

st.selectbox(
    "What's your favorite teacher?",
    ("Amiri", "Hejazi")
)
# Creates a dropdown box where you can place strings or other data types for selection.

st.radio(
    "What's your favorite teacher?",
    ("Amiri", "Hejazi")
)
# Similar to the previous method but displays radio buttons beside each option.

st.multiselect(
    "What's your favorite teacher?",
    ("Amiri", "Hejazi")
)
# Similar to a selectbox but allows multiple selections.

if st.checkbox("Show dataframe"):
    # Creates a checkbox, and when clicked, the code below executes.
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['a', 'b']
    )
    # Generates random data using NumPy with 20 rows and 2 columns.
    # Column names are defined, and Pandas creates a DataFrame.
    # If the provided data does not match the defined dimensions, it throws an error.

pd.DataFrame({
    "first column": [1, 2, 3],
    "Second column": ["Ali", "Reza", "Mohammad"]
})
# Creates a table (like in Excel) where data can be sorted.
# The number of rows and columns must match the provided data.

column1, column2, column3 = st.columns(3) 
# Creates columns. 
# Purpose: Divides the user interface into sections.

column1.write("column1") # Displays "column1" in the first column.
column2.write("column2")
column3.write("column3")

# Alternatively, this can be done as follows:
# Operations performed in the first column:
with column1: 
    st.write("sdf")
    st.checkbox("sdf")
```
