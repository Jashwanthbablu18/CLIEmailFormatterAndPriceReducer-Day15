# 🛠️ Day 15 - Map, Filter, Reduce

Welcome to **Day 15** of my **#30DaysOfPythonChallenge**!  
Today’s focus is on applying functional programming concepts using `map()`, `filter()`, and `reduce()`.

---

## 📌 Topic
Practicing **Python’s functional programming tools**:  
- `map()` for transformation  
- `filter()` for selection  
- `reduce()` for aggregation

---

## 🧠 What I Built

1. ✉️ **Email Cleaner**
   - Uses `map()` to:
     - Convert email addresses to lowercase
     - Strip extra spaces
   - Uses `filter()` to:
     - Remove emails missing `@` or a domain (`.`)

2. 💰 **Price Totaler**
   - Uses `reduce()` from `functools` to:
     - Sum a list of prices into a total amount

---

## 🛠️ Concepts Used

- `map(func, iterable)`  
- `filter(func, iterable)`  
- `reduce(func, iterable)` from `functools`
- Lambda expressions for one-liners
- Input validation and list handling

---

## 💻 How to Run

```bash
python Day-15Code.py
