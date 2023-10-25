from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

LT = Tk()
LT.geometry('1345x705')

LT.resizable(0, 0)
LT.config(bg='#E8F4F8')
LT.title("Language Translator (GUI Based)")


a = Label(LT, text="LANGUAGE TRANSLATOR", font="Helvetica 50 bold underline", pady=25, bg='#E8F4F8', fg='#000000')\
    .pack()
b = Label(LT, text="By - Umang Tilokani", font='Helvetica 25 bold', pady=15, bg='#E8F4F8', fg='#000000')\
    .pack(side='bottom')
c = Label(LT, text="Enter Text", font='Helvetica 30 bold', bg='#E8F4F8', fg='#000000').place(x=205, y=150)

Input_text = Text(LT, font='Helvetica 25 bold', height=10, wrap=WORD, padx=5, pady=5, width=35,
                  bg='#E8F4F8', fg='#008000')
Input_text.place(x=45, y=285)

d = Label(LT, text="Translation", font='Helvetica 30 bold', bg='#E8F4F8', fg='#000000').place(x=975, y=150)

Output_text = Text(LT, font='Helvetica 25 bold', height=10, wrap=WORD, padx=5, pady=5, width=35,
                   bg='#E8F4F8', fg='#DC143C')
Output_text.place(x=800, y=285)
language = list(LANGUAGES.values())

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="#D3D3D3")
src_lang = ttk.Combobox(LT, font='Helvetica 20', values=language, width=20)
src_lang.place(x=147, y=220)
src_lang.set('Select Input Language')

dest_lang = ttk.Combobox(LT, font='Helvetica 20', values=language, width=20)
dest_lang.place(x=925, y=220)
dest_lang.set('Select Output Language')


def translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)


trans_btn = Button(LT, text='CLICK TO TRANSLATE', font='Helvetica 15 bold', command=translate,
                   highlightbackground="#0F52BA", highlightthickness=2)
trans_btn.place(x=576, y=420)

LT.mainloop()
