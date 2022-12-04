from django.shortcuts import render

from .Buddy.chatbot.BuddyBrain import BuddyBrain

from .Buddy.chatbot import Listener
# Create your views here.


class MirrorBuddy(BuddyBrain):
    def __init__(self):
        self.mirror_buddy = BuddyBrain()
    
    def talk(self):
        message = self.mirror_buddy.listen()
        answer, tag = self.mirror_buddy.answer(message)
        self.mirror_buddy.use_voice(answer)
        return message, answer, tag
    
#funkcja 
def chatbot(message):
    message = message.lower()
    tag = ""
    if message=='':
        mirror_buddy = MirrorBuddy()
        while True:
            if tag == 'user_wants_to_talk':
                break
            message, answer, tag = mirror_buddy.talk()
            

    if message=="Hej":
        return "No dzien dobry"
    
    if message.find("led") != -1:
        return "Ledy znajdujące się w pokoju SU niedługo zostaną zerwane, wraz z tym samorząd obalony. Przygotujcie się na rewolucje - Liberté, égalité, fraternité!!"
    if message.find("samorząd") != -1:
        return "Członków samorządu możesz poznać korzystając z funkcji 'Znajdź' na pasku nawigacyjnym. Sam nie wiem o nich za dużo, więc lepiej sam z nimi pogadaj."
    
    response = message
    return response

def chatbot_view(request):
    botresponse = "Cześć! Jestem MirrorBuddy, twój elektroniczny towarzysz, przewodnik po szkole, one-man army! Czego potrzebujesz?"
    if request.method=="POST":
        botresponse = chatbot(request.POST.get('message'))
    
    return render(request, 'chatbot.html', {'botresponse':botresponse})


