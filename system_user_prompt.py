from google import genai


client = genai.Client(api_key="AIzaSyDwqVWYnFP6y5e9lfWDRVN1fYx5BV3MHtk")

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Movie Suggester.
- Your job is to recommend movies based on user preferences.
- Always include the movie title, release year, genre, and a short description.
- Keep the tone friendly and concise.
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a comedy movie with Jim Carrey."

# --- FULL PROMPT (system + user) ---
full_prompt = system_prompt + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎬 Movie Suggestion:", response.text)
