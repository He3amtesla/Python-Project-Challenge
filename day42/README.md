Here's the direct English translation formatted in Markdown:

# Day 42 of 66-Day Python Project Challenge 📅

**Today's Learning Topic:** My Project

## **Description:**

Today I worked on my project and reviewed the lessons from the past 7 days (I don't look at the main codes, I review whatever I learned in the code that day).

I don't want to work on the graphic password generator project right now, currently my own project is a priority for me.

## **What I've Learned:**

if "previous_selections" not in st.session_state:
    st.session_state.previous_selections = [] # Creates a variable with empty list value (variable name previous_selections) inside streamlit's session_state method

A variable is initialized if it's called for the first time

```python
for removed_lesson in removed_lessons:
    st.session_state.selected_data = st.session_state.selected_data[
      st.session_state.selected_data['نام '] != removed_lesson
    ]
```

Inside the bracket, if the boolean value is True that data is kept, if False that row of the framework is removed

```Python
removeds = set(st.session_state.previous_selections) - set(selections_snts)
```
To better understand this code, I'll give a simple example:
f{1,2,3,4,5}-{4,5,6} --> {1,2}

Streamlit refreshes the page every time the user performs an operation, to prevent our data from being lost we use the
streamlit.session_state
method.

```python
Selected= st.radio(
        f"Select item {option}:",
        filtered_ters['ا'].drop_duplicates().tolist(),
        key=option
      )
```

We use key=option in this radio box so that streamlit doesn't encounter an error, why would it encounter an error? Because if we have another radio box of this type, streamlit gets confused