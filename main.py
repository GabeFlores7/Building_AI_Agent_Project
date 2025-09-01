import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    print("Hello from building-ai-agent-project!")
    args = sys.argv
    if len(args) < 2:
        print("Prompt required. Please input prompt for script to execute.")
        sys.exit(1)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents= args[1]

)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.prompt_token_count}")

if __name__ == "__main__":
    main()
