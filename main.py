import pyttsx3
import PyPDF2
from tkinter.filedialog import *
import threading

# reading function
def pdf_read(pdfreader, pages, stop_event):
    player = pyttsx3.init()
    for num in range(pages):
        if stop_event.is_set():
            break
        page = pdfreader.pages[num]
        text = page.extract_text()
        player.say(text)
        player.runAndWait()

# stop reading function
def stop_read():
    input("'Enter' to stop the reading.\n")
    stop_event.set()  # Activer le signal d'arrêt

# pdf selection
book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# stop event creation
stop_event = threading.Event()

# separated thread
thread = threading.Thread(target=pdf_read, args=(pdfreader, pages, stop_event))
thread.start()

# reading stop in main thread
stop_read()

# waiting for the thread to end
thread.join()