## Day 59 of the 66-Day Python Project Challenge 📅  
(2025/3/24)  

### Today's Learning Topic: Currency Converter Streamlit UI  

###### Explanation:  
Today, I added a UI to the currency converter project using the Streamlit library.  

###### What I Learned:  
```python
l = 2.4234234
print(f"{l:.2f}")  # 2.42  # Displays two decimal places
```  

![[Screenshot 2025-03-24 131229 1.jpg]]  

```python
col1.metric(label="Base Currency", value=f"{total_number:.2f} {base_currency}")
```  

```python
st.success(f"✅Exchange Rate: {convert_amount:.4f}")  # Displays message in a green box
```  

```python
st.error("Error fetching exchange rate.")  # Displays message in a red box
```  

```python
if response.status_code != 200:
    return None
# status_code represents:
# <Response [200]>
# Returns the number inside the list
```  

Project Link: [https://github.com/He3amtesla/Convert_currency](https://github.com/He3amtesla/Convert_currency)  
