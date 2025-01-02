# Day 17 of the 66-Day Python Project Challenge 📅

## Today's Learning Topic: LSP (Liskov Substitution Principle)

### 🎯 What Did I Do? And What Did I Learn?

Today, I learned about the LSP principle. The LSP states that a child class should be written in such a way that it can replace the parent class without affecting the correctness of the program. This means that we should be able to use objects of the child class instead of the parent class without changing the behavior of the program.

### ✅ Benefits:

- Increased substitutability of classes
- Improved code structure and design
- Reduced dependencies and increased flexibility in the code

### Code:

```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

def make_bird_fly(bird):
    bird.fly()

# Usage of LSP
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: "Sparrow can fly"
make_bird_fly(penguin)  # Output: "Penguin cannot fly"
```

This code follows the Liskov Substitution Principle. If we were to change the Penguin class like this:

```python
class Penguin(Bird):
    def fly(self):
        pass
```

It would violate the LSP.

The LSP is essentially a guideline for structuring code in parent-child class relationships.

### 🚀 Tomorrow's Plan (2025/1/2):

Tomorrow, I plan to study the ISP (Interface Segregation Principle) and understand how this principle can help improve code structure.
