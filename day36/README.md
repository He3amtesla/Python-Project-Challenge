# Day 36 of the 66-Day Python Project Challenge 📅

**Today's Learning Title:** Password Generator Project (2.9 -3)

**Explanation:**

Today I wrote test cases for my project and learned some points about test cases that I mention in the **What I Learned** section.

###### **What I Learned:**

I learned that

1. **Using `assert` in Test Cases:**

   ```python
   assert False - in answer --> error
   assert True - in answer -->
   ```

2. **Methods `all` and `any`:**

   The methods `all` and `any` both check the iterable; they have this similarity but work differently.

   - `all`: If a boolean expression is `False`, it returns `False`.
   - `any`: If a boolean expression is `True`, it returns `True`.

3. **Generator Expressions:**

   These types of code:

   ```python
   (charters in string.digits for charters in rndome)
   ```

   are called **Generator Expressions**, and they are lazy, meaning they do not hold memory; each iteration outputs the address of the value (in other words, the code is executed piece by piece). Because of this, they are faster than list comprehensions and use less memory.

### Link Project: https://github.com/He3amtesla/Password-Generator-Project