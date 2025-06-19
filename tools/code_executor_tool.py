class CodeExecutorTool:
    def execute(self, code):
        """
        Executes Python code and returns the result.
        """
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            return exec_locals
        except Exception as e:
            return f"Error executing code: {e}"
