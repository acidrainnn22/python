import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


while True:
    with  speech_recognition.Microphone() as mic:
        print("Robot: I am listening")
        audio = robot_ear.listen(mic)

    print("Robot...")

    try: 
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: "+ you)

    if you == "" :
        robot_brain = "I can't  hear you, try again!"
    elif "hello" in you:
        robot_brain = "Hello Ms.Chi"
    elif "your name" in you:
        robot_brain = "My name is computer"
    elif "time" in you:
        now =datetime.now()
        robot_brain = now.strftime("%H hour %M minutes %S seconds")
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d %Y")
    elif "bye" in you:
        robot_brain = "Bye Ms.Chi"
        print("Robot: "+ robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break;
    else:
        robot_brain = "I am fine thank you"

    print("Robot: "+ robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait() 
