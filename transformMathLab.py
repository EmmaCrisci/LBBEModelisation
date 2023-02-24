#lien vers le fichier
lien= "C:/Emma/Stage_GB5_LBBE/FinalModels"
nomFichier = "/flux_noDrugs.m"
######################

## Fonctions ##

def ouvertureFichier(lien,nomFichier):
    fichier = open(lien+nomFichier, 'r')
    lignes = fichier.readlines()
    fichier.close
    return lignes

def ecritureFichier(lien,nomFichier,contenu):
    fichier=open(lien+nomFichier+"_modifs.m", 'w')
    fichier.write(contenu)
    fichier.close
################

#                                                1. Ouverture du fichier
contenu = ouvertureFichier(lien,nomFichier)

### à changer par l'utilisateur ###
nbLignesEntete = 1 # Nombres de lignes dans l'entête
separateurPartie1="\n" # délimiteur avec la partie des équation différentielles
separateurPartie2="%step 1: rate laws\n"
###################################

# Initialisation des Variables
Parametres={"vm":[],"km":[],"V_":[],"ka":[],"al":[],"be":[],"ki":[]} # couple nom valeur
EquaDiff={}
fin=0
ordreReact=[]


replacement1="x("

#                                               2. Récupérer les informations du fichier et ranger sous forme adhéquate
for l in range(len(contenu)):
    ligne = contenu[l]
    #print(ligne)
    if ligne == separateurPartie1:
        fin=1
    
    ###  Récupération des paramètres  ###
    if l >= nbLignesEntete and fin == 0 : # on est pas dans l'entête et la première partie
        ligne=ligne.rstrip()
        couple = ligne.split(" = ")

        #print(couple)
        nomParametre = couple [0]

        valeurParametre = couple[-1]
        valeurParametre = valeurParametre[:-1]
        valeurParametre.rstrip()

        initiales = nomParametre[0:2]
        if initiales in Parametres.keys():
            Parametres[initiales]+= [[nomParametre,valeurParametre]]
    
    if l >= nbLignesEntete and fin==2 : # On est dans la partie des équations différentielles
        ligne=ligne[:-1] # enlever ; à la fin
        ligneDecoup=ligne.split(" = ") 
        
        ordreReact += ligneDecoup[0]
        equation= ligneDecoup[1]
        
        EquaDiff[ligneDecoup[0]] = equation

    if ligne == separateurPartie2 :
        fin= 2
    #print(fin)

    ###  Récupération des équtions différentielles  ###
print(contenu)
# print (Parametres) # validé
print(EquaDiff)
print(ordreReact)
# Gestion des équations différentielles





#                                                3. Mise dans un fichier sous forme R
contenuSortie=""
for key in Parametres :
    contenuSortie += "\n"+key+"<- c("
    for information in Parametres[key]:
        contenuSortie = contenuSortie + information[1]+","
    contenuSortie = contenuSortie[:-1] + ") \nname_"+key+" <- c("
    for information in Parametres[key]:  
        contenuSortie = contenuSortie +"'"+information[0]+"',"
    contenuSortie = contenuSortie[:-1] + ") \nt"+key+" <- t(data.frame("+key+"))\ncolnames(t"+key+")=name_"+key
contenuSortie += "\n"

for key in EquaDiff :
    contenuSortie += key+ ","
contenuSortie += "\nc("   
for key in EquaDiff :
    contenuSortie += EquaDiff[key]+ ","
contenuSortie = contenuSortie[:-1] + ") \n"
#print(contenuSortie)
ecritureFichier(lien, nomFichier, contenuSortie)




 




        



