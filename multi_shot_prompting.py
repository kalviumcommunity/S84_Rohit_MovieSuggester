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

# --- MULTI-SHOT EXAMPLES ---
examples = """
Example 1:
User: Suggest me a sci-fi movie about artificial intelligence.
AI: Ex Machina (2014) - Sci-Fi/Thriller
A thought-provoking film exploring AI consciousness and human relationships.

Example 2:
User: Suggest me a romantic movie with a tragic ending.
AI: Titanic (1997) - Romance/Drama
A love story set on the doomed Titanic, blending romance with historical tragedy.

Example 3:
User: Suggest me a superhero movie with humor.
AI: Deadpool (2016) - Action/Comedy
A hilarious, action-packed superhero movie known for breaking the fourth wall.
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a horror movie about ghosts."

# --- FINAL PROMPT ---
full_prompt = system_prompt + "\n" + examples + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎬 Multi-Shot Suggestion:", response.text)
