import speech_recognition as sr
import pyttsx3
from datetime import datetime
listener = sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[15].id)

def clinicTalk(talk):
    engine.say(talk)
    engine.runAndWait()

def listening():
    with sr.Microphone() as source:
        print("Listening: ")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        return command.lower()

clinicTalk("Hello, I am Clinic. How may I help you? Please choose any one option between Diagnosis or Write Prescription")

def diagnosis():
    clinicTalk("What problems are you facing?")
    command = listening()
    if "having pain" in command:
        lastoccurance=""
        clinicTalk("Where you are facing the pain?")
        area = listening()
        clinicTalk("For how many days?")
        duration = listening()
        clinicTalk("What's the quality of the pain?")
        quality = listening()
        clinicTalk("Is it spreading?")
        spread = listening()
        clinicTalk("At what time you face the pain?")
        timing = listening()
        clinicTalk("How it affects you?")
        effects = listening()
        clinicTalk("Has it happened before?")
        last = listening()
        if last == "Yes":
            clinicTalk("Was it the same?")
            lastoccurance = listening()


def writePrescription():
    clinicTalk("What's the patient name?")
    name = listening()
    clinicTalk("Age?")
    age = listening()
    clinicTalk("Gender?")
    gender = listening()
    medicines = []
    while 1:
        clinicTalk("Name of medicine?")
        medicine = listening()
        clinicTalk("Dozes?")
        dozes = listening()
        medicines.append([medicine,dozes])
        clinicTalk("Anymore Medicine?")
        repeat = listening()
        if repeat == "no":
            break
    
    file1 = open(f"Prescription {datetime.datetime}.txt","a")
    file1.write(f"""

Name - {name}
Age - {age}
Gender - {gender}

    """)

    for medicine in medicines:
        file1.write(f"""

{medicine[0]} - {medicine[1]}

        """)

    file1.close()
        

initial_command=listening()

if initial_command == "diagnosis":
    diagnosis()
elif initial_command == "voice prescription":
    writePrescription()