# calculator_tool.py

class CalculatorTool:
    def evaluate(self, expression):
        """
        Evaluates a mathematical expression.
        """
        try:
            print(f"Evaluating expression: {expression}")  # Debugging output
            result = eval(expression)
            print(f"Calculated result: {result}")  # Debugging output
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"
