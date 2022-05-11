from tkinter import * 
from tkinter import ttk
#Nathan Chiarani - algoritmo cifratura atbash
 
"""
Questi due metodi controllano se la lettera
seguente é maiuscola o minuscola
"""
def isUpperCase(lettera):
    if lettera >= 'A' and lettera <= 'Z':
        return True
    return False

def isLowerCase(lettera):
    if lettera >= 'a' and lettera <= 'z':
        return True
    return False
    
"""
Questo metodo applica algoritmo 
cifratura alla parola:
ABC -> ZYX
"""
def atbash(word):
    lettera = ''
    for i in range(len(word)):
        """
        Controllo se la lettera corrente é 
        maiuscola, se si applico algoritmo
        """
        if isUpperCase(word[i]):
            """
            guarda le singole lettere dell alfabeto e ne trova
            la corrispondenza con l ultima, (uno swap)
            funzione ord restituisce il carattere ASCII
            funzione chr restituisce il carattere dal codice ASCII
            """
            lettera += chr(ord('z') - ord(word[i]) + ord('a'))
        #Controllo se la lettera corrente é minuscola, se si applico algoritmo
        elif isLowerCase(word[i]):
            lettera += chr(ord('z') - ord(word[i]) + ord('a'))
        #mentre se é uno spazio, numero o carattere speciale stampa simboli
        elif word[i].isspace():
                lettera += '❀'
        elif word[i].isnumeric():
                lettera += "❣"
        else:
            lettera += "➹"
    return lettera

class GUI():                              
    def __init__(self):  
        #inizializzazione
        self.root = Tk(className='Chiarani Atbash - Window size')
        self.root.geometry("300x200")
        #background image
        C = Canvas(self.root, bg="blue", height=800, width=800)
        filename = PhotoImage(file = "background.png")
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #testi
        self.testo = StringVar() 
        self.testoC = StringVar()
        self.prevlaue=''
        #entry 
        self.entry = ttk.Entry(self.root, width=40,font="Times 10",textvariable =self.testo)
        self.entry.grid(pady=40,padx=30) 
        self.entry.bind("<KeyRelease>", self.OnEntryClick) #keyup
        self.output = ttk.Entry(self.root,width=40, font="Times 10 overstrike", textvariable =self.testoC)
        self.output.grid(pady=30,padx=30)
        self.root.mainloop()       

    def OnEntryClick(self, event):
        value=self.testo.get().strip()
        changed = True if self.prevlaue != value else False
        self.testoC.set(atbash(value))
        self.prevlaue = value
    
#create the self
GUI()
