import sys
import os
import time
suddivisione_raee = {
    "R1-Grande bianco freddo": ["frigorifero", "congelatore", "condizionatore", "frigorifero doppia porta",
        "frigorifero side-by-side", "frigorifero combinato", "frigorifero da incasso"],







    "R2-Grande bianco non freddo": ["lavatrice", "lavastoviglie", "forno",
        "piano cottura", "cappa aspirante", "scaldabagno",
        "friggitrice", "forno a microonde", "piano induzione",
        "cucina a gas", "forno a vapore", "termoconvettore",
        "caldaia", "stufa a pellet", "aspirapolvere centralizzato",
        "robot aspirapolvere"],







    "R3-TV Monitor a tubo catodico": ["tv", "monitor", "televisore CRT"],








    "R4-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici": ["frullatore", "macchina per il caffè", "bollitore elettrico",
        "robot da cucina", "aspirapolvere", "ferro da stiro", "phon",
        "bilancia da cucina", "spremiagrumi",
        "macchina per il pane",
        "macchina per la pasta",
        "tostapane a muffin", 
        "stampante",
        "telefono fisso", "tastiera e mouse",
        "altoparlanti per pc", "microfono",
        "scheda grafica",
        "custodia per laptop",
        "lampadario", "lampada da tavolo", "lampada a sospensione",
        "faretti",
        "lampada da lettura", "luce notturna",
        "lampada da soffitto",
        "misuratore di pressione sanguigna", "bilancia pesapersone",
        "elettrocardiografo portatile",
        "monitor per la glicemia",
        "aspiratore di secrezioni",
        "monitor per il sonno",
        "apparecchio per la terapia del dolore",
        "termometro auricolare",
        "sonda per ecografia", "monitor per la frequenza cardiaca",
        "defibrillatore portatile",
        "stimolatore cardiaco esterno"],







    "R5-Sorgenti luminose a scarica": ["lampade fluorescenti", "sorgenti luminose"]
}




def puliscischermo():
    os.system("cls")



def menu():
    continuare = "si"
    while continuare == "si":
        print("Seleziona un'opzione:")
        print("1. Visualizza la lista di di rifiuti RAEE")
        print("2. Smista i rifiuti per categoria RAEE")
        print("3. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            stampa()
            time.sleep(6)
            puliscischermo()
            continuare = input("inserire si per continuare, oppure qualsiasi altro tasto per terminare: ")
        elif scelta == "2":
            suddividi_rifiuto()
            time.sleep(6)
            puliscischermo()
            continuare = input("inserire si per continuare, oppure qualsiasi altro tasto per terminare: ")
        elif scelta == "3":
            sys.exit()
            
        else:
            print("Errore, Riprova")



def stampa():
    for categoria, oggetti in suddivisione_raee.items():                  #restituire l'elenco con tutte le chiavi del dizionario con valori
        print(f"{categoria}:")
        for oggetto in oggetti:
            print(f"- {oggetto}")
        


def suddividi_rifiuto():
    raee = input("Che rifiuto vuoi smistare: ")
    raee = raee.lower()
    categoria = 0                                    # Rinominazione della variabile

    for categoria, oggetti in suddivisione_raee.items():
        if raee in oggetti:
            categoria = categoria
            break

    if categoria:
        print(f"\nL'oggetto {raee} appartiene alla categoria {categoria} \n")
    else:
        print("\nL'oggetto inserito non corrisponde a nessuna categoria RAEE. \n")



#------------------------main----------------------------------

menu()