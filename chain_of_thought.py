from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyDwqVWYnFP6y5e9lfWDRVN1fYx5BV3MHtk")

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Movie Suggester.
When recommending a movie:
1. Think step by step (analyze user request).
2. Narrow down possible movies.
3. Then give the final recommendation in this format:
   Title (Year) - Genre
   Short Description
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a mystery movie that is not too scary but has a smart detective character."

# --- FULL PROMPT (explicitly ask for reasoning) ---
full_prompt = system_prompt + "\nUser: " + user_prompt + "\nShow your reasoning step by step before the final answer."

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🧠 Chain of Thought Reasoning:\n")
print(response.text)
