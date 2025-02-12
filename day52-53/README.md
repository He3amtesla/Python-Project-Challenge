Here's the English translation formatted in Markdown:

# Day 52 - 53 of 66-Day Python Project Challenge 📅

## Today's Learning Topic: Monty Hall Problem Simulation Project

### Description:
Yesterday and today I worked on the "Monty Hall Problem Simulation" project. It's an interesting project with a paradox - you might think there's a 50% chance of being correct, but it's actually about 66% to 34%. If you change the door you initially selected, there's a higher probability of winning the car from that door.

Project link: https://lnkd.in/e-aDrGHY

### Key Learning Points:
"
**Timeit** ⏱
**UnderscoreConvention** 🔸
**RandomShuffle** 🎲
**ListDeletion** 🗑️
**StreamlitInput** 🔢
**LineChart** 📈
**Subheader** 📝
**SleepFunction** 😴
"

### What I Learned:

#### timeit
The timeit function takes a parameter-less function, and to convert a function with parameters into one without parameters, we can use an anonymous lambda function!
For example:
`lambda: monty_hell_game(True)`
is the same as:
```python
def wrapper():
    return monty_hell_game(True)
```
Additionally, Jupyter Notebook has magic commands that are very useful. One of them is %timeit which checks the memory usage* and code execution time.

The `_` symbol in Python programming means we use that symbol for variables we don't need in loops.

timeit memory usage*

The shuffle method in the random library shuffles the values in a list and only works with lists.
- The shuffle method is applied directly to the list and its output is None!

- The del method deletes based on index while the remove method deletes based on value (value name) in the list.

```python
number_input = st.number_input("Enter Number for simulate",
        min_value=1, max_value=1000000,
        value=100
        )
```
In the above code, number_input opens a box for value and asks the user for a number with the parameters it needs. The first parameter is string, then... (it's clear in the code!)

```python
chart1 = st.line_chart(x=None, y=None)
```
Opens a line chart with null values
and code
```python
chart1.add_rows([win_without_switch / (i + 1)])
```
Adds a point to chart1 which is a line chart (x value automatically increases by 1 unit and y value is the point (note) that we add to chart1). Each time a new value is added, the x index increases by one and the value is stored in y.

```python
streamlit.subheader("This method creates a subheading that is smaller than the title")
```

```python
import time
time.sleep(.05) #if placed in a loop, we can use this method to make the program sleep based on seconds each time the loop runs
```

### Tomorrow's Plan:
Review previous lesson reviews and review the past 7 lessons.
