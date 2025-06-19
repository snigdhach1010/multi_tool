from langchain_google_genai import ChatGoogleGenerativeAI

class LLMInteractionHandler:
    def __init__(self, google_api_key, llm_model="gemini-1.5-flash"):
        # Initialize the Gemini model with LangChain's ChatGoogleGenerativeAI
        self.llm = ChatGoogleGenerativeAI(
            model=llm_model,
            google_api_key='your-google-api-key-here',
            temperature=0.4,
            max_tokens=None,
        )

    def process_task(self, task, text=None):
        """
        Processes the task (summarization or calculation) with the Gemini model.
        """
        print(f"Processing task with model {self.llm.model}: {task}")
        response = self.call_llm(task, text)
        return response

    def call_llm(self, task, text):
        """
        Interact with Gemini LLM to handle summarization or calculation.
        """
        if "summarize" in task:
            return self.summarize_document(text)
        
        elif "calculate" in task:
            return self.calculate_expression(text)
        
        return "Task not recognized by LLM."

    def summarize_document(self, document):
        """
        Summarize the provided document using Gemini.
        """
        # Make sure document is provided
        if not document:
            return "No document provided for summarization."
        
        # Generate summary using Gemini
        response = self.llm.invoke(f"Please summarize the following document: {document}")
        
        # Access the summary content from the response
        summary = response.content if hasattr(response, "content") else "No summary provided."
        return f"Summary: {summary}"

    def calculate_expression(self, expression):
        """
        Evaluate the provided arithmetic expression.
        """
        try:
            # Evaluate the expression (this assumes it's a valid mathematical expression)
            result = eval(expression)
            return f"Calculation result: {result}"
        except Exception as e:
            return f"Error in calculation: {str(e)}"
