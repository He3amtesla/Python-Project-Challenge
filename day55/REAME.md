# Day 55 of the 66-Day Python Project Challenge 📅  
(2025/3/16)  

## Today's Learning Topic: Introduction to APIs  

### Explanation:  
Today, I reviewed the general concepts of APIs.  

###### What I Learned:  

### RESTful API:  
#### REST Features:  
Past responses are not dependent on current responses, and requests should not be dependent either; in other words, they are **Stateless**.  

### Protocol:  
"A protocol, simply put, is a set of rules and standards that define how communication and data exchange occur between different devices or systems in a network. These rules act like a common language, allowing devices to interact seamlessly, regardless of differences in hardware, software, or operating systems."  

### API Keys:  
If we use an API from a company, every time we send a request, it is sent along with the **API Key**, which helps track our usage of the system.  

### Endpoints and Resources:  
Simply put, if an API is a house, an **endpoint** would be the rooms of that house.  

### Requests:  
Resources can be **JSON, HTML, or text**, and in Python, we can work with requests and resources using the `requests` library.  

### Status Codes:  
Status codes indicate the status of the responses we receive from the server.  

Different response types based on server replies:  
- **1XX:** The server is accepting and processing your request.  
- **2XX:** The information was successfully received.  
- **3XX:** The request was successfully received, but further action is required (redirecting to another address).  
- **4XX:** The request was not completed due to an incorrect URL or possibly because the URL is blocked.  
- **5XX:** Server-side errors—the request was received, but the server couldn't process it.  

```python
import requests
response.status_code  # To retrieve the status code in Python
```

### HTTP Headers:  
Simply put, **headers** contain additional information such as `application/json`, which is attached to the request or response. They accompany the main data to provide extra details.  

### Response Formats:  
A response can take different forms:  
For example:  
```python
response.text
response.json
```

### HTTP Methods and Query Parameters:  
#### HTTP Methods:  
Requests sent to the server can take different forms, such as:  
- **DELETE** | Deletes data.  
- **GET** | Retrieves data.  
- **PATCH** | Updates part of a previous record (modifies specific fields).  
- **POST** | Adds a new record (inserts new data).  
- **PUT** | Updates an entire previous record.  

#### Query Parameters:  
![](https://s6.uupload.ir/files/screenshot_2025-04-01_154939_x5tm.png)

Each `{ }` represents a **record**, and the first record contains attributes like `userId`, etc.  

To filter data, we use **Query Parameters**.  

![](https://s6.uupload.ir/files/screenshot_2025-04-01_155103_4dh7.png)

A **query parameter** typically starts with a **question mark (?)** in the URL:  
`https://lnkd.in/ek5ExsaE`  
It filters and returns responses based on data where `id=2`.  

In Python, this is implemented as follows:  

```python
import requests

url = "https://lnkd.in/eTdqmCmj"
parameter = {"id": 2}
response = requests.get(url, params=parameter)
```