import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import pyttsx3 as psx
from ..chatbot import Listener as listener
#import listener




class BuddyBrain():
    def __init__(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        self.lemmatizer = WordNetLemmatizer()
        self.intents = json.loads(open('/home/pete/Coding/Python/Medi_Bot/Buddy/databases/word_bank2.json').read())

        self.words = pickle.load(open('/home/pete/Coding/Python/Medi_Bot/Buddy/configuration_files/words.pkl', 'rb'))
        self.classes = pickle.load(open('/home/pete/Coding/Python/Medi_Bot/Buddy/configuration_files/classes.pkl','rb'))

        self.model = load_model('/home/pete/Coding/Python/Medi_Bot/Buddy/chatbot_model.model')

        self.engine = psx.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',"Polish")
        self.engine.setProperty("rate",160)

    #tokenizacja i lemantyzacja
    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    #zwraca liste tokenów i zlemantyzwoanych słów
    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    #klasa, która używa gotowego modelu do predykcji
    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = .25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        results.sort(key=lambda x: x[1], reverse=True)

        return_list = []
        for r in results:
            return_list.append({'intent':self.classes[r[0]], 'probability': str(r[1])})
        return return_list

    
    def get_response(self, intents_list, intents_json):
        try:
            tag = intents_list[0]['intent']
            print(f"Wyjątek: {intents_list[0]['intent']}")
        except IndexError:
            print("####################################")
            print("INDEX ERROR")
            print("I WIL PRINT USER WANTS TO TALK")
            print("####################################")
            tag = "user_lonely"
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result, tag

    def answer(self, message):
        ints = self.predict_class(message)
        res, tag = self.get_response(ints,self.intents)
        return res, tag
    
    def listen(self):
        message = listener.listener()
        return message

    def use_voice(self,answer):
        self.engine.say(answer) 
        self.engine.runAndWait()

    def all_in_one(self):
        message = self.listen()
        answer, tag = self.answer(message)
        self.use_voice(answer)
        return message, answer, tag






 

        
        