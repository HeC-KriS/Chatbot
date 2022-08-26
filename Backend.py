
import sys
import urllib
import datetime
import webbrowser
import pandas as pandas
import bs4
import requests
import random
import random

import pyttsx3

from time import sleep
import csv
#import pandas
from csv import reader

import speech_recognition as sr
import pyttsx3

import speech_recognition as sr
import pyttsx3
with open('E:/chatbot/data.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        # print(list_of_rows)

with open('E:/chatbot/logical.csv', 'r') as read_ob:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_ob)
        # Pass reader object to list() to get a list of lists
        list_of_row = list(csv_reader)
        # print(list_of_rows)
y=0 
z=0

value = list_of_row[y][z]
r = sr.Recognizer()


def speak(audio):
    
    engine = pyttsx3.init()
    voices = engine.getProperty(list_of_row[0][1])
    #a = int(list_of_row[0][2])
     
    engine.setProperty(list_of_row[0][1], voices[1].id)
    engine.setProperty([list_of_row[0][3]], [list_of_row[0][4]])
    engine.say(audio)
    engine.runAndWait()
def recozier():
    global MyText
    while (1):

    # Exception handling to handle
    # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Recording...")
                # listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                z1 = input("Did you say " + MyText+ "\ntype yes or no\n")
                if z1 == "yes" or z1 == "Yes":
                    return MyText
                        
                        
                else:
                    speak("Come again")
                    MyText = input("What were u saying?\n")
                    
                
                    

                    break
                #SpeakText(MyText)
                break

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
            speak("Unknown Error Occurred")


def scrapinfo(message):
    message = message.split()
    # Making the URL
    url = "https://www.google.com/search?q="
    
    for i in message:
        url = url + i + "+"

    # HTTP request
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    # Collect results
    results = soup.find_all("div", {"class": "BNeawe s3v9rd AP7Wnd"})
    rest1 = results[0].get_text()
    rest2=results[3].get_text()
    rest3=results[6].get_text()
    #results=results.get_text()
    '''
    for i in range(0,6,2):
        
    # Print results in python console
        print('+'+results[i].get_text())
    '''

    return [rest1,rest2,rest3,url]


def recozier2():
    global Mytext
    while (1):

    # Exception handling to handle
    # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Recording...")
                # listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio
                Mytext = r.recognize_google(audio2)
                Mytext = Mytext.lower()

                z1 = input("Did you say " + Mytext+ "\ntype yes or no\n")
                if z1 == "yes" or z1 == "Yes":
                    return Mytext
                        
                        
                else:
                    speak("Come again")
                    Mytext = input("What were u saying?\n")
                    
                
                    

                    break
                #SpeakText(MyText)
                break

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
            speak("Unknown Error Occurred")

def time():
    now = datetime.datetime.now()
    print(5)
    dt_string = now.strftime(list_of_row[1][1])
    print(6)

    print(dt_string)
    speak(list_of_row[1][2] + now.strftime(list_of_row[1][3]))
    speak(list_of_row[1][4] + now.strftime(list_of_row[1][5]))
def death():
    take_time='There is no set time for overcoming a duel . It is important to know that each person has their own rhythm in overcoming emotional trauma, just as each person takes a different time to heal physical wounds. Be patient with yourself and do not demand deadlines, little by little you will find yourself better.'
    accept='Sadness, pain, anxiety and fear (among others) are normal reactions in situations of mourning. The first step to overcome the loss of your loved one is to accept that you have the right to feel pain for it. Repressing these feelings will not do you any good, and will hinder your recovery, being able to even become complicated and become a pathological duel.'
    seek_support='The death of a loved one does not mean that you should forget how important it was for you in your life. Many people confuse overcoming a loss by forgetting or pretending that they do not exist, but overcoming their death means accepting that the loved one is gone, knowing how important it was for us.'
    deat=[take_time,accept,seek_support]
    txt=random.choice(deat)
    print(txt)
    print(speak(txt))

