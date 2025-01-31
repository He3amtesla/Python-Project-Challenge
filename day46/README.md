# Day 46 of 66-day Python Project Challenge 📅
## Today's Learning Topic: my project 4

### Description:
Today I reviewed lesson 7 from the past days and practiced some pandas methods.

### What I learned:
```python
import pandas as pd
students = pd.DataFrame({
    "name": ["Ali", "Reza"],
    "Age": [12, 52]
})
  
students["name"] = students["name"].str.startswith('A')
students
#startswith is only for finding letters in strings, not possible with numerical values.
```
```
   name  Age
0  True   12
1  False  52
```
Series are single columns, combining series forms a DataFrame.
```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)  # accessing value using index
#when we give manual indices to series, we can get their values both with the indices we gave and with their numerical indices
```
```
a    10
b    20
c    30
dtype: int64
```
```python
import pandas as pd
students = pd.DataFrame({
    "name": ["Ali", "Reza"],
    "Age": [12, 52]
})
print(students["Age"]>20)
```
```
0    False
1     True
Name: Age, dtype: bool
```
```python
import pandas as pd
students = pd.DataFrame({
    "name": ["Ali", "Reza"],
    "Age": [12, 52]
})
 
print(students[students["Age"]>20])
#if the answer is true, nothing happens, if the boolean answer is false that row gets deleted.
```
```
   name  Age
1  Reza   52
```

### Tomorrow's Plan:
Solve my program's input file issues and add extra features