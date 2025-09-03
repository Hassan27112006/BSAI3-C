

"""
These imports provide the required tools for the calculator:

- math:
    * Gives access to mathematical constants (pi, e).
    * Provides math functions (sqrt, sin, cos, etc.).

- time:
    * Used to generate timestamps for calculation history.

- evaluator.safeEvaluator:
    * Custom class for securely evaluating expressions.
    * Uses AST (Abstract Syntax Trees) to avoid unsafe code execution.

- utils.matchassignment:
    * Utility function that checks if an expression
      is a variable assignment (e.g., "x=10").
    * Returns variable name and right-hand side expression.
"""

import math
import time
from evaluator import safeEvaluator
from utils import matchassignment



#  Calculator Core Class


"""
This class implements the core logic for a dynamic calculator.

Features:
- Supports safe expression evaluation (via safeEvaluator).
- Provides built-in constants (pi, e).
- Provides built-in functions (sqrt, sin, cos).
- Supports memory operations (M+, M-, MR, MC).
- Stores and manages variables assigned by user.
- Maintains calculation history (last 20 expressions).
"""


class calculator_core:
   
    #  Initialization
   
    def __init__(self):
        """
        Initialize calculator with:
        - safeEvaluator instance for secure evaluation.
        - Default constants (pi, e).
        - Default math functions (sqrt, sin, cos).
        - Memory storage (initialized to 0.0).
        - History list for previous calculations.
        """
        self.evaluator = safeEvaluator()
        self.vari = {"pi": math.pi, "e": math.e}
        self.fun = {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos}
        self.memory = 0.0
        self.history = []

 
    # 🔹 Memory Operations
    # 
    def m_plus(self, x):
        """Add value x to memory."""
        self.memory += x

    def m_minus(self, x):
        """Subtract value x from memory."""
        self.memory -= x

    def mr(self):
        """Return current memory value."""
        return self.memory

    def mc(self):
        """Clear memory (reset to 0.0)."""
        self.memory = 0.0

    # ------------------------------------------
    # 🔹 Expression Evaluation
    # ------------------------------------------
    def evaluate(self, expr):
        """
        Evaluate an expression.
        - If expression is an assignment (e.g., x=10):
            * Extract variable name and right-hand side.
            * Evaluate RHS using safeEvaluator.
            * Store value in vari dictionary.
            * Add to history.
        - If expression is just a calculation:
            * Directly evaluate using safeEvaluator.
            * Add to history.
        """
        assign = matchassignment(expr)
        if assign:
            var, rhs = assign
            val = self.evaluator.eval_expr(rhs, self._env())
            self.vari[var] = val
            self._add_history(expr, val)
            return val

        val = self.evaluator.eval_expr(expr, self._env())
        self._add_history(expr, val)
        return val

    # ------------------------------------------
    # 🔹 Environment Setup
    # ------------------------------------------
    def _env(self):
        """
        Create evaluation environment.
        Combines:
        - User-defined variables (vari).
        - Supported math functions (fun).
        This ensures only safe operations are available to evaluator.
        """
        env = {}
        env.update(self.vari)
        env.update(self.fun)
        return env

    # ------------------------------------------
    # 🔹 History Management
    # ------------------------------------------
    def _add_history(self, expr, val):
        """
        Save a calculation to history.
        - Stores expression, result, and timestamp.
        - Keeps only the last 20 calculations.
        """
        self.history.insert(0, (expr, val, time.strftime("%H:%M:%S")))
        self.history = self.history[:20]
