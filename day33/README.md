# Day 33 of the 66-Day Python Challenge 📅
**Today's Learning Topic:** Intro to Password Generator Project (1-3)

### Description:
This morning, from around 7:15 to 10:35, I worked on the "Intro to Password Generator Project" and completed half of the project. In this project, I defined a parent abstract class and three child classes. Each of the three classes generates random passwords, but with different functionalities.

### Practice Code:
```python
from random import choice
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    @abstractmethod    
    def generator(self):
        pass  


class PinPasswordGenerator(PasswordGenerator):
    def __init__(self, length_numbers: str):  # Where the object is created.
        self.length_numbers = length_numbers
        
    def generator(self) -> str:
        return ''.join([choice(string.digits) for _ in range(self.length_numbers)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length_numbers: int, upper: bool = False, lower: bool = False):  # Where the object is created.
        self.length_numbers = length_numbers
        
        if upper:
            self.ascii_letters = string.ascii_letters.upper()
            self.punctuation = string.punctuation.upper()

        elif lower:
            self.ascii_letters = string.ascii_letters.lower()
            self.punctuation = string.punctuation.lower()
            
        else:
            self.ascii_letters = string.ascii_letters
            self.punctuation = string.punctuation

    def generator(self) -> str:
        print(''.join([choice(string.digits + self.ascii_letters + self.punctuation) for _ in range(self.length_numbers)]))


class RandomPasswordGenerator2(PasswordGenerator):
    def __init__(self, length_numbers: int, in_clude_numbers: bool = False, in_clude_symbol: bool = False):  # Where the object is created.
        self.length_numbers = length_numbers
        self.charctors = string.ascii_letters
        
        if in_clude_numbers:
            self.charctors += string.digits

        if in_clude_symbol:
            self.charctors += string.punctuation

    def generator(self) -> str:
        return ''.join([choice(self.charctors) for _ in range(self.length_numbers)])
```

### Examples:
```python
RPG2 = RandomPasswordGenerator2(length_numbers=55, in_clude_symbol=True, in_clude_numbers=True)
RPG2.generator()  # -> "KEf^&dT0:>QZ?=+`x}rO+_t$gY#uyd%&NXe$EkY0)0bC|uE/T'30Ad!"
```

```python
randompass = RandomPasswordGenerator(10)
randompass.generator()  # -> 26wP_lPzV\
```

```python
pincode = PinPasswordGenerator(length_numbers=10)
pincode.generator()  # -> '2393446169'
```

### What I Learned:
```python
from random import choice
list_numbers = "0123456789"  # Note: A list of characters is represented as a string.
print(choice(list_numbers))  # --> 3
```

```python
import string
''.join([choice(string.digits) for _ in range(8)])
# --> '32982920'
```

```python
import string
print('\n'.join([choice(string.digits) for _ in range(8)]))
# -->
# 7
# 1
# 4
# 2
# 3
# 5
# 6
# 0
```

```python
for i in range(8):
    print(i)
# -->
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
```

```python
lines = ['Line 1', 'Line 2', 'Line 3']
result = '\n'.join(lines)
print(result)
# -->
# Line 1 
# Line 2 
# Line 3
```

```python
import string

string.ascii_letters  # --> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.punctuation    # --> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

```python
''.join([choice(string.digits + "" + "") for _ in range(8)])
# --> '14903340'
```

#### Notes:
- **Deprecated:** When a method from a library is marked as deprecated (e.g., with a strikethrough), it means the method is outdated. You can still use it, but it might be removed in future library versions. This warning is shown to developers to encourage the use of alternatives.

- **Abstract Classes:** Classes that use the `@abstractmethod` decorator cannot be instantiated (i.e., you cannot create objects from them).

- **`__init__`:** This is where the object is created, and behaviors are defined.

- **Python Argument Rules:** Positional arguments must be provided first, followed by keyword arguments. You must either use all positional arguments or all keyword arguments for a given method.

### Tomorrow Plan:
Tomorrow I plan to add MemorablePasswordGeneration class in my project.
