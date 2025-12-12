# 🔐 CipherVault

**CipherVault** is a secure, offline password manager built in Python. It provides a graphical interface to store passwords locally in an encrypted format, ensuring your data remains unreadable without the unique master key.

## 🚀 Key Features

* **Military-Grade Encryption:** Uses the `cryptography` library (Fernet/AES) to lock data instantly.
* **Offline Privacy:** No cloud servers. Your data lives in a text file on your own machine.
* **Automatic Key Management:** Generates a unique `secret.key` on the first run.
* **Dark Mode GUI:** A clean, hacker-themed interface built with `Tkinter`.
* **One-Click Decryption:** Instantly reveal your stored credentials securely.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI:** Tkinter (Standard Library)
* **Security:** `cryptography` library (Fernet module)
* **Storage:** Local File I/O (.txt and .key files)

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/CipherVault.git](https://github.com/YourUsername/CipherVault.git)
    cd CipherVault
    ```

2.  **Install Dependencies**
    ```bash
    pip install cryptography
    ```

## 💻 How to Run

1.  Ensure `main.py` and `security_engine.py` are in the same folder.
2.  Run the application:
    ```bash
    python main.py
    ```
3.  **To Add:** Enter a Website and Password -> Click **Encrypt & Save**.
4.  **To View:** Click **DECRYPT DATABASE** to see your secrets.

## ⚠️ Critical Warning

This program generates a file named `secret.key`. **Do not delete or lose this file.**
If you lose this key, the mathematics behind the encryption make it impossible to recover your passwords.

## 📜 License

This project is open-source and available for educational purposes.
