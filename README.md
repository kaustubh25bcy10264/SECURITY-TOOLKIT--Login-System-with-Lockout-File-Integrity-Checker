# 🔐 Security Toolkit – Login System with Lockout & File Integrity Checker

> **⭐ Ideal for academic submissions, security demonstrations, and practical cybersecurity training.**

---

## 📖 Overview

The **Security Toolkit** is a cybersecurity-focused project showcasing secure login handling, account lockout protection, file integrity verification, and audit logging.

This toolkit emphasizes secure programming principles such as **hashing**, **modularization**, **error handling**, and **logging**—all essential in modern security engineering.

---

## ✨ Core Features

| Feature | Description | Security Focus |
| :--- | :--- | :--- |
| **Secure File Hashing** | Implements **SHA-256 hashing** using chunked reading for safe processing of large (multi-GB) files. | Integrity Verification |
| **Login Lockout System** | Automatically locks accounts after repeated failed login attempts (configurable) to counter **brute-force attacks**. | Authentication Security |
| **User-Friendly Error Messages** | Provides descriptive feedback for missing files, invalid credentials, or permission issues. | Usability & Security |
| **Audit Logging** | Logs all login attempts, lockouts, hashing operations, and errors for **forensic analysis**. | Accountability & Monitoring |
| **Modular Code Architecture** | Separate modules for hashing, logging, and authentication ensures clean separation of concerns. | Maintainability & Scalability |
| **Efficient & Memory-Safe** | Uses **chunk-based hashing** to avoid memory overload when handling large files. | Performance |

---

## 🛠️ Technologies Used

* **Python 3.x** (Recommended: 3.11 or 3.12)
* `hashlib` — Secure hashing library
* `logging` — Audit & event tracking
* `random`  — Password generation logic
* **Visual Studio Code / Visual Studio 2022**
* **Git & GitHub** — Version control

---

## ⚙️ Installation & Setup

 1. **Clone the Repository**

```bash
git clone [https://github.com/your-username/security-toolkit.git](https://github.com/your-username/security-toolkit.git)
cd security-toolkit
```

2. **Set Up Python Environment**
   
Ensure Python 3.11+ is installed. It is highly recommended to create and activate a virtual environment.


Linux / macOS
```Bash
python -m venv venv
source venv/bin/activate
```

Windows
```Bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**
* If requirements.txt exists:

```Bash
pip install -r requirements.txt
```

4. **Run the Project**

* Start normally:
```Bash
python main.py
```

* Run file hashing (provide a path to a file):
```Bash
python main.py path/to/your/file.ext
```

## 🧪 Testing Guide
Use the following scenarios to validate the toolkit's security features:

### ✔️ Successful Login
1.  Enter valid username and password.
2.  Confirm successful login message and log entry.

### ❌ Lockout After Failed Attempts
1.  Enter wrong credentials 3 or more times.
2.  Verify:
- Account is locked.
- Lockout event is properly logged.
- A clear countdown message is shown.

### 📄 File Hashing Test
1.  Place a test file (e.g., sample.txt) in the project directory.
2.  Run the hashing command: python main.py sample.txt
3.  Check:
  - Hash output is displayed.
  - A "File not found!" message appears if an incorrect path is provided.
  - Log entries confirm the hashing activity.

### 🔐 Permission Denied Test
1.  Try hashing a file without read permissions.
2.  Verify the correct error message and log entry.

### 📝 Audit Trail Validation
1.  Inspect the log file: logs/project.log
2.  You should see entries for: Login attempts, Lockouts, File hashes, and Exceptions/errors.

### 🚀 Future Improvements
These features are planned for future development to enhance security posture:
  * Salted password hashing (using bcrypt or argon2)
  * Multi-Factor Authentication (MFA)
  * Role-Based Access Control (RBAC)
  * Encrypted user database
  * Log rotation & archival
