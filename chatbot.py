import speech_recognition as sr
import pyttsx3
import webbrowser
import tkinter as tk
import wikipedia

#text to speech
engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()

#voice input speech recognition
def check():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
        order= r.recognize_google(audio,language="en-in",show_all=True)
    e2.insert(tk.END,order)
    global x
    x=order.split(' ')
    

    
#creating GUI
root= tk.Tk()
root.geometry("300x400")
root.title("Chatbot")
root.configure(bg="black")
e1=tk.Text(root)
l1=tk.Label(root,text="Output:")
l1.place(x=20,y=10)
e1.place(x=20,y=45,height=50,width=180)
e2=tk.Text(root)

l=tk.Label(root,text="-------------------")
l.place(x=20,y=100)
l=tk.Label(root,text="You said:")
l.place(x=20,y=130)
e2.place(x=20,y=160,height=30,width=180)
b1=tk.Button(root,text="Speak",bg="red",fg="white",command=check)
b1.place(x=60,y=210,height=50,width=100)

root.mainloop()

#some pre deined chats
greetings=["Hello","Hi","Hey"]
wish={"Morning":"Good Morning","Night":"Good Night","care":"You Too."}
silly={"love":"I love myself","hate":"lmao,look at your face","children":"Oh please."}
