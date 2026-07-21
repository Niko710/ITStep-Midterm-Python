# ITStep Python Midterm — Console Applications

A collection of three interactive Python console applications created for the
ITStep Backend Python midterm. Each project focuses on practical programming
skills: clear menus, input validation, reusable functions, JSON file handling,
and object-oriented design where it fits the problem.

## Projects

### 🌐 Translator

Translate individual words between Georgian and English using UTF-8 JSON
dictionaries. Choose a language direction, enter a word or space-separated
words, and receive the translation in the console. If a word is missing, the
application can add its translation to the selected dictionary.

- Georgian → English and English → Georgian modes
- Dictionary data stored in `translate/geo-eng.json` and
  `translate/eng-geo.json`
- Safe dictionary updates via a temporary JSON file

Run it with:

```bash
python3 translate/main.py
```

### 🏧 ATM Simulator

An educational ATM simulation with local account persistence. Users can register
an account, log in with password retry protection, view their balance, deposit
money, and withdraw money when sufficient funds are available.

- User records and balances stored in `atm/users.json`
- Unique numeric IDs for newly registered users
- `Decimal` used for monetary calculations
- Validation for empty usernames, password length, and non-positive amounts

```bash
python3 atm/main.py
```

> **Note:** This is a learning project. `users.json` contains sample data and
> passwords are not production-secure. Never use real personal information or
> passwords in this file.

### 📚 Book Management System

Manage an in-memory collection of books through a simple command-line menu.
The project uses `Book` and `BookManager` classes to model book data and manage
the collection.

- Add books with title, author, and publication year
- List every book with clear details
- Search titles case-insensitively, including partial matches
- Validate required text fields and numeric publication years

```bash
python3 book-management-system/main.py
```

## Skills Demonstrated

- Variables, conditions, loops, lists, dictionaries, and user-defined functions
- Defensive console input handling and informative error messages
- Reading, creating, and updating JSON files
- File-safe updates using `pathlib` and temporary files
- Object-oriented programming with classes, methods, and string representations
- Type hints and docstrings for clearer, maintainable code

## Getting Started

### Requirements

- Python **3.10** or newer
- No third-party packages — the projects use only the Python standard library

From the repository root, run one of the commands shown above. Each application
provides its own interactive menu; enter the listed command exactly as shown and
use `exit` to close it.

## Repository Structure

```text
.
├── atm/
│   ├── main.py                 # ATM console application
│   └── users.json              # Sample accounts and saved balances
├── book-management-system/
│   └── main.py                 # Book and BookManager application
├── translate/
│   ├── main.py                 # Translator console application
│   ├── eng-geo.json            # English-to-Georgian dictionary
│   └── geo-eng.json            # Georgian-to-English dictionary
└── README.md
```

## Quick Verification

Check that all source files have valid Python syntax before submitting changes:

```bash
python3 -m py_compile translate/main.py atm/main.py book-management-system/main.py
```

Then manually test each menu's normal and invalid input paths. For example, test
an unknown translation, an ATM withdrawal above the available balance, and a
book search with no matching title.
