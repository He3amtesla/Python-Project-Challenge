## Day 26 of the 66-Day Python Project Challenge 📅

### Today's Learning Title: Documenting Python Code

---

### What did I do?

Today, after finishing the “one step closer to the dream” challenge, I started looking at the topic of “Documenting Python Code.” I learned a lot. Thanks to Mr. Hejazi for explaining this subject in such a simple and very useful way.

These are the titles I looked at today:

- Why documentation is important in the first place
- The difference between commenting and documenting
- How to document our Python code

---

### Today's Learning Topics:

**Why documentation is important in the first place**

- **The difference between commenting and documenting**
- **How to document our Python code**
- **The importance of documentation** (kind of a continuation of the first item)
- **What is the difference between adding comments and documentation?** (explained further after the second item)
- **The `help()` function**
- **What is a docstring?**
- **Types of documentation formats**
- **Changing from outside via the dunder doc method**

---

### What did I learn? 🔑

#### The importance of documentation:

Our code is read more than it is written, both by ourselves and by others.

For me, it has happened many times that after writing my code, when I revisited it a few days later, I couldn’t remember what a certain part of the code did because I hadn’t written any documentation. (Especially in university, where the professor asked for assignments; after submitting, the following week when we showed it, we couldn’t remember how our code worked. Because of that, it seemed like we were getting help from AI… hmm.)

And one of the most important aspects of documentation is that with excellent documentation, we can sell our product. For instance, code that is poorly written but has great documentation will attract customers.

---

#### What is the difference between adding comments and documentation?

In documentation, we mostly explain the purpose of the code, how to use it, the overall goal, why we used this specific algorithm, etc.*

Whereas in commenting, we explain the details of the code, for example, which part of the code does what, the reason for placing this algorithm in the code, marking TODO, and so on.*

_Note: Documentation is usually written outside of the code, for example in script files._

_Note: We should not include useless information in the comments._

---

#### The `help()` function:

The `help()` function explains what a function, class, or data type does. Similar to the `help()` function, there is the dunder doc method (which has some differences from the `help()` function).*

---

#### What is a docstring?

A docstring is a type of attribute that is placed right after the definition (e.g., class definition, class method, or function) and is stored in the `__doc__` attribute.

In a class docstring, we write explanations of the class, for example how the class works, etc.

_Note: Avoid writing extra data; write just enough so that if you don’t include it, the reader might not understand._

In a function or method docstring, we write explanations such as what it does, what its arguments are, what it raises (when it raises an error), the method or function limitations, and side effects.

(Side effects mean changes outside its own scope that a function might perform, for example changing a global variable or anything that isn’t itself.)

---

#### Types of documentation formats:

For example, Google, Sphynx, NumPy, and so on.

There are tools that can automatically generate documentation for functions and classes.

For instance, the well-known tool Sphynx and Auto Documents (these tools include different documentation formats).

---

#### One more use of the dunder doc:

We can change the doc of classes, methods, or functions from outside using the dunder doc method if we have written documentation for them:
```python
class Student:
    """
    dsfdsf
    """
    
    def __init__(self):
        """_summary_
        """
        
Student.__init__.__doc__ = "heloo"
```

---

Tomorrow: I will do commenting and documentation in the Rock, Paper, Scissors project code.
