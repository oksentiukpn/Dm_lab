...

# 🧮 Relation Properties Lab

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Doctest](https://img.shields.io/badge/tests-passed-green.svg?logo=pytest)](https://docs.python.org/3/library/doctest.html)

> A Python lab project for working with **binary relations** — compute reflexive, symmetric, and transitive closures,  
> analyze equivalence classes, and check relation properties with ease ⚙️  

...

## 📁 Project Overview

relation_lab/ │ ├── main.py              # Main script with all functions ├── result.csv           # Output file (created by write_file) └── README.md            # You're here :)

---

## ✨ Features

| 🔢 Category | 🧠 Function | 🧩 Description |
|-------------|-------------|----------------|
| **File I/O** | `read_file()` | Reads a matrix from a file |
| | `write_file()` | Writes a matrix to `result.csv` |
| **Closures** | `reflexive_closure()` | Adds missing diagonal elements (makes relation reflexive) |
| | `symmetric_closure()` | Adds mirrored pairs (makes relation symmetric) |
| | `warshall()` | Computes **transitive closure** using Warshall’s algorithm |
| **Analysis** | `relation_breakdown()` | Splits relation into **equivalence classes** |
| | `is_transitive()` | Checks if a relation is **transitive** |
| **Combinatorics** | `count_transitive()` | Counts all transitive relations for a given set size `n` *(⚠️ slow for n > 4)* |

---

## 🧪 Running Tests

All functions include built-in **doctests** — no external libraries required!

```bash
python main.py

✅ If everything is correct, you’ll see:

TestResults(failed=0, attempted=...)


---

🚀 Quick Examples

🔹 Transitive Closure

>>> warshall([[0, 1, 0],
...           [0, 0, 1],
...           [0, 0, 0]])
[[0, 1, 1], [0, 0, 1], [0, 0, 0]]

🔹 Equivalence Classes

>>> relation_breakdown({(1,2), (2,1), (3,4), (4,3), (1,1), (2,2), (3,3), (4,4)}, False)
[{1, 2}, {3, 4}]

🔹 Transitivity Check

>>> is_transitive({(0, 1), (1, 2), (0, 2)}, False)
True


---

⚡ Performance Note

count_transitive(n) grows exponentially (2^(n²) relations checked).
For best results:

🧩 n <= 4 → OK ✅

🐢 n = 5 → slow

🧨 n > 5 → don’t even try



---

💡 Behind the Scenes

This project demonstrates key Discrete Mathematics and Set Theory concepts using Python:

Binary relations

Equivalence relations

Relation properties: reflexive, symmetric, transitive

Closures & relation matrices

Doctest-based validation



---

🧑‍💻 Author

Олександр Оксентюк & Аліна Яцко
🎓 Python developer & discrete math enthusiast
📅 2025


---

📜 License

This project is licensed under the MIT License — free to use, share, and modify.


---

> “Mathematics is not about numbers, equations, or algorithms: it’s about understanding.” — William Paul Thurston



---
