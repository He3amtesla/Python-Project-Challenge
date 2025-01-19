### Day 34 of the 66-Day Python Challenge 📅
#### Today's Learning Title: 3- Password Generator Project (1.1 - 3)

---

### Explanation:
Today was quite an unusual day—it’s my birthday, and I hadn't slept last night. I ended up sleeping twice, from around 12 PM to 6 PM. Last night, I was busy cleaning up the data of the university's offered classes to choose good professors and convenient times for registration. Anyway, moving on. Today, I continued working on the Password Generator project (still incomplete). In one of the project classes, we needed the NLTK library database to generate meaningful passwords by combining words from the database.

---

### What I Learned:
The **NLTK library** is one of the well-known tools for Natural Language Processing (NLP). It has a vast database, and in this project, we used the words available in its database to extract meaningful words for password generation. While NLTK has many applications, we focused on the part relevant to this project.

---

### How to Use:
To install:
```bash
pip install nltk
```

```python
import nltk

# Downloading the NLTK words database (only needed once; the file is saved locally afterward)
nltk.download("words") 
list_words = nltk.corpus.words.words()  # Loading all words into the list_words variable
print(len(list_words))  # --> 236736
```

---

### Tomorrow's Plan:
Tomorrow, I plan to add the `MemorablePasswordGeneration` class (which I intended to work on today but couldn’t due to unforeseen events).
