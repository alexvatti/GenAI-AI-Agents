import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def get_gpt5_mini_response(task_prompt, effort_level):
    """A simple function to call gpt-5-mini and return text."""
    print(f"REQUESTING: {task_prompt}")
    print(f"CONTROL SETTING: reasoning['effort'] = '{effort_level}'\n")

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=[
                {"role": "developer", "content": "You are a concise assistant."},
                {"role": "user", "content": task_prompt}
            ],
            reasoning={"effort": effort_level}, # <-- Your control knob
            text={"format": {"type": "text"}},
        )
        
        # This is the standard way to extract text from the new API format
        print("MODEL RESPONSE:")
        print(response.output_text)
        print("\n" + "="*60 + "\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example 1: Use Minimal Effort for precise, factual answers (Low Variability) ---

# Task: Get a single, specific fact.
get_gpt5_mini_response(
    task_prompt="What is the boiling point of water in Celsius?",
    effort_level="minimal" 
)
# Expected Output: Very direct and factual (100 degrees Celsius).

# --- Example 2: Use High Effort for analysis or slightly more complex generation ---

# Task: Requires a bit more analysis or varied word choice.
get_gpt5_mini_response(
    task_prompt="Describe the color blue without using the word 'blue'.",
    effort_level="high" 
)
# Expected Output: The model takes more "internal steps" to generate varied descriptions (e.g., 'azure', 'sky', 'ocean hue').

# --- Example 3: Use Medium Effort for a standard, balanced response ---

# Task: General explanation.
get_gpt5_mini_response(
    task_prompt="Explain why we have leap years.",
    effort_level="medium"
)
# Expected Output: A clear explanation that is coherent and balanced in tone.
