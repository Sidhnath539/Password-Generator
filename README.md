# 🔐 Password Generator Using Python Tkinter

## 📌 Project Overview

The Password Generator is a GUI-based Python application developed using the Tkinter library. It generates strong and secure random passwords based on user-defined criteria such as password length and character types. Users can customize the password by choosing uppercase letters, lowercase letters, numbers, and special symbols.

This project helps users create secure passwords for online accounts and demonstrates the use of Python GUI development and random string generation.

---

# 🚀 Features

* User-friendly graphical interface
* Custom password length selection
* Include uppercase letters (A-Z)
* Include lowercase letters (a-z)
* Include numbers (0-9)
* Include special symbols (!@#$%^&*)
* Random secure password generation
* Copy password to clipboard
* Input validation and error handling

---

# 🛠️ Technologies Used

* Python 3.x
* Tkinter (GUI Development)
* Random Module
* String Module

---

# 📂 Project Structure

```text
Password-Generator/
│
├── password_generator.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/password-generator.git
```

### Step 2: Navigate to the Project Directory

```bash
cd password-generator
```

### Step 3: Install Python

Ensure Python 3.x is installed on your system.

Check installation:

```bash
python --version
```

---

# ▶️ Running the Application

Execute the following command:

```bash
python password_generator.py
```

The Password Generator GUI window will open.

---

# 📖 How to Use

1. Launch the application.
2. Enter the desired password length.
3. Select the character types:

   * Uppercase Letters
   * Lowercase Letters
   * Numbers
   * Symbols
4. Click **Generate Password**.
5. The generated password will appear in the output field.
6. Click **Copy Password** to copy it to the clipboard.

---

# 🖥️ Sample Output

```text
Password Length: 12

Selected Options:
✔ Uppercase
✔ Lowercase
✔ Numbers
✔ Symbols

Generated Password:
A#7kP!9x@Lm2
```

---

# 🔄 Workflow

1. User enters password length.
2. User selects desired character categories.
3. Application creates a character pool.
4. Random characters are selected.
5. Password is generated and displayed.
6. User can copy the password to the clipboard.

---

# 🏗️ Modules Used

## Tkinter

Used for creating the graphical user interface.

## Random

Used to generate random characters for the password.

## String

Provides predefined character sets:

* ascii_uppercase
* ascii_lowercase
* digits
* punctuation

---

# ❌ Error Handling

### Invalid Length

```text
Password length must be greater than 0.
```

### No Character Type Selected

```text
Please select at least one character type.
```

### Empty Password Copy

```text
Generate a password first!
```

---

# 🎯 Learning Outcomes

Through this project, you will learn:

* Python GUI Development
* Event Handling in Tkinter
* Random Data Generation
* Input Validation
* Clipboard Operations
* User Interface Design

---

# 🔒 Security Benefits

* Generates unpredictable passwords
* Supports strong password creation
* Helps improve account security
* Reduces use of weak passwords

---

# 📈 Future Enhancements

* Password Strength Meter
* Password History Storage
* Dark Mode Theme
* Password Export Feature
* Auto-Save Generated Passwords
* Multiple Password Generation
* QR Code Password Sharing

---

# ✅ Advantages

* Simple and lightweight
* Easy to use
* Fast password generation
* Customizable settings
* Improves online security

---

# 👨‍💻 Author

**Siddhnath Prajapati**

Python Developer | GUI Application Developer

---

# 📄 License

This project is developed for educational and learning purposes. You are free to modify, improve, and distribute it for non-commercial use.

---

# 🙏 Acknowledgement

Special thanks to Python's Tkinter library and the open-source community for providing excellent resources and documentation that helped in developing this project.
