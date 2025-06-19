# tool_router.py

class ToolRouter:
    def __init__(self, available_tools):
        self.available_tools = available_tools

    def route_tool(self, tool_type):
        """
        Select the appropriate tool based on the task.
        """
        print(f"Routing tool for: {tool_type}")
        if tool_type == "summarizer":
            return self.available_tools["summarizer"]
        elif tool_type == "calculator":
            return self.available_tools["calculator"]
        elif tool_type == "python_executor":
            return self.available_tools["python_executor"]
        else:
            return None
