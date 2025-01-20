### Day 35 of the 66-Day Python Project Challenge 📅
#### Today's Learning Title: Password Generator Project (2-3)
As I promised yesterday, I added the `MemorablePasswordGenerator` class to my project. The way this class works is that it generates passwords with meaningful words and uses a separator to separate those words. For example: `hesam-amin-bank`. The user can also specify the number of words (these settings have default values, but the user can customize them to their preferences).

##### What I Learned:
- The `random.choice` method only takes one argument.
- In Boolean variables, the value `None` is considered as `False`. (None -Value-> NoneType)
- Conditions can be applied in comprehensions.
  Example:
  ```python
  [choice(list_words).upper() if choice([True, False]) else choice(list_words).lower() for _ in range(self.number_of_words)]
  ```

##### `MemorablePasswordGenerator` Class:
```python
list_words = nltk.corpus.words.words()

class MemorablePasswordGenerator(PasswordGenerator):

    def __init__(self, number_of_words: int = 4, separator_symbol: str = '-', capitalize: bool = None):

        self.number_of_words = number_of_words

        self.separator_symbol = separator_symbol

        self.capitalize = capitalize

    def generator(self) -> str:

        if self.capitalize:

            return (self.separator_symbol.join([choice(list_words).upper() for _ in range(self.number_of_words)]))

        if self.capitalize == None:

            # return (self.separator_symbol.join([choice([choice(list_words), choice(list_words).upper()]) for _ in range(self.number_of_words)]))

            return (self.separator_symbol.join([choice(list_words).upper() if choice([True, False]) else choice(list_words).lower() for _ in range(self.number_of_words)]))

        return (self.separator_symbol.join([choice(list_words).lower() for _ in range(self.number_of_words)]))
```

Example usage:
```python
MPG = MemorablePasswordGenerator(number_of_words=5, separator_symbol=',', capitalize=None)
MPG.generator()  # --> 'hint|PARTICIPIAL|infertile|bustling|FRAUDLESSNESS'
```

#### Plan for Tomorrow:
Tomorrow, I plan to complete this initial version of the project, write test cases for it, and publish it publicly on GitHub.
