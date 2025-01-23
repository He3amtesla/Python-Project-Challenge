## Day 38 of the 66-Day Python Project Challenge 📅  
**Today's Learning Title:** Intro to Streamlit Dashboard Project and Intro to Streamlit  

### **Explanation:**  

```bash
pip install streamlit
```

With this command, all the dependencies of Streamlit and Streamlit itself will be installed.  
Streamlit, like Jupyter Notebook and Lute, creates a local host from your system to display a graphical interface. When we make changes to our code, it can instantly reflect and display them (of course, we need to keep it running).  

Streamlit is pure python.
Using streamlit, we can create a web application.

```python
import streamlit as st

st.write("helloo")

if st.toggle("ON/OFF"):
    st.write("Hi I am ON")
```

To execute the code written using the Streamlit library, you need to run it like this:  
```bash
streamlit run <name_module.py>
```
#### code:
```python
import streamlit as st

st.write("helloo")

if st.toggle("ON/OFF"):
    st.write("Hi I am ON")
```
![GUI Environment streamlit](https://s8.uupload.ir/files/screenshot_2025-01-23_232623_ugdj.png)
