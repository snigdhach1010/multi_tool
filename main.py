# main.py

from llm_interaction import LLMInteractionHandler

if __name__ == "__main__":
    # Replace with your actual Google API key
    google_api_key = "your-google-api-key-here"
    
    agent = LLMInteractionHandler(google_api_key)

    # Get user input for the task and text (document or calculation expression)
    task = input("Enter the task (e.g., 'summarize' or 'calculate'): ").lower()
    text = input("Enter the document or calculation expression: ")

    # Process the task with the Gemini LLM model
    result = agent.process_task(task, text)
    
    # Print the results (summarized text or calculation result)
    print("Result:", result)
