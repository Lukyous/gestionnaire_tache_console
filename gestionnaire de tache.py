import datetime
import subprocess
import os

try:
    os.mkdir(r"C:\Program Files\Gestionnaire_de_tache")
except Exception as e:
    if "Access is denied" in str(e):
        print("Accès non autorisé.")
    else:
        pass
try:
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        tache = folder.readlines()
except:
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "w") as folder:
        folder.write(" ")

def voir_tache():
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        tache = folder.readlines()
    if tache == []:
        print("+-------------------------------+")
        print("| Aucune tache n'a été trouvée. |")
        print("+-------------------------------+")
        return
    for i in tache:
        print(f"{i.replace('-T', '').replace('-t', '|').replace('heure = ', '| créé le ').replace('delais = ', '| Etat: ')}", end="", flush="")

def ajout_tache(texte):
    now = datetime.datetime.now()
    heure = now.strftime("%d/%m/%Y %H:%M:%S")
    if "-T" and "-t" not in texte:
        print("Vous ne pouvez pas ajouter cette tache car elle manque du titre et du texte.")
        return
    if "-T" not in texte:
        print("Vous ne pouvez pas ajouter cette tache car elle manque d'un titre.")
        return
    if "-t" not in texte:
        print("Vous ne pouvez pas ajouter cette tache car elle manque d'un texte.")
        return
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        tache = folder.readlines()
        nombre = len(tache)
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "a") as folder:
        folder.write(f"{nombre+1}) {texte} heure = {heure} delais = [en cours]\n")
        print("La tache a été ajouté.")

def etat_change(numero, choix="en cours"):
    numero = str(numero)+")"
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        tache = folder.readlines()
    for i in tache:
        if numero in i:
            ind = tache.index(i)
            etat = i.split("[")
            etat = etat[-1]
            etat = etat.strip("]\n")
            i = i.replace(etat, choix)
            tache[ind] = i
            with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "w") as folder:
                folder.write("")
            with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "a") as folder:
                for i in tache:
                    folder.write(i)

def supprime_tache(*args):
    wox = []
    for ju in args:
        for wo in ju.strip():
            if wo != "" and wo != " ":
                wo = str(wo)
                wox.append(wo)
    j=1
    lst= []
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        tache = folder.readlines()
    for i in wox:
        i = str(i)+")"
        for u in tache:
            if i in u:
                del tache[tache.index(u)]
                with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "w") as folder:
                    folder.write("")
                with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "a") as folder:
                    for x in tache:
                        folder.write(x)
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "r") as folder:
        m = folder.readlines()
        for a in m:
            a = a.replace(a[0], str(j))
            j+=1
            lst.append(a)
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "w") as folder:
        folder.write("")
    with open(r"C:\Program Files\Gestionnaire_de_tache\tache.txt", "a") as folder:
        for x in lst:
            folder.write(x)

while True:
    commande = input("gestionnaire--> ").strip()
    if commande == "help":
        print("""\n
help                        afficher les commandes
ajout -T titre -t texte     ajouter une tache.
supprime 2                  Pour supprimer la tache 2
supprime 2 3 5 6            Pour supprimer les taches 2, 3, 5, 6.
voir                        Pour voir les taches.
etat 1 en suspens           Pour changer l'état de la tache 1 de
                            en cours à en suspens.
cls                         supprime l'historique du terminal.\n""")
    elif "ajout" in commande:
        commande = commande.lstrip("ajout")
        print()
        ajout_tache(commande)
        print()
    elif "supprime" in commande.lower():
        commande = commande.lstrip("supprime")
        supprime_tache(commande)
    elif commande.lower() == "voir":
        print("")
        voir_tache()
        print("\n")
    elif "etat" in commande:
        commande = commande.lstrip("etat")
        ls = commande.split()
        numero = ls[0]
        del ls[0]
        choix = " ".join(ls)
        etat_change(numero, choix)
    elif commande.lower() == "cls":
        subprocess.run("cls", shell=True)
