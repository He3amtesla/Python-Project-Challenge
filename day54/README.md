# Day 54 of 66-Day Python Challenge 📅
## Today's Learning Topic: **Contact Book Implementation Project**
Description: 
Today, I finally completed this project after a long time. This project is like the contact saves on the phone, you can add contacts, update the desired contact, even delete or see the entire list of your saved contacts.

### What I've learned:
`from collections import defaultdict`
This library, if a key doesn't exist, it automatically opens it when we give a value to that key and assigns a value instead of giving an error and generally produces a dictionary and if we define a numeric value inside its method, it sets a numeric value, and if we define a list, it sets a list, and so on...
We can access inside the dictionary like this:
```
diccct = {
    "ali": {
        "phone": "09141190804",
        "email": "hesam@gmail.com"
    },
    "divid": {
        "phone": "09141198804",
        "email": "am@gmail.com"
    }
}
```
```python
diccct["ali"]["phone"]#output ->09141190804
```