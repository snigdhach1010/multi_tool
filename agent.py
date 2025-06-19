from task_planner import TaskPlanner
from tool_router import ToolRouter
from memory import Memory
from llm_interaction import LLMInteractionHandler
from tools.web_search_tool import WebSearchTool
from tools.calculator_tool import CalculatorTool
from tools.code_executor_tool import CodeExecutorTool
from tools.document_summarizer_tool import DocumentSummarizerTool

class LLMAgent:
    def __init__(self, llm_model):
        self.memory = Memory()
        self.task_planner = TaskPlanner()
        self.tool_router = ToolRouter({
            "summarizer": DocumentSummarizerTool(),
            "calculator": CalculatorTool(),
            "python_executor": CodeExecutorTool(),
        })
        self.llm_interaction_handler = LLMInteractionHandler(llm_model)

    def execute_task(self, task):
        print(f"Executing task: {task}")
        
        subgoals = self.task_planner.generate_subgoals(task)
        print(f"Subgoals generated: {subgoals}")
        
        results = []
        for subgoal in subgoals:
            tool_type = subgoal.split(" ")[2]  # Example: extract tool type from subgoal
            tool = self.tool_router.route_tool(tool_type)
            
            if tool:
                print(f"Using tool: {tool_type}")
                
                if tool_type == "summarizer":
                    print("Calling summarizer tool...")
                    result = tool.summarize("This is a long document content for summarization.")
                elif tool_type == "calculator":
                    print("Calling calculator tool...")
                    result = tool.evaluate("3 + 5")  # Example calculation
                elif tool_type == "python_executor":
                    print("Calling python executor tool...")
                    code = "x = 10\nx + 5"  # Example code to execute
                    result = tool.execute(code)

                print(f"Tool result: {result}")
                results.append(result)
            else:
                print(f"Tool {tool_type} not found!")

        print(f"Final results: {results}")
        return results