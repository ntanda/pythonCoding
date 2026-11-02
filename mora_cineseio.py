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
while len(storia) < 10:
    mossa_umano = input("Fai la tua mossa (sasso, carta, forbisce) : ")
    mossa_umano = mossa_umano.lower().strip() # minuscule o sesìnza spazio
    
    if mossa_umano not in mosse :
        print("\nMossa non valida ! " )
        continue
    
    # Regole del gioco che è nel sistema : il computer mostra casualemente, 
    # poi segnale la partita
 
    mosaa_computer = random.choice(mosse) # il computer mostra casualemente gli elementi di gioco
    print(f"Tu : {mossa_umano}, | Computer : {mosaa_computer} ")
    
    # Azione del gioco
    


"""
Pratica Git and GitHub
A. Git in local sul computer

1. creo una cartella repository del progetto in local e sapere dove l'ho messo. 
il nome è pythonCoding e si trova nel Documents
2. Vado scrivere sul terminal per posizionarmi prima su Documents con cd , 
poi posizionarmi su pythonCoding cartella progetto
poi, creo un cartela repository su local con git init -> 
poi faccio git status per vedere i miei file
poi, faccio git add mora_cineseio, cioé il nome del file
poi, faccio git commit -m "commentari" . e posso farlo direttamente nel VS con + e message e commit
poi, Vedere tutti i commit già nella cronologia: faccio git log --oneline

B. GitHub remote online
2. creo un cartella repository del progetto online che è questa copia che sta in local
- vado nel mio account GìtHub ntanda, e creo primo il nuovo repository e la descrizione
- poi, faccio collegare il repository in local a questo che è online 
tramite questo commande : git remote add origin https://github.com/ntanda/pythonCoding
- poi, per Verificare il collegamento se è riuscito tra local e online . git remote -v
per sapere che il collegamente è andato bene si vede questo fetch e push :
origin  https://github.com/ntanda/pythonCoding (fetch)
origin  https://github.com/ntanda/pythonCoding (push)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Primo push su GitHub

Dobbiamo sapere che il git push invia i commit locali al repository remoto. 
Ma è solo l'opzione -u che crea questo collegamento tra il branch locale main e 
il branch remoto origin/main che si fa dal command : git push -u origin

E doppo questa prima configurazione collegata con -u tramite il command : git push -u origin
 che facciamo il primo push del cartella repository local online.
E per i push successivi basta il command : git push.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


** Ma prima di fare questo push -u, dobbiamo verificare che il main di GitHUb online corrisponde 
con main in local, or in local si chiama Head master.
Cosa fare? Cambiamo il Head master al main con il command : 
Soluzione: rinominare il branch locale in main, poi rifare il push:

1. git branch -M main
2. git push -u origin main
3. git push


"""