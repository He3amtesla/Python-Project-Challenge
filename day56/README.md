## Day 56 of the 66-Day Python Project Challenge 📅  
(2025/3/17)  

### Today's Learning Topic: Environment Variable  

#### Explanation:  
Today, I watched the "Environment Variable" video and learned that we can use this environment for API security or similar purposes.  

#### What I Learned:  
We can store sensitive information on our machine using environment variables. This enhances security by keeping credentials like emails, passwords, and API keys outside our Python code.  
Here’s how we set environment variables in different environments:  

### __Setting in Linux__  
```bash
export VARIABLE_NAME="h234"
```  

### __Setting in Jupyter Notebook__  
```python
%env VARIABLE_NAME = h234  # It automatically treats the value as a string
```  

### __Setting in Python__  
```python
import os

os.environ["VARIABLE_NAME"] = "h234"
```  

### __Viewing the Value__  

#### __Linux:__  
```bash
echo $VARIABLE_NAME
```  

#### __Jupyter Notebook:__  
```python
%env VARIABLE_NAME
```  

#### __Python:__  
```python
os.environ["VARIABLE_NAME"]
os.environ.get("VARIABLE_NAME")
```  

### __Removing the Variable__  

#### __Linux:__  
```bash
unset VARIABLE_NAME
```  

#### __Python:__  
```python
del os.environ["VARIABLE_NAME"]
```  

#### __Jupyter Notebook:__  
It's better to use the `os` library for removal.  

---

### ###### English Words:  
- **Session** → جلسه  
- **Percent** → درصد  
- **Constant** → پایدار، دائمی  
- **Provider** → ارائه دهنده  
- **Instance** → نمونه، مثال، مورد  