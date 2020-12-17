import random

class Chatbot:

    def __init__(self, reaktionen, zufallsantworten):
        self.__reaktionen = dict(reaktionen)
        self.__zufallsantworten = list(zufallsantworten)
        self.__intelligentanswers = False

    def set_Message(self, message):
        self.__message = str(message)

    def get_response(self):
        self.__message = self.__message.lower()
        self.__words = self.__message.split()

        for word in self.__words:
            if word in self.__reaktionen:
                self.__intelligentanswers = True
                self.__response = self.__reaktionen[word]
        if not self.__intelligentanswers:
            self.__response = random.choice(self.__zufallsantworten)

        return self.__response
