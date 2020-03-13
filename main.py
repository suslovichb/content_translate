from tkinter import *
from tkinter import scrolledtext
from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def fix_tags(text):
    text = text.replace('</ ', '</')
    text = text.replace(' <', '<')
    text = text.replace('> ', '>')
    return text

def translate(event=None):
    new_text = fix_tags(translator.translate([txt_original.get(1.0, END)], src=src_lang.get(), dest=dest_lang.get())[0].text)
    txt_translated.delete(1.0, END)
    txt_translated.insert(1.0, new_text)

window = Tk()
window.title("Content Translate")
window.geometry('600x500')
window.bind('<Return>', translate)

src_lang = StringVar()
dest_lang =StringVar()

src_ru = Radiobutton(text="RU", variable=src_lang, value='ru')
src_uk = Radiobutton(text="UK", variable=src_lang, value='uk')
src_en = Radiobutton(text="EN", variable=src_lang, value='en')
src_ru.place(relx=0.01, rely=0)
src_uk.place(relx=0.21, rely=0)
src_en.place(relx=0.41, rely=0)
src_lang.set('ru')

txt_original = Text(window, width=50, height=12)
txt_original.place(relx=0.01, rely=0.05)
txt_original.bind('<Return>', translate)

btn = Button(window, text="translate", bg = 'grey', fg ='white', command=translate)
btn.place(relx=0.8, rely=0.05)

dest_ru = Radiobutton(text="RU", variable=dest_lang, value='ru')
dest_uk = Radiobutton(text="UK", variable=dest_lang, value='uk')
dest_en = Radiobutton(text="EN", variable=dest_lang, value='en')
dest_ru.place(relx=0.01, rely=0.45)
dest_uk.place(relx=0.21, rely=0.45)
dest_en.place(relx=0.41, rely=0.45)
dest_lang.set('uk')

txt_translated = Text(window, width=50, height=12)
txt_translated.place(relx=0.01, rely=0.5)

window.mainloop()
