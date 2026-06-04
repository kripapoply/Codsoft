print("Hello! I am CodSoft Chatbot.")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is CodSoft Chatbot.")

    elif user == "who are you":
        print("Bot: I am a simple AI chatbot.")

    elif user == "where are you from":
        print("Bot: I am created in Python.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI.")

    elif user == "what is coding":
        print("Bot: Coding is writing instructions for computers.")

    elif user == "what can you do":
        print("Bot: I can answer basic questions.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a nice day.")

    elif user == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "thank you":
        print("Bot: You are welcome!")

    elif user == "thanks":
        print("Bot: Happy to help!")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "what is your purpose":
        print("Bot: My purpose is to help users.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer Python? Because it is easy to learn!")

    elif user == "what is your favorite color":
        print("Bot: I like all colors equally.")

    elif user == "are you human":
        print("Bot: No, I am a chatbot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")
