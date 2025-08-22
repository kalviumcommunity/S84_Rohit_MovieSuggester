from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyDwqVWYnFP6y5e9lfWDRVN1fYx5BV3MHtk")

# --- SYSTEM PROMPT (role of AI) ---
system_prompt = """
You are an AI Movie Suggester.
Recommend movies based only on the user query.
Always provide movie title, release year, and a short explanation.
"""

# --- USER PROMPT (zero-shot: no examples given) ---
user_prompt = "Suggest me a thriller movie with a plot twist."

# Combine prompts
full_prompt = system_prompt + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎬 Zero-Shot Suggestion:", response.text)
