from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")

system_prompt = """
You are an AI Movie Suggester.
Always recommend movies in this format:
Title (Year) - Genre
Short Description
"""

user_prompt = "Suggest me a science fiction movie."

# Try different temperatures
for temp in [0.0, 0.7, 1.0]:
    print(f"\n--- Temperature: {temp} ---")
    response = client.models.generate_content(
        model="gemini-pro",
        contents=system_prompt + "\nUser: " + user_prompt,
        generation_config={"temperature": temp}
    )
    print(response.text)
