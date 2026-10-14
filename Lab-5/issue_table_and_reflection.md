# Lab 5: Static Code Analysis

## 1. Issues Identified and Fixed

| No. | Tool | Issue | Fix Applied |
|---|---|---|---|
| 1 | Bandit | SQL query constructed through string concatenation, creating a potential SQL injection vulnerability. | Replaced string concatenation with parameterized SQL queries using placeholders. |
| 2 | Bandit | Hardcoded curator password in the source code. | Removed the unused hardcoded password. |
| 3 | Bandit | Subprocess command used `shell=True`, creating an avoidable security risk. | Replaced the shell command with a direct Python print statement. |
| 4 | Pylint | Unused `datetime` import. | Removed the unused import. |
| 5 | Pylint | Missing module and function docstrings. | Added descriptive docstrings. |
| 6 | Pylint | Function names did not follow snake_case naming conventions. | Renamed functions to use snake_case. |
| 7 | Flake8 | Lines exceeded the recommended length. | Split long statements across multiple lines. |
| 8 | Flake8 | Missing whitespace around an operator and excess blank lines. | Corrected spacing and blank-line formatting. |

## 2. Before-and-After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 4.85/10 | 10.00/10 |
| Bandit | 5 findings: 4 low, 1 medium | No issues identified |
| Flake8 | 8 reported violations | No violations reported |
