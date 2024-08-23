import datetime
def assistente_virtuale(comando):
    comando = comando.lower()
    if "data" in comando:   # così basterà che l'utente digiti la parola data 
                            # da sola o in una frase e l'assistente darà la data di oggi
                            # sia in maiuscolo che in minuscolo
        oggi = datetime.datetime.now().date()  
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif "ora" in comando:  # stessa cosa che ho fatto per data
        ora_attuale = datetime.datetime.now().time()  
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."  
    return risposta
while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))