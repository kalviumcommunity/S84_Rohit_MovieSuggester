from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOURAIzaSyDwqVWYnFP6y5e9lfWDRVN1fYx5BV3MHtk")

# --- FUNCTION TO BUILD DYNAMIC PROMPT ---
def build_prompt(genre=None, actor=None, mood=None):
    system_prompt = """
    You are an AI Movie Suggester.
    Recommend movies in this format:
    Title (Year) - Genre
    Short Description
    """
    
    # Dynamically create user request
    user_prompt = "Suggest me a movie"
    if genre:
        user_prompt += f" in the {genre} genre"
    if actor:
        user_prompt += f" starring {actor}"
    if mood:
        user_prompt += f" that matches a {mood} mood"
    user_prompt += "."
    
    return system_prompt + "\nUser: " + user_prompt


# --- EXAMPLE RUNS ---
# Example 1: Genre + Actor
prompt1 = build_prompt(genre="action", actor="Tom Cruise")

# Example 2: Genre + Mood
prompt2 = build_prompt(genre="romance", mood="sad")

# Example 3: Only Mood
prompt3 = build_prompt(mood="funny")

# Call Gemini for each
for p in [prompt1, prompt2, prompt3]:
    response = client.models.generate_content(
        model="gemini-pro",
        contents=p
    )
    print("\n🎬 Suggestion:", response.text)
