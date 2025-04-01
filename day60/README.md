## Day 60 of the 66-Day Python Project Challenge 📅  
(2025/3/31)  

### Today's Learning Topic: Caching  

##### Explanation:  
A few days ago, I reviewed the topic of caching, and today I revisited it and implemented it in my currency converter project.  

##### What I Learned:  

One way to utilize caching is by importing the `functools` library:  

```python
from functools import cache, lru_cache
```  

```python
@cache  # <--- This decorator stores data in RAM and returns the result instantly instead of recalculating
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```  

```python
@lru_cache(maxsize=100000)  # lru: Least Recently Used
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```  

The `lru_cache` decorator is similar to `cache`, and in fact, `cache` internally uses `lru_cache`. The key difference is that `lru_cache` allows setting a memory limit (e.g., if set to 1000, it will store only the most recent 1000 values).  

```python
fibonacci.cache_info()
```  

```
CacheInfo(hits=998, misses=1001, maxsize=100000, currsize=1001)
```

- **hits**: The number of times the cache was used.  
- **misses**: The number of times the function had to compute a result because the value wasn’t cached.  
- **maxsize**: The maximum cache size.  
- **currsize**: The current number of items stored in the cache.  

There is another caching method that works based on time and memory limits. To use this, the `cachetools` library must be installed.  

```python
from cachetools import cached, TTLCache
```  

Usage example:  

```python
ttl_cache = TTLCache(maxsize=300, ttl=3 * 60 * 60)  # Time in seconds
```  

To use it, apply the decorator before the function:  

```python
@cached(ttl_cache)
```  
Project Link: https://github.com/He3amtesla/Convert_currency