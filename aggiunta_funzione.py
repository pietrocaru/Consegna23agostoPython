import datetime
from time import strftime   # qui ho cercato suggerimenti, non sapevo di dover importare anche questo modulo

def datetoday():        # ho creato questa funzione per dare senso a datetoday()
    return strftime("%d/%m/%Y")

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetoday() 
        risposta = "La data di oggi è " + oggi
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()  
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."  
    return risposta
while True:     # qui ho aggiunto i ":" dopo while True
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente)) 