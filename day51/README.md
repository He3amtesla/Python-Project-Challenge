Here's the English translation formatted in Markdown:
# Day 51 of 66-Day Python Challenge 📅

## Today's Learning Topic: Happy Numbers Project

### Description:
After 5 days of rest, today I worked on the Happy Numbers project and placed it on [GitHub](https://github.com/He3amtesla/HappyNumbersChecker).

### What I Learned:

```python

def happy_number(n: int) -> bool:
    numbers = set()
    while (n != 1) and (n not in numbers):
        numbers.add(n) # متدد برای اضافه کردن به اخر ست
        n = sum([int(_)**2 for _ in str(n)])
        #numbers.add(n)
    if n == 1:
        return True
    else:
        return False
    
happy_number(45) #False

#---
[int(_)**2 for _ in str(n)] #[25, 9]

#--
f = ''.join([str(_)if False else str(0) for _ in range(10)]) 
# join فقط میتواند روی رشته ها اعمال شود روی لیست ها از اعداد یا اینتجر نمیتواند اعمال شود
#'0000000000'

#--
sum ([16, 25]) #41
```
