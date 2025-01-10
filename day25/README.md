# Day 25 of the 66-day Python project challenge 📅  
## Today's learning title: Typing and improving the Rock, Paper, Scissors project code

### What did I do?  
Today, I improved the "Rock, Paper, Scissors" project code; now each method is responsible for its own task.  
And I typed the project code (Type hints) using the typing library so that I can perform more accurate typing.

---

## 🛠️ Today's learning topics:

### Typing (Type Hints)
📚 Using the typing library to specify data types and increase code accuracy and readability.  

### Bitwise operators (&, |)
⚙️ The difference in using bitwise operators in boolean and bitwise values and how to use them correctly.  

### Common mistakes in writing conditions
🚧 Analyzing a common mistake in using `or` and providing correct solutions for input comparison.  

### Improving the project code
✨ Optimizing the responsibilities of methods and fixing existing issues in the program logic.

---

## What did I learn? 🔑  
Bitwise operators &, |: These operators are used for bitwise operations, for example:  
```python
a = 5 #101
b = 3 #011
c = a & b
#value c --> 1
```
And also in boolean values:  
True --> 1
False --> 0
I gave the project code I wrote to the AI model, and it pointed out an error in this code:  
```python
 user_win: list[str] = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]
 
        for i in user_win:
            if (user == i[0]) & (computer== i[1]):
                return "congratulations You Win"
```

It said you should use `and` instead of `&` because this type of `&` operator is used for bitwise operations.  
But the code I wrote still executed correctly; do you know why?  
Because the interpreter treats it like a boolean inside parentheses, and if `(user == i[0])` and `(computer == i[1])` are correct, correct means True, and True means 1. A bitwise 1 with a bitwise 1 becomes 1, and the result executes correctly. (It depends on the usage conditions; it’s not only made for bitwise values, we can also use this operator for boolean values.)

### Interpreter behavior in such code
```python
if input() == 'q' or 'Q':
	break
```
The interpreter first takes input from the user, then compares it with `q`. If it is `q`, it exits the loop, but if not, it goes to the `Q` part. However, it doesn’t see `Q` as a character; it sees it as a boolean, meaning if the string is empty, it’s False, but if the string is not empty, it considers it True.  
To allow the user to exit the program if they enter the characters `q` or `Q`, there are several ways to implement this behavior:
```python
if input() in ('q', 'Q'):
	break
```
or  
```python
if input() == 'q' or input() == 'Q':
	break
```
and...

---

## ✅ The benefits of this learning:
- Improving code readability and maintainability  
- Increasing the precision of typing and better understanding of the code by other developers  

---

## 🔗 Project link:
[[https://lnkd.in/eJ_A97mT](https://lnkd.in/eJ_A97mT)
](https://github.com/He3amtesla/RockPaperScissors-Game)
