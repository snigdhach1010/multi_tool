import requests

class WebSearchTool:
    def __init__(self):
        self.api_url = "https://api.example.com/search"

    def search(self, query):
        """
        Simulate a web search and return results.
        """
        response = requests.get(self.api_url, params={'q': query})
        return response.json()  # Mocking the result
