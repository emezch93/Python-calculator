def chatbot():
    print("Hi! I'm your simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if 'hello' in user_input:
            print("Bot: Hello there!")
        elif 'how are you' in user_input:
            print("Bot: I'm fine, thank you!")
        elif 'bye' in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
