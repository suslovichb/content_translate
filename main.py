from tkinter import *
from tkinter import scrolledtext
from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def fix_tags(text):
    text = text.replace('</ ', '</')
    return text

def clicked():
    new_text = fix_tags(translator.translate([txt_original.get(1.0, END)], src='en', dest='uk')[0].text)
    txt_translated.delete(1.0, END)
    txt_translated.insert(1.0, new_text)

window = Tk()
window.title("Content Translate")
window.geometry('500x400')

# lbl = Label(window, text="testlabel1", font=("Arial Bold", 12))
# lbl.grid(column=0, row=0)

txt_original = Text(window, width=50, height=10)
txt_original.grid(column=0, row=1)

btn = Button(window, text="translate", bg = 'grey', fg ='white', command=clicked)
btn.grid(column=1, row=1)

txt_translated = Text(window, width=50, height=10)
txt_translated.grid(column=0, row=16)

window.mainloop()
