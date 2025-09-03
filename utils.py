import re


# ==============================================
# 🔹 Assignment Expression Matcher
# ==============================================

"""
This utility function checks whether a given expression
is a variable assignment (e.g., "x = 10 + 5").

It uses a regular expression to detect assignments and
returns the variable name and right-hand side expression.

Supported Syntax:
- Variable names must start with a letter or underscore.
- Variable names can contain letters, numbers, and underscores.
- Assignment uses '=' sign with optional spaces around it.
- Right-hand side can be any valid mathematical expression.

Examples:
- "x=10"      → ("x", "10")
- "y = 5*2"   → ("y", "5*2")
- "z = sqrt(9)" → ("z", "sqrt(9)")
- "2x=10"     → None (invalid variable name)
"""

# ----------------------------------------------
# 🔹 Regular Expression for Assignment
# ----------------------------------------------
"""
Regex: ^\s*([A-Za-z_]\w*)\s*=\s*(.+)$

Explanation:
- ^\s*              → Start of string, allow leading spaces.
- ([A-Za-z_]\w*)    → Variable name:
                       * Must start with letter or underscore.
                       * Can contain letters, digits, underscores.
- \s*=\s*           → Equal sign with optional spaces around it.
- (.+)              → Right-hand side (RHS), at least one character.
- $                 → End of string.
"""
_assign_re = re.compile(r"^\s*([A-Za-z_]\w*)\s*=\s*(.+)$")


# ----------------------------------------------
# 🔹 Function: matchassignment
# ----------------------------------------------
def matchassignment(expr: str):
    """
    Check if an expression is an assignment.

    Parameters:
    - expr (str): Input expression (e.g., "x=10", "y = 5*2").

    Returns:
    - (var, rhs) if valid assignment:
        * var: variable name (string)
        * rhs: right-hand side expression (string)
    - None if not a valid assignment.

    Example:
    >>> matchassignment("x=10")
    ('x', '10')

    >>> matchassignment("a = sqrt(16)")
    ('a', 'sqrt(16)')

    >>> matchassignment("5=10")
    None  (invalid, cannot assign to number)
    """
    m = _assign_re.match(expr)
    if not m:
        return None
    return m.group(1), m.group(2)

