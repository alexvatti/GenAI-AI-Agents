from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Summarize the performance of small cap, mid cap, large cap ",
    config=config,
)

print(response.text)