def relation_probs():
    listen='Often you believe you are listening, but you are distracted or rehearsing your answer in your mind. You dont really hear what the other person is saying. People want your undivided attention when they are speaking. When they are done sharing, summarize what you heard and ask for confirmation.'
    hidden='Reoccurring family conflicts often mask a hidden issue because family members are afraid to tell the truth. Be open. Ask questions that encourage honesty and a deep discussion.'
    perspective='Its easy to see your family from your own perspective and not recognize the differences between individuals. Every family is filled with different needs, personalities, and viewpoints. Whether you agree or not, be open to hearing from your family members about how they see and experience you. What they share may surprise you.'
    humble='Be Humble. Working through a conflict can cause you to react and over-explain yourself. Dont do it! Humility requires you to listen, understand, and not respond with an explanation. Honestly, people dont really care about all your reasons, just let them know you regard them more highly than yourself. Believe me, I know  I often have reasons for why I do what I do and my kids call me out. Humility, sigh….'
    apology='Offer a sincere apology. A sincere apology is soothing balm to a wounded heart. The secret is that your apology cant be offered without first listening to their complaint. A hasty “I am sorry” to end a conflict is meaningless. You must understand how you offended the other person and commit to preventing it from happening again.'
    relas=[listen,hidden,perspective,humble,apology]
    txt=random.choice(relas)
    print(txt)
    print(speak(txt))
 
def demotivation():
    timeout='Sometimes, the feeling of restlessness comes from too much work or too much routine. Our brain needs a bit of novelty, and our bodies need a bit of rest. Put whatever you have to do on hold and take a short break doing something that you enjoy. Relax, take a walk, have a nice nap, or go and try out something new.Take a break without worrying too much about your problems, and you will come back energized and ready to take the situation on.'
    hands_on='There are tasks that can help you reduce restlessness. Often, we tend to get too stuck on our digital devices or too caught up in our heads. Instead, go and do something that involves interacting with the physical world and that will bring you a clear result. Clean a room, organize your desk, water the plants, or do some gardening.'
    fun='A common reason for the lack of motivation is the feeling that our day is going to be dull and unpleasant. You can address it by scheduling something fun for later.'
    punctuality='A good tip to reduce restlessness is to set a deadline that will push you to start acting now. It will help you get into action right away. It is important, however, to respect the deadline you set for yourself and stop working when you said you would.'
    demotiv=[timeout,hands_on,fun,punctuality]
    txt=random.choice(demotiv)
    print(txt)
    print(speak(txt))

def alone():
    socializing='First and the foremost way to tackle loneliness is to start interacting with people. Interaction doesn’t include online chatting, it means talking with people in-person to establish a strong connection and bond among.'
    community='A variety of programs are organized by schools, colleges, institutions, companies, government to help people get close to each other. By participating in these programs, one can connect with many others of similar interests. Marathons, Raahgiri Day or Swatch Bharat Abhiyaan are some of the interest-based communities that you can get involved.'
    volunter='Volunteering not only helps you to connect with people but also gives a chance to engage in activities that you are passionate about. While working, you’ll connect with people that are into the same interest zone as you are, which will help you to connect with them easily.'
    pet='Welcoming a pet into your life helps to heal loneliness as you would have someone with you all the time. You can talk to them, feed them, go for a walk with them, love them and get love in return. Dogs and cats are regarded as the best companions to share your feelings with and getting the same amount of affection without being judged.'
    alon=[socializing,community,volunter,pet]
    txt=random.choice(alon)
    print(txt)
    print(speak(txt))


def Addiction():
    play_games='It is easy to place blame when in the throes of addiction or when dealing with an addict. It’s important to understand that the addict is not to blame for his/her addiction, but that s/he must take sole — and soul — responsibility for recovering from it.'
    Be_patient='It may take more than one attempt to get it right. Some days may be harder than others.  Every effort you make is a step towards your goal, and it is an essential part of the journey. Even if someone is not yet ready to change, but they take a few steps toward recovery, they are receiving tools that can help them later on.'
    exercise='Exercise is an important part of any healthy lifestyle.  Some people recover from alcohol and drugs with exercise alone simply because they don’t want to feel bad every day when they try to move their bodies. This is especially true for athletes who have had addiction problems. For the average person, 30-60 minutes of walking outside every day will do wonders.'
    priority='Divine love is accessible to everyone and it the most powerful form of healing. People often have profound experiences of emotional release and also physical healing, including healing from addiction. And, as Bob Fritchie points out, the more people involved, the better. So you can use Divine Love to help someone you love even if they are not ready to use it themselves. I love the idea of being able to tune into and utilize this energy on behalf of myself and others. '
    addict=[play_games,Be_patient,exercise,priority]
    txt=random.choice(addict)

    print(txt)
    print(speak(txt))

