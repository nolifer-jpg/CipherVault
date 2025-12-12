import os
import tkinter as tk
from tkinter import messagebox

import security_engine

cipher = security_engine.get_cipher()


def add_password():
    website = website_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Fields Cannot be empty!")
        return

    encrypted_pwd = security_engine.encrypt_content(cipher, password)

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {encrypted_pwd}\n")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password Saved & Encrypted!")


def decrypt_database():
    if not os.path.exists("passwords.txt"):
        messagebox.showerror("Error", "File Not Found!")
    else:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
        result_text = ""
        for line in lines:
            try:
                curr_line = line.strip()
                website, encrypted_password = curr_line.split(" | ")
                decrypted_password = security_engine.decrypt_content(
                    cipher, encrypted_password
                )

                result_text += (
                    f"Site: {website}\nPass: {decrypted_password}\n{'-' * 20}\n"
                )
            except Exception:
                continue

        messagebox.showinfo("Decrypted Data", result_text)


root = tk.Tk()
root.title("CipherVault")
root.geometry("500x400")
root.configure(bg="black")

tk.Label(
    root,
    text="---CipherVault---",
    font=("Courier", 24, "bold"),
    bg="black",
    fg="#00FF00",
).pack(pady=20)

tk.Label(root, text="Website", bg="black", fg="white").pack()
website_entry = tk.Entry(root)
website_entry.pack()

tk.Label(root, text="Password", bg="black", fg="white").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

add_btn = tk.Button(
    root, text="Encrypt & Save", width=20, bg="gray", command=add_password
).pack()
decrypt = tk.Button(
    root, text="DECRYPT", width=20, bg="red", fg="white", command=decrypt_database
).pack()

root.mainloop()
