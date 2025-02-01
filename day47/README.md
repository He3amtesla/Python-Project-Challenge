# Day 47 of the 66-Day Python Challenge 📅  
## **Today's Learning Topic:** my project 5

### **Description:**  
Today, I added the ability to predict non-matching columns with equal content to the "Smart Curriculum Builder" program. Now, if the website changes the name of a column, it can predict it to some extent, and the program will still work.  
Additionally, I did a quick review of the lesson from 7 days ago. [[Day 2]]

###### What I Learned:

First, this snippet of code was added to the program:  
```python
st.write(f"Number of Excel columns: `{len(data.columns)}`")

counter = len(data.columns)-1  # This method is used to find the number of columns in an Excel file.
i = 0

st.write (data.columns[i])  # This gives the name of the column by indexing the columns method on the dataframe.

while i<=counter:
    name_colum = data.columns[i]
    name_colum = name_colum.split()

    for word in name_colum:
        if word == "استاد":
            data["استاد"] = data[data.columns[i]]  # We need to pay attention to this point.

        elif word == "زمانبندی":
            data["زمانبندي تشکيل کلاس"] = data[data.columns[i]]  # Extracts the name of the column and then assigns the content to the "زمانبندي تشکيل کلاس" column or creates a column with this name (depends on whether it already exists or not).

        elif word == "نام درس":
            data["نام درس"] = data[data.columns[i]]

    i = i + 1
```
I used proper naming conventions to avoid issues when coding.

**Program for Tomorrow:**  
I will be focusing on the topic "Python Bootcamp - Project Ideas" by Mr. Ali Hejazi.