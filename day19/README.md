
# Day 19 of the 66-Day Python Project Challenge 📅
**Today's Learning Topic:** Dependency Inversion Principle (DIP) 💡

## What I Did
Today, I took a closer look at the Dependency Inversion Principle (DIP) and explored how we can implement it in our code. 

The DIP emphasizes that both high-level and low-level classes should depend on an abstraction (interface or abstract class) rather than each other. Instead of having a high-level class directly depend on low-level classes, an abstract interface should mediate the dependency.

---

## Key Learnings 🔑

### 1. Creating an Abstract Class or Interface
Define an abstract class or interface to act as a bridge between the high-level and low-level classes. This helps decouple dependencies.

### 2. Avoiding Direct Dependency
When the high-level class depends only on an abstract class or interface, rather than multiple low-level classes, the code becomes easier to manage, adapt, and maintain.

### 3. Using `mypy` for Type Checking
With type hints in place, `mypy` can analyze potential issues, improving code quality. Without type annotations, `mypy` defaults to `Any`, which might miss critical errors.

---

### DIP Implementation Example 
```Python
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass


class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class SMSSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # وابستگی به کلاس انتزاعی

    def notify(self, recipient, message):
        self.sender.send_message(recipient, message)

email_sender = EmailSender()
sms_sender = SMSSender()

# ارسال پیام با ایمیل
notification_service = NotificationService(email_sender)
notification_service.notify("user@example.com", "Hello via Email!")

# ارسال پیام با پیامک
notification_service = NotificationService(sms_sender)
notification_service.notify("+989123456789", "Hello via SMS!")

#CODED WRITTEN BY CHATGPT
```


---

## How to Use `mypy` ⚙️
If your code is in a file, say `example.py`, you can run the following command to check types:

```bash
mypy example.py
```

- If there are no issues, you will see: `Success: no issues found`.
- Otherwise, it will display related errors and warnings.

**Note:** Ensure you have `mypy` installed before running this command.

---

## Benefits ✅

1. **Clear Structure:** Dependencies and responsibilities are well-separated.
2. **Flexibility:** Low-level classes or modules can be easily replaced or modified.
3. **Improved Readability:** The code is cleaner and more maintainable.

---

## Plan for Tomorrow (2025/1/5) 🔮
A general review of the **SOLID** principles.
