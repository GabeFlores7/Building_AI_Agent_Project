import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from building-ai-agent-project!") # user greeting

    args = sys.argv # recieve user input/prompt from CLI
    user_prompt = args[1] # store user input/prompt

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),] # store prompt history into messages list of objects
    
    if len(args) < 2: # If no prompt was passed, print error and exit script
        print("Prompt required. Please input prompt for script to execute.")
        sys.exit(1)

    # Feed user input into LLM
    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents= messages

)
    print(response.text) # print model's response to console

    # If verbose option is selected
    if len(args) > 2 and args[2] == "--verbose":
        print(f"User prompt: {args[1]}")
        # provide metadata to user
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.prompt_token_count}")

if __name__ == "__main__":
    main()
