# Day 30 of the 66-Day Python Project Challenge 📅
## Today's Learning Title: Review Month Lesson (Phase 1-2) 📑

### What Did I Do?
Today marks 30 days into the Python Project Challenge (I can’t believe it’s been 30 days!). Every 30 days, a review of the past lessons is conducted to reinforce and solidify knowledge. The review plan includes two phases:
- **Phase 1:** Covers the first half of the lessons for the month.
- **Phase 2:** Covers the second half.

Today, I completed Phase 1 of the review, and alongside it, I edited and added some content to the documentation.

#### Topics Reviewed:
1. VS Code Extensions for Productivity
2. How to Download and Update Source Code from GitHub
3. Introduction to the Number Guesser Game Project
4. Different Ways to Run a Python Project
5. Number Guesser Project - Solution A
6. Number Guesser Project - Solution B
7. Understanding Project Directories in Python
8. Comprehensive Guide to Writing a `README.md` File
9. Comprehensive Guide to Writing a `requirements.txt` File
10. Importance of Good Software Design
11. Single-Responsibility Principle (SRP)
12. Open-Closed Principle (OCP)
13. Liskov Substitution Principle (LSP)
14. Interface Segregation Principle (ISP)
15. Dependency Inversion Principle

---

### Key Additions:
1. **Using `round()` Function**
    ```python
    # Function to round numbers
    round(number, ndigits=None)
    # number: The number you want to round.
    # ndigits: The decimal place you want to round to.
    
    # Example:
    x = 10.25264
    round(x, 2)  # Output --> 10.25
    ```

2. **Scalability in Web Applications**
    - Frameworks provide structured guidelines.
    - **Scalability**: Code becomes more efficient and optimized as the project grows, ensuring it performs seamlessly for a large number of users.

3. **Checking if a String Contains Only Alphabets**
    ```python
    x = "sdf"
    x.isalpha()  # Output --> True
    # This method checks if the string contains only alphabetic characters.
    ```

4. **Setting Python Path in Jupyter Notebooks**
    - Note: Python path addition does not occur in `.ipynb` terminals because Jupyter uses its kernel.
    - Solution: Use the `os` library for path management.

5. **Resizing Images in `README.md`**
    ```html
    <img src="./../Screenshot%202025-01-14%20215825.png" width=200>
    ```
    - Example: Adjust image size in the README. Start the image path with `./`.

6. **Simulating Terminal Commands in Code**
    ```bash
    # Example of simulating terminal commands
    pip freeze > requirements.txt
    ```
    - This command saves all packages in the environment to a `requirements.txt` file. If the file does not exist, it will be created.

