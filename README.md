
# 🧮 Dynamic Calculator (Streamlit + Safe Evaluator)

A **secure, dynamic calculator web app** built with **Python and Streamlit**.  
This project evaluates mathematical expressions, supports variable assignments, provides memory functions, and ensures safety using **AST-based expression parsing** instead of Python’s `eval`.

---

## 🚀 Features

- ✅ Evaluate mathematical expressions safely (`2+3*5`, `sqrt(16)`)
- ✅ Variable assignments (`x = 10`, `y = x*2`)
- ✅ Built-in math constants (`pi`, `e`)
- ✅ Built-in math functions (`sqrt`, `sin`, `cos`)
- ✅ Memory functions (M+, M-, MR, MC)
- ✅ History of last 20 calculations (with timestamps)
- ✅ Secure evaluation using Python **AST** (no arbitrary code execution)

---

## 📂 Project Structure

---

## ⚡ How It Works

### Streamlit Frontend (`app.py`)
- User enters expressions in a text input.
- Buttons allow evaluation, memory operations, and clearing.
- Displays:
  - Result
  - Memory state
  - Calculation history
  - Defined variables

### 2. **Calculator Core (`core.py`)**
Handles:
- Variables storage
- Built-in math functions/constants
- Memory operations:
  - `M+` (add to memory)
  - `M-` (subtract from memory)
  - `MR` (recall memory)
  - `MC` (clear memory)
- History (stores last 20 expressions)

### 3. **Safe Evaluator (`evaluator.py`)**
Uses Python’s **AST (Abstract Syntax Trees)** to safely evaluate expressions:
- Supports:
  - Addition (+), Subtraction (-)
  - Multiplication (*), Division (/)
  - Modulus (%), Power (**)
  - Unary plus (+x), Unary minus (-x)
  - Function calls (`sqrt(16)`, `sin(pi/2)`)
  - Variables (`x`, `y`)
- Blocks unsafe operations (no loops, imports, or system access).

### 4. **Assignment Matcher (`utils.py`)**
- Detects assignments like:
  - `"x = 10"`
  - `"radius = sqrt(16)"`
- Returns `(variable, expression)` pair for evaluation.

---

## 🔢 Supported Operations

| Operation     | Symbol | Example        | Result |
|---------------|--------|----------------|--------|
| Addition      | `+`    | `2+3`          | `5`    |
| Subtraction   | `-`    | `10-4`         | `6`    |
| Multiplication| `*`    | `3*5`          | `15`   |
| Division      | `/`    | `10/2`         | `5.0`  |
| Modulus       | `%`    | `10%3`         | `1`    |
| Power         | `**` or `^` | `2^3` or `2**3` | `8` |
| Unary Plus    | `+`    | `+5`           | `5`    |
| Unary Minus   | `-`    | `-7`           | `-7`   |

---

## 📐 Built-in Constants and Functions

- Constants:
  - `pi` = 3.141592...
  - `e`  = 2.718281...
- Functions:
  - `sqrt(x)` → Square root
  - `sin(x)` → Sine
  - `cos(x)` → Cosine

---

## 💾 Memory Functions

- `M+` → Add last result to memory
- `M-` → Subtract last result from memory
- `MR` → Recall memory
- `MC` → Clear memory

---

## 📜 History

- Stores **last 20 calculations**.
- Each entry includes:
  - Expression
  - Result
  - Timestamp ---