

**Day 45 of the 66-Day Python Project Challenge 📅**

**Today's Learning Title:** my project 3

Today, I reviewed lesson 7 from the past days ([[1- Intro to Streamlit Dashboard Project and Intro to Streamlit]]), and I gathered some information about DataFrames. I understood that DataFrames are two-dimensional arrays, similar to Excel files, and to create a DataFrame, we can use Pandas and other packages (Polars* is a great package for lazy DataFrames, and I found it very interesting as it gives different outputs compared to other DataFrame packages).

**Summary of Today's Key Learnings:**

📊 **DataFrames**

📝 **Creating a DataFrame in Pandas**

❌ **Removing Index in DataFrame Display**

🔄 **Transpose DataFrame**

**What I have learned:**

**Creating a DataFrame with the Pandas library:**

```python
import pandas as pd

students = pd.DataFrame({
    "Name": ["ali", "bahzad"],
    "Age": [12, 14]
})

print(students)
#-output->
  Name    Age
0  ali     12
1 bahzad   14
```

To remove the index column in the display, we can use `.to_string(index=False)`:

```python
# continue the above code
students.to_string(index=False)
print(students)
```

In this code, the output remains unchanged because `students.to_string(index=False)` was not stored in a variable. If we had stored it in a variable, the output would look like this:

```
 Name   Age
 ali    12
bahzad  14
```

The method `to_string()` belongs to Pandas.

The `T` method in Pandas gives the following output:

```python
# continue the above code
print(students.T)
```

This transposes the DataFrame, swapping rows and columns:

```
        0       1
Name    ali   bahzad
Age     12     14
```
Tomrow: I will continue learning about the features of Pandas