def Insomia():
    create_routine='Creating a sleep routine before you go to bed can be helpful to establish good sleep habits. Do something before bed each evening that relaxes you or prepares you to fall asleep, such as meditating or journaling.Try to go to bed at the same time every night and wake up at the same time every morning.Avoid using any screens right before you go to bed because the light can make it harder to fall asleep.'
    factors='Sometimes your insomnia is related to something else. If you can identify what’s causing it, then that root cause can be treated. For example, maybe you have undiagnosed anxiety or depression that’s leading to insomnia.If you have gone through a traumatic experience, if you’re under a lot of stress or if you have a physical health problem, these can all lead to insomnia. Speak with your doctor if you’re unsure if any of these situations apply to you but believe something similar could be causing your insomnia.'
    sleep_journal='Keeping a sleep journal can help you see patterns in how you sleep and maybe identify habits that can easily change. It can also be helpful to show your doctor or health care provider if you aren’t able to get past your insomnia.Include information such as how long you slept, what you did before bed and whether or not you woke up in the night. You can also detail your sleep quality and how you felt when you woke up in the morning.'
    change_ur_thinking='Often we get stuck in a pattern of negative and self-defeating thoughts when we experience anxiety. It can be frustrating, but it’s helpful to work on changing your negative thoughts.'
    insom=[create_routine,factors,sleep_journal,change_ur_thinking]
    txt=random.choice(insom)
    print(txt)
    print(speak(txt))

def Stress():
    Breathe='Slow, deep breaths can help lower blood pressure and heart rate. Try pranayama breathing, a yogic method that involves breathing through one nostril at a time to relieve anxiety. The technique is supposed to work the same way as acupuncture, balancing the mind and body.'
    Music='No matter what the song, sometimes belting out the lyrics to a favorite tune makes everything seem all right. If you’re in a public place, just listening to music can be a quick fix for a bad mood. Classical music can be especially relaxing right before bedtime.'
    Quick_walk='When you’re feeling overwhelmed or having trouble concentrating, go for a quick stroll around the block. You’ll get the benefits of alone time, physical activity, and a few minutes to gather your thoughts.'
    Yoga='Put your feet up—against the wall, of course. The Vipariti Kirani yoga pose involves lying on the floor and resting the legs up against a wall. Not only does it give the body a good stretch, but it helps create peace of mind, too.'
    strss=[Breathe,Music,Quick_walk,Yoga]
    txt=random.choice(strss)
    print(txt)
    print(speak(txt))

def weather():
    speak(list_of_row[2][1])
    weather = input(list_of_row[2][2])
    speak(list_of_row[2][3])
    print(list_of_row[2][3])
    webbrowser.open(list_of_row[2][5] + weather, new=list_of_row[2][4])
    sleep(5)
    
def song():
    speak(list_of_row[3][1])
    Link = input(list_of_row[3][2])
    speak(list_of_row[3][3])
    print(list_of_row[3][3])
    webbrowser.open(list_of_row[3][5] + Link, new=list_of_row[3][4])
    sleep(5)

def search():
    speak(list_of_row[4][1])
    Link = input(list_of_row[4][1])
    speak(list_of_row[4][2])
    print(list_of_row[4][2])
    webbrowser.open(list_of_row[4][4] + Link, new=list_of_row[4][3])



    sleep(5)
def ash():
    speak(list_of_row[15][1])
    print(list_of_row[15][1]
    )
    sleep(1)
def quit():
    sys.exit()
