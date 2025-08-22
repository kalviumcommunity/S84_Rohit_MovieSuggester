import tiktoken  # pip install tiktoken

# Initialize tokenizer (GPT-3.5/GPT-4 tokenizer works similarly for demo)
tokenizer = tiktoken.get_encoding("cl100k_base")

# Example prompts
prompt1 = "Suggest me a comedy movie."
prompt2 = "Suggest me a romantic comedy movie starring Jim Carrey with a funny plot and a happy ending."

# Tokenize
tokens1 = tokenizer.encode(prompt1)
tokens2 = tokenizer.encode(prompt2)

print("Prompt 1:", prompt1)
print("Tokens:", tokens1)
print("Token count:", len(tokens1))

print("\nPrompt 2:", prompt2)
print("Tokens:", tokens2)
print("Token count:", len(tokens2))
