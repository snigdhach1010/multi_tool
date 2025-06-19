class Memory:
    def __init__(self):
        self.short_term_memory = {}
        self.long_term_memory = {}

    def store_in_short_term(self, key, value):
        self.short_term_memory[key] = value

    def store_in_long_term(self, key, value):
        self.long_term_memory[key] = value

    def retrieve_from_short_term(self, key):
        return self.short_term_memory.get(key)

    def retrieve_from_long_term(self, key):
        return self.long_term_memory.get(key)