def greetings():
    print(list_of_row[5][1])
    print("\n")
    speak(list_of_row[5][1])
    print(
        list_of_row[5][2])
    print("\n \n \n")
    # ("type 'hi', 'hello' or 'hey' to start, After starting...,type your name and begin..., type 'search' to search for something, type 'time' or 'what's the time' for the date and time, you can ask me my favourite color by typing 'favourite color', P.S - I'm not case sensitive. ")
    print(list_of_row[5][3])
    speak(list_of_row[5][3])
    print("\n")


    with open('E:/Chatbot_back/data.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        # print(list_of_rows)

    y = 1
    z = 0
    value = list_of_rows[y][z]
    print("\n")
    while True:
        check =input("type yes if u want to use voice recognition feature else type no\n")
        if check == 'yes' or check == "Yes":

            
            
            print(recozier())
            message = MyText
            break
    
    # print(value)
        elif check == "no" or check == "No":
            message = input(list_of_row[5][4] + "\n")
            break
        else:
            print("Come Again!!")
            continue

    while True:
        

        z = 0
        value = list_of_rows[y][z]
       
        # initialize list of lists
        if value == message:
            
            print(list_of_rows[y][1])
            speak(list_of_rows[y][1])

            if message == "quit":
                sys.exit()
                break
            break




        elif value == list_of_rows[-1][z]:
            
            print("I didnt get it but u can tell me what to text for it.....")
            speak("I didnt get it but u can tell me what to text for it.....")
            b = input("Reply for it: ")

            data = [[message, b]]
            df = pandas.DataFrame(data, columns=['input', 'output'])
            df.to_csv('E:/chatbot/data.csv', index=False, mode='a', header=False)

            break

        else:
            y = y + 1
            print(4)
            continue


def help(list_of_rows, z,y):
    #global message2
    while True:

    



        print('d')
        speak(list_of_row[6][1])
        name = input(list_of_row[6][1]+"\n")
        print("This is ASH A.K.A Artificial Super Human created by TRKE Company owned by Mast. Krishvin Raam. M and Mast. Tharak Enjamur")
        speak("This is ASH AKA Artificial Super Human created by TRKE Company owned by Mast Krishvin Raam M And Mast Tharak Enjamur")
        print("\n")

        while True:
            y = 1
            z = 0
            speak(list_of_row[6][2] + name)
            while True:
                check2 =input("type yes if u want to use voice recognition feature else type no\n")
                if check2 == 'yes' or check2 == "Yes":
                    
                    print(list_of_row[6][2]+", " + name + list_of_row[6][3]+'\n')
                    speak(list_of_row[6][2]+", " + name + list_of_row[6][3])
                    print(recozier2())
                    message2 = Mytext
                    break
            
            # print(value)
                elif check2 == "no" or check2 =="No":
                    message2 = input(list_of_row[6][2]+", " + name + list_of_row[6][3]+'\n')
                    break
                else:
                    print("Come Again!!")
                    continue

            #message2 = input(list_of_row[6][2]+", " + name + list_of_row[6][3]+'\n')

            while True:
                        #print(1)
                        #c = str(a[b])
                        #print(2)
                        #b = b + 1
                        
                        #print(3)
                        
                        
                        #value = list_of_rows[y][z]

                        if 1 == 1:
                            message2=message2.lower()
                            print(2)
                            #print(list_of_rows[y][1])
                            c = list_of_rows[y][1]
                            p = message2.split()
                            qqq = 0
                            #print(p)
                            #print(p[0])
                            value = list_of_rows[y][z]
                            while True:
                                r = str(p[qqq])
                                #print(qqq)
                                
                                
                                #print(list_of_rows[y][z])

                                if r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[9][0] or r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[9][1]:
                                    print(time())
                                    break

                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[10][0] or r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[10][1]:
                                    print(search())
                                    break

                                    print(7)
                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[11][0] or r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[11][1]:
                                    print(song())
                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[12][0] or r == list_of_rows[y][z] and list_of_rows[y][1] == list_of_row[12][1]:
                                    print(weather())
                                    break

                                                                    
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'death' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'death':
                                    print(death())
                                    break

                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'conflict' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'conflict':
                                    print(relation_probs())

                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'demotivation' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'demotivation':
                                    print(demotivation())
                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'loneliness' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'loneliness':
                                    print(alone())
                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'addiction' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'addiction':
                                    print(Addiction())
                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'Insomnia' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'Insomnia':
                                    print(Insomia())

                                    break
                                elif r == list_of_rows[y][z] and list_of_rows[y][1] == 'stress' or r == list_of_rows[y][z] and list_of_rows[y][1] == 'stress':
                                    print(Stress())
                                    break
                                elif r == "quit" or r == "bye":
                                    print("bye bro will see ya later!")
                                    
                                    print(quit())
                                    break
                            
                                elif r == str(p[-1]) and list_of_rows[y][z] == list_of_rows[-1][z]:
                                    
                                    #print(3)
                                    #speak(list_of_row[7][1])
                                    #print(list_of_row[7][1])
                                    #webbrowser.open(list_of_row[7][4] + message2, new=list_of_row[7][2])
                                    dat1,dat2,dat3,ur=scrapinfo(message2)
                                    print(dat1)
                                    speak(dat1)
                                    print(dat2)
                                    speak(dat2)
                                    print(dat3)
                                    speak(dat3)
                                    webbrowser.open(ur, new=list_of_row[7][2])


                                    while True:
                                        check =input("type yes if u want to use voice recognition feature else type no\n")
                                        if check == 'yes' or check == "Yes":
                                            
                                            print(recozier())
                                            w = MyText
                                            break
            
            # print(value)
                                        elif check == "no" or check == "No":
                                            w = input(list_of_row[7][3]+"\n")
                                            break
                                        else:
                                            print("Come Again!!")
                                            continue

                                    
                                    #w = input(list_of_row[7][3]+"\n")
                                    xxx = w.split()
                                    yyy = 0
                                    while True:
                                        zzz = str(xxx[yyy])
                                        print(2)
                                        yyy = yyy + 1
                                        if zzz == "song" or zzz == "Song" or zzz == "song?" or zzz == "Song?":
                                            data = [[message2,"song"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "weather" or zzz == "Weather" or zzz == "Weather?" or zzz == "weather?":
                                            #data = [[message2,"weather"]]
                                            #df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df = pandas.DataFrame({'input': [message2],'output': ['weather']})
                                            df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "Time" or zzz == "time" or zzz == "time?" or zzz == "Time?":
                                            data = [[message2,"time"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "search" or zzz == "Search" or zzz == "search?" or zzz == "Search?":
                                            data = [[message2,"search"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == xxx[-1]:
                                            data = [[message2,dat2]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                            break
                                            '''
                                            print(list_of_row[8][1])
                                            speak(list_of_row[8][1])
                                            print(list_of_row[8][2])
                                            speak(list_of_row[8][2])
                                            print(list_of_row[8][3])
                                            speak(list_of_row[8][3])

                                        
                                            speak(list_of_row[8][4])
                                            k = input(list_of_row[8][4])
                                            if k == "new" or "New":
                                                data = [[message2, w]]
                                                df = pandas.DataFrame(data, columns = ['input', 'output'])
                                                df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                                break

                                            else:
                                                data = [[message2,k]]
                                                df = pandas.DataFrame(data, columns = ['input', 'output'])
                                                df.to_csv('E:/chatbot/data.csv', index = False, mode = 'a', header = False)
                                                break
                                            '''
                                        else:
                                            continue
                                        
                            
                                else:
                                    if list_of_rows[y][z]== list_of_rows[-1][z]:
                                        qqq = qqq+1
                                        y = 0
                                    elif message2 == list_of_rows[y][z]:
                                        if list_of_rows[y][1] == 'song' or list_of_rows[y][1] == 'Song':
                                            print(song()) 
                                        elif list_of_rows[y][1] == 'time' or list_of_rows[y][1] == 'Time':
                                            print(time())
                                        elif list_of_rows[y][1] == 'weather' or list_of_rows[y][1] == 'Weather':
                                            print(weather())
                                        elif list_of_rows[y][1] == 'search' or list_of_rows[y][1] == 'Search':
                                            print(song())
                                        else:
                                            print(list_of_rows[y][1])
                                        break
                                        
                                        
                                    
                                    
                                    else:
                                        y=y+1
                                    continue
                                break
                            break

                        

                        

                            
                

        
dogo=0
cogo=0
print(greetings())
print(help(list_of_rows, dogo, cogo))
#print(speak("hello"))
