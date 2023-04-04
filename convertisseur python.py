from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

convertisseur = Tk()
convertisseur.title("Convertisseur de monnaie")
convertisseur.geometry("380x380")

OPTIONS = {
    "EUR":1,
    "USD":1.08,
    "JPY":139.21,
    "CAD":0.69,
    "AUD":0.65,
}



def ok():
    prixx = prix.get()
    if not prixx:
        messagebox.showerror("Erreur", "Entrez une valeur correcte")
        return
    if not prixx.isdigit():
        messagebox.showerror("Erreur", "Chiffre/nombre, pas de lettres...")
        return
    qst = variable1.get()
    qst2 = variable2.get()
    DICT = OPTIONS.get(qst,None)
    DICT2 = OPTIONS.get(qst2,None)
    convertis = round(float(DICT2)*float(prixx)/float(DICT),2)
    resultat.config(state='normal')
    resultat.delete(1.0,END)
    resultat.insert(INSERT,prixx,INSERT," ",INSERT,qst,INSERT," = ",INSERT,convertis,INSERT," ",INSERT,qst2)
    resultat.config(state='disabled')
 


nomApp = Label(convertisseur,text="CONVERTISSEUR DE MONNAIE",font=("arial",15,"bold"),fg="black")
nomApp.place(x=40, y=100)

resultat = Text(convertisseur,height=3,width=30,font=("arial",10,"bold"),bd=5,state='disabled')
resultat.place(x=70, y=300)

fr = Label(convertisseur,text="VALEUR :",font=("arial",10,"bold"),fg="black")
fr.place(x=10, y=165)

prix = Entry(convertisseur,font=("arial",10))
prix.place(x=125, y=160,height=30,width=120)

choix = Label(convertisseur,text="DE :",font=("arial",10),fg="black")
choix.place(x=5, y=220)

variable1 = StringVar(convertisseur)
variable1.set(None)
option = OptionMenu(convertisseur, variable1, *OPTIONS.keys())
option.place(x=35 , y=210,width=100, height=40)

choix2 = Label(convertisseur,text="VERS :",font=("arial",10),fg="black")
choix2.place(x=180, y=220)

variable2 = StringVar(convertisseur)
variable2.set(None)
option2 = OptionMenu(convertisseur, variable2, *OPTIONS.keys())
option2.place(x=230 , y=210,width=100, height=40)

boutton = Button(convertisseur,text="CONVERTIR",fg="black",font=("arial",16),bg="grey",command=ok)
boutton.place(x=105, y=260,height=40,width=150)



convertisseur.mainloop()