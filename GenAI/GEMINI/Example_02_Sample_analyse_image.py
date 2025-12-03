from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

with open(r'LeBron_James_Layup.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'What teams are playing in this image.'
    ]
  )

print(response.text)