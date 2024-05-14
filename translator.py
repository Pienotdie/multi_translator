from googletrans import Translator

import tkinter as tk


class GUI:
    def __init__(self):

        self.translater = Translator()

        self.root = tk.Tk()
        self.root.title("Translater")
        self.root.geometry("800x700")

        self.text_1 = tk.Text(self.root, height=10)
        self.text_1.place(relx=0, rely=0, relwidth=1)

        self.var_1 = tk.IntVar()
        self.var_2 = tk.IntVar()
        self.var_3 = tk.IntVar()
        self.var_4 = tk.IntVar()
        self.var_5 = tk.IntVar()
        self.var_6 = tk.IntVar()

        self.languages = {'ar': self.var_1, 'fr': self.var_2, 'uk': self.var_3,
                          'ps': self.var_4, 'tr': self.var_5, 'ru': self.var_6}

        self.chk_1 = tk.Checkbutton(self.root, text='arabic', variable=self.var_1)
        self.chk_2 = tk.Checkbutton(self.root, text='french', variable=self.var_2)
        self.chk_3 = tk.Checkbutton(self.root, text='ukrainian', variable=self.var_3)
        self.chk_4 = tk.Checkbutton(self.root, text='pashto', variable=self.var_4)
        self.chk_5 = tk.Checkbutton(self.root, text='türkish', variable=self.var_5)
        self.chk_6 = tk.Checkbutton(self.root, text='russian', variable=self.var_6)

        self.chk_1.place(relx=0.1, rely=0.4, relwidth=0.1)
        self.chk_2.place(relx=0.1, rely=0.5, relwidth=0.1)
        self.chk_3.place(relx=0.1, rely=0.6, relwidth=0.1)
        self.chk_4.place(relx=0.2, rely=0.4, relwidth=0.1)
        self.chk_5.place(relx=0.2, rely=0.5, relwidth=0.1)
        self.chk_6.place(relx=0.2, rely=0.6, relwidth=0.1)

        self.button = tk.Button(self.root, text='Translate', command=self.to_translate)
        self.button.place(relx=0.3, rely=0.3, relwidth=0.1)

        self.text_2 = tk.Text(self.root, height=10)
        self.text_2.place(relx=0, rely=0.77, relwidth=1)

        self.button = tk.Button(self.root, text='Clear', command=self.clear)
        self.button.place(relx=0.5, rely=0.3, relwidth=0.1)

        self.root.mainloop()

    def to_translate(self):
        for lg, v in self.languages.items():
            if v.get():
                self.text_2.insert(tk.END, self.translater.translate(self.text_1.get('1.0', tk.END),
                                                                     dest=lg).text + '\n')

    def clear(self):
        self.text_2.delete('1.0', tk.END)


GUI()

# 'ar': 'arabic'
# 'fr': 'french'
# 'de': 'german'
# 'ps': 'pashto'
# 'fa': 'persian'
# 'ru': 'russian'
# 'uk': 'ukrainian'
