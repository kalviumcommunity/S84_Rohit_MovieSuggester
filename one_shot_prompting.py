from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyDwqVWYnFP6y5e9lfWDRVN1fYx5BV3MHtk")

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Movie Suggester.
Always recommend movies in this format:
Title (Year) - Genre
Short Description
"""

# --- ONE EXAMPLE (few-shot learning with 1 sample) ---
example = """
Example:
User: Suggest me a sci-fi movie about space exploration.
AI: Interstellar (2014) - Sci-Fi
A visually stunning film directed by Christopher Nolan, exploring time dilation and survival in space.
"""

# --- USER PROMPT (new request) ---
user_prompt = "Suggest me an action movie with Tom Cruise."

# --- FINAL PROMPT (system + example + user) ---
full_prompt = system_prompt + "\n" + example + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎬 One-Shot Suggestion:", response.text)
