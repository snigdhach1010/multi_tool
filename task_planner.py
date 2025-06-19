# task_planner.py

class TaskPlanner:
    def __init__(self):
        pass

    def generate_subgoals(self, task):
        """
        Given a task, break it down into smaller subgoals.
        """
        subgoals = []
        
        if "summarize" in task:
            subgoals.append("Use the summarizer tool to summarize the content.")  # Changed "document summarizer" to "summarizer"
        
        if "calculate" in task:
            subgoals.append("Use the calculator tool to evaluate the expression.")
        
        if "code" in task:
            subgoals.append("Use the python executor tool to run the code.")
        
        return subgoals
