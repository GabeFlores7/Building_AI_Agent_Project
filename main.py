import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model_name = 'gemini-2.0-flash-001'

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def main():
    print("Hello from building-ai-agent-project!") # user greeting

    args = sys.argv # recieve user input/prompt from CLI

    if len(args) < 2: # If no prompt was passed, print error and exit script
        print("Prompt required. Please input prompt for script to execute.")
        sys.exit(1)

    user_prompt = args[1] # store user input/prompt

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),] # store prompt history into messages list of objects
    

    # Feed user input into LLM
    response= client.models.generate_content(
    model= model_name,
    contents= messages,
    config= types.GenerateContentConfig(
        tools= [available_functions],
        system_instruction= system_prompt),
)


    if response.function_calls:
        for functions_call_part in response.function_calls:
            print(f"Calling function: {functions_call_part.name}({functions_call_part.args})")
    else:
        print(response.text) # print model's response to console

    # If verbose option is selected
    if len(args) > 2 and args[2] == "--verbose":
        print(f"User prompt: {args[1]}")
        # provide metadata to user
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.prompt_token_count}")

if __name__ == "__main__":
    main()
