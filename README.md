# ITStep Python Midterm Project

This repository contains my three console applications built for the ITStep Backend Python midterm. The projects demonstrate working with user input, validation, JSON file persistence, standard library utilities, and Object-Oriented Programming (OOP) in Python.

---

## Projects Overview

### 1. Translator App (`translate/`)

A console application for translating words and phrases between Georgian and English.

- **Features**:
  - Supports Georgian → English (`geo-eng`) and English → Georgian (`eng-geo`) modes.
  - Direct phrase translation support alongside word-by-word fallback.
  - Prompts to add missing words directly into the dictionary during runtime.
  - Uses atomic file replacement (`tmp.json` + `os.replace`) to save new words safely without corrupting dictionary files.
  - Interactive loop allowing multiple translations per session.

- **Run command**:
  ```bash
  python3 translate/main.py
  ```

---

### 2. ATM Simulator (`atm/`)

A console ATM simulator managing user accounts, authentication, and balance transactions.

- **Features**:
  - Account registration with automatic unique ID generation (starting at `1001`).
  - Username uniqueness checking and password length validation (minimum 8 characters).
  - Secure login system limited to 3 password attempts before exit.
  - Financial calculations handled using Python's `decimal.Decimal` to avoid floating-point rounding errors.
  - Full data persistence stored in `atm/users.json` using a custom `JSONEncoder` and `object_hook`.

- **Run command**:
  ```bash
  python3 atm/main.py
  ```

---

### 3. Book Management System (`book-management-system/`)

An Object-Oriented console application to manage a collection of books with persistent JSON storage.

- **Features**:
  - Built with `Book` and `BookManager` classes.
  - Full data persistence saved to `book-management-system/database.json`.
  - Custom `BookEncoder` (`json.JSONEncoder` subclass) for converting `Book` objects to JSON.
  - Custom `decode_book` object hook to reconstruct `Book` instances upon loading.
  - Add new books (title, author, publication year).
  - List all stored books formatted cleanly via `__repr__`.
  - Case-insensitive search supporting partial title matches.

- **Run command**:
  ```bash
  python3 book-management-system/main.py
  ```

---

## Technical Highlights

- **Standard Library Only**: Built strictly using Python 3 built-in modules (`json`, `pathlib`, `decimal`, `os`, `typing`).
- **Object-Oriented Programming**: Custom classes, instance methods, and magic methods (`__repr__`).
- **Data Serialization**: Custom `JSONEncoder` implementations and `object_hook` decoders for complex types (`Decimal`, custom class instances).
- **Data Integrity & Persistence**: Persistent storage in JSON files across all three projects with atomic file writes.
- **Input Validation**: Guard clauses, type checks, and loop-based input retry prompts.

---

## Requirements & How to Run

- **Python Version**: Python 3.10 or higher.
- **Dependencies**: None (uses standard library only).

Run any project from the repository root:

```bash
python3 translate/main.py
python3 atm/main.py
python3 book-management-system/main.py
```

---

## Repository Structure

```text
.
├── atm/
│   ├── main.py                 # ATM console application
│   └── users.json              # Persistent user accounts database
├── book-management-system/
│   ├── database.json           # Persistent books database
│   └── main.py                 # Book and BookManager OOP application
├── translate/
│   ├── main.py                 # Translator console application
│   ├── eng-geo.json            # English-to-Georgian dictionary
│   └── geo-eng.json            # Georgian-to-English dictionary
└── README.md
```

