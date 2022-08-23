
import sys
import urllib
import datetime
import webbrowser



import pyttsx3

from time import sleep
import csv
import pandas
from csv import reader

import speech_recognition as sr
import pyttsx3

import speech_recognition as sr
import pyttsx3
with open('E:/Chatbot_back/data.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        # print(list_of_rows)

with open('E:/Chatbot_back/logical.csv', 'r') as read_ob:
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
            df.to_csv('data.csv', index=False, mode='a', header=False)

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


                                
                                elif r == "quit" or r == "bye":
                                    print("bye bro will see ya later!")
                                    
                                    print(quit())
                                    break
                            
                                elif r == str(p[-1]) and list_of_rows[y][z] == list_of_rows[-1][z]:
                                    
                                    print(3)
                                    speak(list_of_row[7][1])
                                    print(list_of_row[7][1])
                                    webbrowser.open(list_of_row[7][4] + message2, new=list_of_row[7][2])
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
                                            df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "weather" or zzz == "Weather" or zzz == "Weather?" or zzz == "weather?":
                                            data = [[message2,"weather"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "Time" or zzz == "time" or zzz == "time?" or zzz == "Time?":
                                            data = [[message2,"time"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == "search" or zzz == "Search" or zzz == "search?" or zzz == "Search?":
                                            data = [[message2,"search"]]
                                            df = pandas.DataFrame(data, columns = ['input', 'output'])
                                            df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                            break
                                        elif zzz == xxx[-1]:
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
                                                df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                                break

                                            else:
                                                data = [[message2,k]]
                                                df = pandas.DataFrame(data, columns = ['input', 'output'])
                                                df.to_csv('data.csv', index = False, mode = 'a', header = False)
                                                break
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
