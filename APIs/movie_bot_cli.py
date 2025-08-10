import sys

def cli_movie_bot():
    print("🎥 Welcome to the Movie Bot CLI! 🎬")
    print("Type your message to ask about movies. (Type 'exit' to quit)\n")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in ['exit', 'quit']:
            print("👋 Goodbye! Thanks for using the Movie Bot.")
            break

        try:
            response = movie_reply(user_message)
            print("\nMovie Bot:", response, "\n")
        except Exception as e:
            print("\nMovie Bot: Oops! Something went wrong.")
            print(f"Error: {e}\n")

if __name__ == "__main__":
    from movie_bot_core import movie_reply  # Make sure your main movie bot code is saved as movie_bot_core.py
    cli_movie_bot()
