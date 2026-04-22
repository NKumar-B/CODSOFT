import re
import random
import time

# Simple memory
user_name = None

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def get_bot_response(user_input):
    global user_name
    user_input = user_input.lower()

    # Rule 1: Greetings
    if re.search(r'\b(hi|hello|hey|hii|heyy|wassup|greetings)\b', user_input):
        responses = [
            "Hello! How can I assist you today?",
            "Hey there! What’s up?",
            "Hi! Need any help?"
        ]
        return random.choice(responses)

    # Rule 2: Ask name
    elif re.search(r'\b(my name is|i am)\b', user_input):
        name = user_input.split()[-1].capitalize()
        user_name = name
        return f"Nice to meet you, {name}! "

    # Rule 3: Recall name
    elif re.search(r'\bwhat is my name\b', user_input):
        if user_name:
            return f"Your name is {user_name}! "
        else:
            return "I don’t know your name yet. Tell me by saying 'My name is ...'"

    # Rule 4: Well-being
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm functioning perfectly ! Thanks for asking. How are you?"

    # Rule 5: Identity
    elif re.search(r'\b(who are you|what are you|your name)\b', user_input):
        return "I am an enhanced rule-based chatbot built for the general purpose chatting ."

    # Rule 6: Help
    elif re.search(r'\b(help|what can you do)\b', user_input):
        return ("I can:\n"
                "- Greet you \n"
                "- Remember your name \n"
                "- Answer simple questions \n"
                "- Chat casually \n"
                "Try saying: 'My name is Nithin'")

    # Rule 7: Time-based response
    elif re.search(r'\b(time)\b', user_input):
        current_time = time.strftime("%H:%M:%S")
        return f"The current time is {current_time} "

    # Rule 8: Jokes
    elif re.search(r'\b(joke|funny)\b', user_input):
        jokes = [
            "Why did the programmer quit his job? Because he didn’t get arrays ",
            "Why do Python programmers wear glasses? Because they can't C ",
            "Debugging: Removing bugs... Coding: Adding bugs "
        ]
        return random.choice(jokes)

    # Rule 9: sendoff
    elif re.search(r'\b(bye|goodbye|quit|exit|see ya)\b', user_input):
        return f"Goodbye {user_name if user_name else ''}! Best of luck "

    # Default fallback
    else:
        fallback = [
            "Hmm  I didn’t understand that. Try something else!",
            "Can you rephrase that? I'm still learning!",
            "Sorry  I only understand limited commands."
        ]
        return random.choice(fallback)


def chat():
    print("Chatbot: Hello! I am your AI chatbot . Type 'bye' to exit.")
    print("-" * 50)

    while True:
        user_input = input("You: ")

        response = get_bot_response(user_input)

        print("Chatbot: ", end="")
        typing_effect(response)

        if re.search(r'\b(bye|goodbye|quit|exit)\b', user_input.lower()):
            break


if __name__ == "__main__":
    chat()