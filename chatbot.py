def chatbot():
    print("Welcome to my Python Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        message = input("You: ").lower().strip()

        if message == "hello":
            print("Bot: Hi!")
        elif message == "how are you":
            print("Bot: I'm fine, thanks!")
        elif message == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
