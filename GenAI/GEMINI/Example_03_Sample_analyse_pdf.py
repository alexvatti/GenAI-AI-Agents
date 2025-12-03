from google import genai
from google.genai import types
import pathlib
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path(r'alex-report-06-Mar-2025-1764590459524.pdf.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)