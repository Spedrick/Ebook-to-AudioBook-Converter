import pyttsx3
import pyPDF2

book = open('ebook.pdf','rb')
pdfReader = pyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

print('The Book comprises ',pages,' pages')
startPage = int(input('Which page you want to start from: '))

if startPage > pages or startPage <= 0:
  while(startPage <= pages and startPage > 0):
    startPage = int(input('Please Enter a valid Page number:- '))

for num in range(startPage, pages):
  page = pdfReader.getPage(num)
  text = page.extractText()
  speaker.say(text)
  speaker.runAndWait()
