from googletrans import Translator
import customtkinter as ct


class GUI:
    def __init__(self):

        self.translater = Translator()

        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("green")
        self.root = ct.CTk()
        self.root.title("Translater")
        self.root.geometry("800x600")

        self.text_1 = ct.CTkEntry(self.root, height=67,
                                  placeholder_text="Enter your text",
                                  width=700,
                                  border_width=2,
                                  corner_radius=20)
        self.text_1.place(relx=0.5, rely=0.1, anchor='center')

        self.var_ar = ct.IntVar()
        self.var_fr = ct.IntVar()
        self.var_uk = ct.IntVar()
        self.var_ps = ct.IntVar()
        self.var_tr = ct.IntVar()
        self.var_fa = ct.IntVar()
        self.var_ur = ct.IntVar()
        self.var_es = ct.IntVar()
        self.var_ru = ct.IntVar()

        self.languages = {'ar': self.var_ar, 'fr': self.var_fr, 'uk': self.var_uk,
                          'ps': self.var_ps, 'tr': self.var_tr, 'fa': self.var_fa,
                          'ur': self.var_ur, 'es': self.var_es, 'ru': self.var_ru}

        self.chk_ar = ct.CTkCheckBox(self.root, text='arabic', variable=self.var_ar, corner_radius=50)
        self.chk_fr = ct.CTkCheckBox(self.root, text='french', variable=self.var_fr, corner_radius=50)
        self.chk_uk = ct.CTkCheckBox(self.root, text='ukrainian', variable=self.var_uk, corner_radius=50)
        self.chk_ps = ct.CTkCheckBox(self.root, text='pashto', variable=self.var_ps, corner_radius=50)
        self.chk_tr = ct.CTkCheckBox(self.root, text='türkish', variable=self.var_tr, corner_radius=50)
        self.chk_fa = ct.CTkCheckBox(self.root, text='persian', variable=self.var_fa, corner_radius=50)
        self.chk_ur = ct.CTkCheckBox(self.root, text='urdu', variable=self.var_ur, corner_radius=50)
        self.chk_es = ct.CTkCheckBox(self.root, text='spanish', variable=self.var_es, corner_radius=50)
        self.chk_ru = ct.CTkCheckBox(self.root, text='russian', variable=self.var_ru, corner_radius=50)

        self.chk_ar.place(relx=0.1, rely=0.35, relwidth=0.2)
        self.chk_fr.place(relx=0.1, rely=0.45, relwidth=0.2)
        self.chk_uk.place(relx=0.1, rely=0.55, relwidth=0.2)
        self.chk_ps.place(relx=0.3, rely=0.35, relwidth=0.2)
        self.chk_tr.place(relx=0.3, rely=0.45, relwidth=0.2)
        self.chk_fa.place(relx=0.3, rely=0.55, relwidth=0.2)
        self.chk_ur.place(relx=0.5, rely=0.35, relwidth=0.2)
        self.chk_es.place(relx=0.5, rely=0.45, relwidth=0.2)
        self.chk_ru.place(relx=0.5, rely=0.55, relwidth=0.2)

        self.button = ct.CTkButton(self.root, text='Translate', command=self.to_translate, corner_radius=20)
        self.button.place(relx=0.35, rely=0.2, relwidth=0.11)

        self.text_2 = ct.CTkTextbox(self.root, height=150, width=700, border_width=2, corner_radius=20)
        self.text_2.place(relx=0.5, rely=0.77, anchor='center')

        self.button = ct.CTkButton(self.root, text='Clear', command=self.clear, corner_radius=20)
        self.button.place(relx=0.55, rely=0.2, relwidth=0.1)

    def to_translate(self):
        for lg, v in self.languages.items():
            if v.get():
                self.text_2.insert(ct.END, self.translater.translate(self.text_1.get(), dest=lg).text + '\n')

    def clear(self):
        self.text_2.delete('0.0', ct.END)


if __name__ == "__main__":
    app = GUI()
    app.root.mainloop()

# 'ar': 'arabic'
# 'fr': 'french'
# 'de': 'german'
# 'ps': 'pashto'
# 'fa': 'persian'
# 'ru': 'russian'
# 'uk': 'ukrainian'
# 'ur': 'urdu'
