# 📚 Python Library Management System

A simple **Library Management System** built with Python, MySQL, and OpenLibrary API.  
This project allows users to create accounts, log in securely, borrow or view books, and manage their library activities — all through a command-line interface.

---

## 🚀 Features

- 🧾 **User Authentication**
  - Create a new account
  - Secure login using **bcrypt** password hashing
  - Reset forgotten passwords

- 📚 **Book Management**
  - Search for books using the `get_book()` function
  - Automatically fetch book details (title, author, year, edition, link)
  - Add new books to the MySQL database
  - Display all stored books in a tabular format using `tabulate`

- 🌐 **Smart Integration**
  - Opens book links directly in your default web browser
  - Validates user emails using Regular Expressions
  - Uses `OpenLibrary` API for fetching book data

---

## 🧩 Technologies Used

- **Python 3**
- **MySQL** (Database)
- **bcrypt** (Password encryption)
- **tabulate** (Table formatting)
- **webbrowser** (Open book URLs)
- **re** (Email validation)
- **OpenLibrary API** (Book data)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
