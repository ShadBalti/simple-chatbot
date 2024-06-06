import spacy
from nltk.chat.util import Chat, reflections
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", "Nice to meet you %1!"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi, how can I assist you today?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.", "You can call me Chatbot.", "I'm your friendly assistant."]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you for asking!", "I'm just a program, but I'm here to help you!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.", "Don't worry about it!"]
    ],
    [
        r"I am fine",
        ["Good to know that you are fine.", "Great! How can I assist you today?"]
    ],
    [
        r"quit",
        ["Bye, take care!", "Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*) your name?",
        ["My name is Chatbot.", "You can call me Chatbot.", "I'm Chatbot, your virtual assistant."]
    ],
    [
        r"how (.*) created?",
        ["I was created using Python and spaCy.", "I am a result of programming with Python and spaCy."]
    ],
    [
        r"what (.*) want?",
        ["I want to help you with your queries.", "I'm here to assist you with any questions you have."]
    ],
    [
        r"(.*) weather?",
        ["I don't have weather data right now, but you can check it online.", "I'm not connected to a weather service, but you can check your local weather app."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help you. What do you need assistance with?", "How can I assist you? Please let me know your query."]
    ],
    [
        r"(.*) created you?",
        ["I was created by a developer using Python and spaCy.", "A programmer built me using Python and the spaCy library."]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm a virtual assistant, so I exist in the digital world.", "I don't have a physical location, but I'm here to help you online."]
    ],
    [
        r"(.*) joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"(.*) (age|old)?",
        ["I'm timeless!", "I'm as old as the internet, or maybe just a bit younger."]
    ],
    [
        r"(.*) (music|song)?",
        ["I don't listen to music, but I can help you find some!", "I'm not into music, but I bet you have great taste!"]
    ],
]

# Creating a Chat object with spaCy NLP
class AdvancedChat(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)
        self.nlp = nlp
    
    def respond(self, input):
        doc = self.nlp(input.lower())
        for pattern, responses in self._pairs:
            match = doc.similarity(self.nlp(pattern))
            if match > 0.7:
                response = random.choice(responses)
                return response % tuple(self._wildcards(doc, pattern))
        return "I didn't quite understand that. Could you please rephrase?"

# Start the chatbot
def chat():
    chatbot = AdvancedChat(pairs, reflections)
    print("Hi, I'm the chatbot you created. How can I help you today?")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye, take care!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
