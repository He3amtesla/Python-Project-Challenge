# Day 41 of 66-Day Python Challenge 📅

## **Title of Today's Learning: Streamlit Dashboard Implementation (1-2)**

### Description:
Today:
- Worked on my project, practiced some codes I previously used AI assistance with to learn
- Watched Streamlit Dashboard Implementation video diary-style, planning to implement in Password Generator project tomorrow
- Reviewed lessons from the past 7 days

Key Learning Keywords:
- 🧑‍💻 Data management in Streamlit with st.session_state
- 🔍 Checking variable existence in st.session_state
- 📊 Creating empty DataFrame with pd.DataFrame and columns
- ❌ Removing duplicate rows with drop_duplicates()
- 🔠 Sorting data with sort_values() in pandas

### What I Learned in My Project:
This code snippet
```python
if "selected_data" not in st.session_state:
    st.session_state.selected_data = pd.DataFrame(columns=data.columns)
```
took me a while to learn.

How it works:
```
if "selected_data" not in st.session_state:
# If no variable named selected_data exists in Streamlit's session_state:
```

```
    st.session_state.selected_data = pd.DataFrame(columns=data.columns)
    #
```
Copies column names from the file to the columns variable (only column names) and creates a DataFrame, sending it to st.session_state.selected_data

and:
```python
pd.DataFrame(columns = ["cton1", "ston2"], index = [1, 2])
```
```bash
 cton1 ston2
1  NaN  NaN
2  NaN  NaN
```
To add values, we use pandas' loc* feature,
star:

and:

drop_duplicates()
`drop_duplicates() method arguments *`

A pandas method that removes duplicate rows, keeping the row from which duplicate rows were created.

and:
sort_values()*
A pandas method that sorts strings alphabetically.
series*
DataFrame*