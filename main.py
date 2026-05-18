# Rule based Python based chatbot by seetha ram

import datetime
import time


name = input("Enter your name: ")
present_hour = datetime.datetime.now().hour

if 5 <= present_hour <= 11:
    print("Good Morning", name)

elif 11 <= present_hour <= 17:
    print("Good Afternoon", name)

elif 17 <= present_hour <= 20:
    print("Good Evening", name)

else:
    print("Good Night", name)


print("Welcome to rule-based-chatbot!")
print("You can ask me basic question, Type 'bye' to exit from bot")

# Chatbot memory creation [dictionry of responses]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am fine. Thank you",
    "who are you": "I am a chatbot created by Seetha ram",
    "motivate me": "build projects, not excuses",
    "happy": "Great to hear that",
    "what is a function": "jakar chatgpt ko pado",
    "bye": "Thank you, see you again",
}


# Function to get response from chatbot
def get_response_of_bot(user_question):
    user_question = user_question.lower()
    for eachKey in responses:
        if eachKey in user_question:
            return responses[eachKey]
    return "I am not trained to answer that. will learn soon"


# Take user input

while True:
    userInput = input("Please ask your question: ")
    reply = get_response_of_bot(userInput)

    print("Bot response: ", reply)

    if "bye" in userInput.lower():
        break
