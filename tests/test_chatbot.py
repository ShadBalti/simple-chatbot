import unittest
from advanced_chatbot import AdvancedChat, pairs, reflections

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = AdvancedChat(pairs, reflections)

    def test_greeting(self):
        response = self.chatbot.respond("Hi")
        self.assertIn(response, ["Hello!", "Hey there!", "Hi, how can I assist you today?"])

    def test_name(self):
        response = self.chatbot.respond("What is your name?")
        self.assertIn(response, ["I am a chatbot created by you.", "You can call me Chatbot.", "I'm your friendly assistant."])

    def test_quit(self):
        response = self.chatbot.respond("quit")
        self.assertIn(response, ["Bye, take care!", "Goodbye! Have a great day!", "See you later!"])

if __name__ == "__main__":
    unittest.main()
