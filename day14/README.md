
# Day 14 of the 66-Day Python Project Challenge 📅

## Today's Learning Topic: Single-Responsibility Principle (SRP)

🎯 **What did I do?**

Today, I focused on reviewing and implementing the Single-Responsibility Principle (SRP). This principle emphasizes that each class should have only one responsibility, meaning it should have only one reason to change.

🔑 **What did I learn?**

This principle helps us write cleaner and more maintainable code. Instead of having a class that handles multiple functions, each class should be responsible for a single, specific task. This makes the code more flexible, understandable, and easier to modify.

To explain this better, let's use a simple example. Imagine we have a multi-tool that has both a knife and a saw. While this tool might be useful in some cases, it can't perform better than a dedicated single-purpose knife or saw.

In the code I previously encountered, the `FileManager` class was used for both reading and writing files as well as compressing and extracting files. This design made the code heavily dependent on this class, and changes in one of these functions could affect other parts of the system.

To fix this issue, I rewrote the code and split it into two classes. Now, the `FileManager` class is solely responsible for reading and writing files, and the `Compresser` class is responsible for compressing and extracting files.

### Code Before SRP:

```python
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

### Code After SRP:

```python
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class Compresser:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

✅ **Benefits:**

- The code is now more clearly divided, with each class responsible for only one task.
- This improves readability and makes the code easier to maintain.
- Additionally, if changes are needed for compression or extraction functionality, they will only be made in the `Compresser` class, and the rest of the code will remain unaffected.

#### tomorrow's program:
Tomorrow, I'll dive into the Open-Closed Principle (OCP)
