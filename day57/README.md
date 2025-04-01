## Day 57 of the 66-Day Python Project Challenge 📅  
(2025/3/18)  

### Today's Learning Topic: Consuming APIs With Python  

#### Explanation:  
Today, I explored fetching data from an API.  

###### What I Learned:  
To use an API, we must check its documentation. Some filters are mandatory and should be set in `params`.  

**Example of setting parameters in Python:**  
```python
parameters = {
    "api_key": os.environ["API_KEYS"],
    "limit": 1,
}
```  

**Example of retrieving image-related data from JSON:**  
```python
response.json()["Image"]
```  