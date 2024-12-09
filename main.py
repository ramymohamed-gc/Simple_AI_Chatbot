import os
from dotenv import load_dotenv 
from openai import AzureOpenAI
import colorama
from colorama import Fore, Style

load_dotenv()

def main():
    colorama.init(autoreset=True)
    
    client = AzureOpenAI(  
    api_version="2024-07-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key="sk-abcdefghijklmnopqrstuvwx1234567890abcdef"
)

    system_message = {
        "role": "system",
        "content": "You are a virtual AI agent that assists users with their questions. Provide helpful, concise, and friendly answers."
    }

    conversation_history = [system_message]

    while True:
        print(Fore.CYAN + "-" * 50)
        user_input = input(Fore.GREEN + "You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(Fore.YELLOW + "Goodbye!")
            break

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=conversation_history,
        )

        answer = response.choices[0].message.content
        print(Fore.CYAN + "-" * 50)
        print(Fore.MAGENTA + "Model: " + Style.RESET_ALL + answer)
        print(Fore.CYAN + "-" * 50)

        conversation_history.append({
            "role": "assistant",
            "content": answer
        })

if __name__ == "__main__":
    main()