import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.contacts = []

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Email:").grid(row=1, column=0, sticky="e")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=1, column=1)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if name and email:
            contact = Contact(name, email)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and email.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = ""
            for contact in self.contacts:
                contact_list += f"Name: {contact.name}, Email: {contact.email}\n"
            messagebox.showinfo("Contact List", contact_list)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
