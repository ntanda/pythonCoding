# la liste delle mosse
import random
# variabile list / cosa abbiamo bisogno nel gioco
mosse = ["sasso", "carta", "forbisce"]

#Si vogliamo stampare e fare alcune azione
# come contare ogni elemente del mosse secondo la sua posizione
# si fa con count; poi quanti sono, si con len
# per elemento a caso si fa con randon.choice(name of the liste)
# in per indicare che un elemente fate parte in un range del mosse for carta in range(mosse)

print(mosse[0]) # -> sasso (si conta da 0 ! cioé l'indice)
print(mosse[2]) # -> forbisce 
print(mosse[-1]) # -> forbisce 
print(len(mosse)) # -> ci sono 3 elementi nel mosse cioe quanti elementi ci sono nella list mosse
print("carta" in mosse) # -> si, True # false
print("piera" in mosse) # -> non, false
print(random.choice(mosse)) # -> un elemente a caso

# La lista della storia dei turni
storia = []   
               
storia.append("vittoria")  
storia.append("sconfitta")
storia.append("vittoria")
print(storia) #['vittoria', 'sconfitta', 'vittoria']
print(len(storia))  # 3 turni giocati secondo il risultato
print(storia.count("vittoria")) # 2 vittorie ## countiamo , 
# Quest serve a calculare il punteggio contando e non salvare come una variabile simplice 
# si fa :
storia.count("vittoria") * 10 

"""
vittorie = storia.count("vittoria")    # conta quante volte c'è "vittoria" -> 2
punteggio = vittorie * 10              # 2 x 10 = 20
opo 3 turni validi, count("vittoria") dà 2 e il punteggio è 20.
"""

# Condizione per giocare fino a 10 torni
while len(storia) < 10:  # ripete finché la lista non ha 10 elementi. Il pareggio non fa	, quindi non conta.
    mossa_umano = input("Fai la tua mossa (sasso, carta, forbisce) : ")
    mossa_umano = mossa_umano.lower().strip() # minuscule o sesìnza spazio
    
    if mossa_umano not in mosse :
        print("\nMossa non valida ! " )
        continue
    
    # Regole del gioco che è nel sistema : il computer mostra casualemente, 
    # poi segnale la partita
 
    mossa_computer = random.choice(mosse) # il computer mostra casualemente gli elementi di gioco
    print(f"Tu : {mossa_umano}, | Computer : {mossa_computer} ")
    
    # Cominciare il gioco 
    if mossa_umano == mossa_computer :
        print("Pareggio, si rigioca il turno")
    elif (mossa_umano == "sasso" and mossa_computer == "forbisce ") or\
         (mossa_umano == "carta" and mossa_computer == "sasso" ) or\
         (mossa_umano == "forbisce" and mossa_computer == "carta") :
        
        print("Hai vinto questo torno ! ")
        storia.append("vittoria ")
    else:
        
        print("Il computer ha vinto questo torno")
        storia.append("sconfitta ")
        
        # Punteggio che vuole dire su 10 torni, quanti volte ha vinto?
        punteggio = storia.count("vittoria ") * 10
        print("Storia dei turni :", storia )
        print(f"Tuo punteggio finale è : {punteggio}/100 ")
        
        
"""
Non servono né   turno += 1	né vittorie += 1 : la lista tiene il conto da sola.
continue torna all’inizio del  ciclo quando la mossa non è valida.
"""
     
        
        
 