import random

# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "greetings"]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Function to generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for word in greetings:
        if word in user_input:
            return random.choice(responses)
    return "I'm sorry, I don't understand what you're saying."

# Main loop for chatting
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot: " + response)
import random

# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "greetings"]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Function to generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for word in greetings:
        if word in user_input:
            return random.choice(responses)
    return "I'm sorry, I don't understand what you're saying."

# Main loop for chatting
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot: " + response)