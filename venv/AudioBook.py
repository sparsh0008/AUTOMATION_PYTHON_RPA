import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader

book = open("Seminar Topics.pdf", "rb")
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
print("Number of pages - ", pages)

speaker = pyttsx3.init()
for i in range(pages):
    print("Reading Page - ", i + 1)
    page = reader.pages[i]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
