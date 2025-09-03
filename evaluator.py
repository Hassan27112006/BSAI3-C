import ast


# ==============================================
# 🔹 Safe Evaluator Class
# ==============================================

"""
This class securely evaluates mathematical expressions
using Python's Abstract Syntax Trees (AST).

Why AST?
- Prevents execution of unsafe Python code.
- Only allows a controlled subset of operators and nodes.
- Safe alternative to using Python's built-in `eval`.

Supported Operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%) → remainder after division
- Power (**) → exponentiation
- Unary plus (+x) and unary minus (-x)
- Variables (e.g., x, y) defined in environment
- Function calls (e.g., sqrt(16), sin(x)) if included in environment
"""


class safeEvaluator:
    # ------------------------------------------
    # 🔹 Allowed Operations
    # ------------------------------------------
    """
    Define sets of allowed AST nodes and operators.
    - BinOps: +, -, *, /, %, **
    - UnaryOps: +, -
    - Nodes: numbers, expressions, variables, function calls
    """
    Allowed_binopes = {ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow}
    allowed_unaryops = {ast.UAdd, ast.USub}
    allowed_nodes = {ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant}

   
    #  Public Method: Expression Evaluation
   
    def eval_expr(self, expr, env):
        """
        Evaluate a mathematical expression safely.

        Parameters:
        - expr (str): Input expression as string (e.g., "2+3*5", "sqrt(16)").
        - env (dict): Environment with allowed variables and functions.

        Steps:
        1. Replace '^' with '**' (since ^ in Python means XOR, not power).
        2. Parse expression into AST tree.
        3. Recursively evaluate AST tree using _eval().
        """
        expr = expr.replace('^', '**')
        tree = ast.parse(expr, mode='eval')
        return self._eval(tree.body, env)

    # ------------------------------------------
    # 🔹 Private Method: Recursive AST Evaluation
    # ------------------------------------------
    def _eval(self, node, env):
        """
        Recursively evaluate AST nodes.

        Supported nodes and operations:
        - ast.Constant → numeric constants like 2, 3.14
        - ast.UnaryOp:
            * +x → returns positive of x
            * -x → returns negative of x
        - ast.BinOp:
            * left + right → addition
            * left - right → subtraction
            * left * right → multiplication
            * left / right → division (floating-point)
            * left % right → modulus (remainder)
            * left ** right → exponentiation (power)
        - ast.Name:
            * Variables must exist in env (e.g., x, y).
        - ast.Call:
            * Function calls like sqrt(16), sin(x).
            * Function must exist in env and be callable.
        """

        # -------------------------
        # 🔹 Numeric Constants
        # -------------------------
        if isinstance(node, ast.Constant):
            return node.value

        # -------------------------
        # 🔹 Unary Operations (+, -)
        # -------------------------
        elif isinstance(node, ast.UnaryOp):
            val = self._eval(node.operand, env)
            return +val if isinstance(node.op, ast.UAdd) else -val

        # -------------------------
        # 🔹 Binary Operations (+, -, *, /, %, **)
        # -------------------------
        elif isinstance(node, ast.BinOp):
            left = self._eval(node.left, env)
            right = self._eval(node.right, env)

            # Addition
            if isinstance(node.op, ast.Add): return left + right
            # Subtraction
            if isinstance(node.op, ast.Sub): return left - right
            # Multiplication
            if isinstance(node.op, ast.Mult): return left * right
            # Division
            if isinstance(node.op, ast.Div): return left / right
            # Modulus
            if isinstance(node.op, ast.Mod): return left % right
            # Power (exponentiation)
            if isinstance(node.op, ast.Pow): return left ** right

        # -------------------------
        # 🔹 Variables
        # -------------------------
        elif isinstance(node, ast.Name):
            if node.id not in env:
                raise ValueError(f"Undefined variable: {node.id}")
            return env[node.id]

       
        #  Function Calls
        
        elif isinstance(node, ast.Call):
            fname = node.func.id
            if fname not in env or not callable(env[fname]):
                raise ValueError(f"Undefined function: {fname}")
            # Recursively evaluate arguments
            args = [self._eval(arg, env) for arg in node.args]
            return env[fname](*args)

      
        #  Unsupported nodes
       
        else:
            raise ValueError(f"Unsupported expression: {ast.dump(node)}")
