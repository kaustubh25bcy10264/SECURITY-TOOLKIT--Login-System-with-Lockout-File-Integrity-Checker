# 🔐 Security Toolkit – Login system with lockout & File integrity checker

>**⭐ Very ideal for academic submissions, security demonstrations, and practical cybersecurity training.**

---

## 📖 Overview

The **Security toolkit: Login system with lockout and file integrity checker** is a cyber-security related project demonstrating secure handling of login, account lockout protection, verification and checking of file integrity, and, audit logging.

This toolkit stresses on secure programming principles such as **hashing**,**modularization**,**error handling**, and **logging** –all essential in perspective of modern security engineering.

---

## ✨Project's core features

| Feature | Description | Security Focus |
| :--- | :--- | :--- |
| **Secure File Hashing** | Implements **SHA-256 hashing** using chunked reading for safe processing of very large files(even files in Gigabytes). | Verification of Integrity |
| **Login Lockout System** | Automatically locks accounts after repeated failed login attempts (configurable) to counter **brute-force attacks**. | Authentication Security |
| **User-Friendly Error Messages** | Provides descriptive feedback for missing files, invalid credentials, or permission issues. | Usability & Security |
| **Audit Logging** | Logs all login attempts, lockouts, hashing operations, and errors, for? **Forensic analysis**. | Accountability & Monitoring |
| **Modular Code Architecture** | Separate modules for hashing, logging, and authentication ensures clean separation of concerns. | Maintainability & Scalability |
| **Efficient & Memory-Safe** | Uses **chunk-based hashing** to avoid memory overload when handling large files. | Performance |

---

## 🛠️ technologies used in this project

* **Python 3.x** (Recommendation: 3.11 or 3.12)
* `hashlib` — A Secure hashing library
* `logging` — Audit & event tracking
* `random`  — Logics for Password generation
* **Visual Studio Code / Visual Studio 2022**
* **Git & GitHub** — Version control

---

## ⚙️ Installation & setup

1. **Clone Repository**
	
```bash
git clone https://github.com/kaustubh25bcy10264/SECURITY-TOOLKIT--Login-System-with-Lockout-File-Integrity-Checker.git
cd security-toolkit
```

2. **Setting up python environment**
	
Please Ensure python 3.11 or higher is installed. It is highly recommended to create and activate a virtual environment and work inside it.
	
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

3. **Installing dependencies**

If requirements.txt exists:

```Bash
pip install -r requirements.txt
```

Run file hashing (provide a path to a file):
```Bash
python main.py path/to/your/file.ext
```

## 🧪 Testing Guide
Use the following given scenarios to check & validate the toolkit's security features:

### ✔️ Successful login
1.  Enter valid username and password.
2.  Confirm successful login message and log entry inside log file.

### ❌ Lockout After Failed Attempts
1.  Enter wrong credentials 3 or more times.
2.  Verify following:
- Account is locked that is you can't relogin for predefined time, here it is 30 seconds.
- Lockout event is properly logged.
- Program should display a clear countdown message.

### 📄 File Hashing Test
1.  Place a test file (e.g., sample.txt) in the project directory.
2.  Run the hashing command: python main.py sample.txt
3.  Check:
  - Hash output is displayed.
  - A "File not found!" message appears if an incorrect path is provided.
  - Log entries confirm the hashing activity.

### 🔐 Permission Denied Test
1.  Attempt to hash a file that you don’t have permission to read.
2.  Confirm that the expected error message and corresponding log entry are produced.

### 📝 Audit Trail Validation
1.  Inspect the log file: logs/project.log
2.  You should see proper  entries for: Login attempts, Lockouts, File hashes, and Exceptions/errors.

### 🚀 Future Improvements
These features are planned for future development of the project and to enhance its security posture, these are given below:
  * Can use Salted password hashing (using bcrypt or argon2) in place of hash256.
  * Multi-Factor Authentication (MFA) will ensure more security.
  * Role-Based Access Control (RBAC) can be added.
  * properly Encrypted user databases could be integrated.
  * Log rotation & archival.

