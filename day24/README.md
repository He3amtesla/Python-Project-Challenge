
### Day 2 of the 66-Day Python Project Challenge 📅
**Today's Learning Topic:** Implementing the Rock, Paper, Scissors Game 🎮

---

### What Did I Do?

Today, I wrote a simple Rock, Paper, Scissors game project and learned interesting concepts about user input handling and how methods are stored in variables. The program is designed so that the user can exit the game by entering `q` or `Q`. Tomorrow, I plan to improve this game further.

---

### Key Learnings 🔑

#### User Input and Validation:
In the following code:

```python
if input() in ('q', 'Q'):
    break
```

We check if the user enters `q` or `Q` to exit the loop. However, in this code:

```python
if input() in ('q' or 'Q'):
    break
```

The code results in an error because the Python interpreter first evaluates `('q' or 'Q')` as `True` (since non-empty strings are always `True`). As a result, the condition does not work correctly.

The purpose of this code snippet was to allow the user to quit the game by entering `q` or `Q`.

---

#### Difference Between Using Parentheses and Not Using Them for Methods:
In this code:

```python
computer_choice = self.get_computer_choice()
```

The method `get_computer_choice()` is executed, and its result is stored in the variable `computer_choice`. However, in this code:

```python
computer_choice = self.get_computer_choice
```

The variable `computer_choice` acts as a pointer to the method `get_computer_choice`. This means the method can later be invoked using `computer_choice()`.

Simply put, in the second case, the variable holds the method itself instead of the method's result.

---

#### Overwriting Mode:
In a keyboard, the **OVR** mode stands for "overwrite mode," where new text replaces the old text. This mode can be toggled using the `INS` key. By default, the **Insert Mode** is active, which allows adding new text without deleting the existing text.


### Link Game Project:
https://github.com/He3amtesla/RockPaperScissors-Game/tree/main
---
### Tomorrow's Plan (2025/1/10) 🔮

**Goal:** Improving the Rock, Paper, Scissors Game Project 🎮