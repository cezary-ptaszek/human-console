import speech_recognition as sr
from selenium import webdriver
import re
import time
import os
import subprocess
import ctypes


def questionAndAnswer(question):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(question)
        audio = r.listen(source)
    answer = r.recognize_google(audio)
    print("You: " + answer)
    return answer


def anyQuestion(action, sth, q):
    return re.search(r'^.*' + action + '.*' + sth + '.*', q)


ques = questionAndAnswer("Hi there! What can I do for you?")

# inne akcje
# otwieranie Chroma
if anyQuestion("start", "Chrome", ques) or anyQuestion("open", "Chrome", ques) or anyQuestion("run", "Chrome", ques):
    q = questionAndAnswer("Sure, what website do you want to open (Youtube, Google)?")
    time.sleep(0.5)
    if anyQuestion("", "YouTube", q):
        q1 = questionAndAnswer("Ok, enter the search phrase, please.")
        time.sleep(0.5)
        print("Got it!")
        driver = webdriver.Chrome(executable_path=r'C:\Users\Cerciak\Downloads\chromedriver.exe')
        driver.get("https://www.youtube.com/results?search_query=" + q1)
        driver.find_element_by_xpath('.//*[@id="contents"]/ytd-video-renderer[1]').click()
    elif anyQuestion("", "Google", q):
        q1 = questionAndAnswer("Ok, enter the search phrase, please.")
        time.sleep(0.5)
        print("Got it!")
        driver = webdriver.Chrome(executable_path=r'C:\Users\Cerciak\Downloads\chromedriver.exe')
        driver.get("https://www.google.com/search?q=" + q1)

elif anyQuestion("", "log out", ques) or anyQuestion("", "log off", ques):
    print("   _____                 _ _                _ ")
    print("  / ____|               | | |              | |")
    print(" | |  __  ___   ___   __| | |__  _   _  ___| |")
    print(" | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |")
    print(" | |__| | (_) | (_) | (_| | |_) | |_| |  __/_|")
    print("  \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)")
    print("                                  __/ |       ")
    print("                                 |___/        ")
    time.sleep(1)
    os.system("shutdown -l")

elif anyQuestion("", "lock", ques):
    ctypes.windll.user32.LockWorkStation()

elif anyQuestion("push", "GitHub", ques) or anyQuestion("", "GitHub", ques):
    subprocess.call(['gitpush.bat'])

# otwieranie pliku
elif anyQuestion("open", "text file", ques):
    q = questionAndAnswer("Ok, what is the name of file?")
    print("Got it!")
    os.startfile(q + ".txt")
elif anyQuestion("open", "doc file", ques):
    q = questionAndAnswer("Ok, what is the name of file?")
    print("Got it!")
    os.startfile(q + ".docx")
elif anyQuestion("open", "PDF file", ques):
    q = questionAndAnswer("Ok, what is the name of file?")
    print("Got it!")
    os.startfile(q + ".docx")

# otwieranie aplikacji
elif anyQuestion("open", "program", ques) or anyQuestion("run", "program", ques) or anyQuestion("start", "program", ques):
    q = questionAndAnswer("Ok, what is the name of program?")
    if anyQuestion("", "C plus", q) or anyQuestion("", "cplusplus", q) or anyQuestion("", "C++", q):
        print("Got it!")
        subprocess.call(['C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'])
    elif anyQuestion("", "gif", q):
        print("Got it!")
        subprocess.call(['C:\\Program Files (x86)\\ScreenToGif\\ScreenToGif.exe'])

# zamykanie aplikacji
elif anyQuestion("close", "program", ques) or anyQuestion("exit", "program", ques) or anyQuestion("kill", "program", ques):
    q = questionAndAnswer("Ok, what is the name of program?")
    if anyQuestion("", "C plus", q) or anyQuestion("", "cplusplus", q) or anyQuestion("", "C++", q):
        print("Got it!")
        os.system("TASKKILL /F /IM devcpp.exe")
    elif anyQuestion("", "gif", q):
        print("Got it!")
        os.system("TASKKILL /F /IM ScreenToGif.exe")
    elif anyQuestion("", "Chrome", q):
        print("Got it!")
        os.system("TASKKILL /F /IM chrome.exe")


# otwieranie strony
elif anyQuestion("", "website", ques) or anyQuestion("", "web", ques):
    q1 = questionAndAnswer("Ok, enter the search phrase, please.")
    time.sleep(0.5)
    print("Got it!")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Cerciak\Downloads\chromedriver.exe')
    driver.get("https://www." + q1)

else:
    print("nie mam takiej odpowiedzi")
