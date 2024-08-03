#librería
import google.generativeai as genai
import os
import tkinter as tk
from tkinter import scrolledtext

#API KEY
API_KEY = 'AIzaSyBNiA04cDNQ0f4lVMoKSAhPUsW6xQDmkaE'
genai.configure(api_key=API_KEY)

#Set tk window
root = tk.Tk()
root.title('Chatbot')
root.geometry('800x600')

#Chat log
log = scrolledtext.ScrolledText(root, width=100, height=30, state='disabled')
log.pack()
#input field
entry = tk.Entry(root, width=50)
entry.pack()

#modelo elegido
model = genai.GenerativeModel('gemini-1.5-flash', 
                                  generation_config=genai.GenerationConfig(
                                  max_output_tokens=1000,
                                  temperature=0,))
#chat
chat = model.start_chat(history=[])

#Función para enviar mensaje
def enviar():
    #set entry
    msg = entry.get()
    entry.delete(0, tk.END)
    log.config(state='normal')
    log.insert(tk.END, 'User: ' + msg + "\n")

    #Response
    response = chat.send_message(msg)
    log.insert(tk.END, 'Gemini: ' + response + "\n")
    log.config(state='disabled')
    log.yview(tk.END)

#Botón
send_button = tk.Button(root, text='Send', command=enviar)
send_button.pack()

#Iniciar tkinter
root.mainloop()