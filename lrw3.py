import re # librerie Regular_Expression (expressions reguliere
Texte="La blablablamation est importante pour les blablameurs. Apprenez a' blamer avec une manette!"


# procedure de remplacement d'une expression reguliere par un texte: re.sub(Expression_Reguliere_Du_texte_a_remplac%e9,Texte_de_remplacement,Texte)
# Expression_Reguliere_Du_texte_a_remplac%e9="(bla)+" [bla se repete une ou plusieurs fois]
Texte_de_remplacement = "program"
Texte="La blablablamation est importante pour les blablameurs. Je blame avec une manette!"

# re.sub retoutre le texte apres substitution


Texte_Apres_Remplacement=re.sub("(bla)+","program",Texte)
#print (Texte_Apres_Remplacement)

import urllib
import urllib.request as urllib2
# Ouvrir le fichier contenant la page index.html
fichier=open("index.html","rb")
contenu_fichier=""
# Lecture du contenu du fichier
for ligne in fichier:
    contenu_fichier+=ligne.decode("unicode_escape")
fichier.close()
# rechercher toutes les occurence dans le texte de la forme "[^"]+\.css"|"[^"]+\.
# '.' (point) == nimporte quel caractere ('\.' reference le caractere point)
# | == OU logique (exemple "[^"]+\.css"|"[^"]+\.js"|"[^"]+\.png" signifie "[^"]
# [^"] == touts cractere sauf '"'
# [^"]+ == suite de caracteres ne contenant pas le cracatere '"'
matches=re.findall('"[^"]+\.css"|"[^"]+\.js"|"[^"]+\.png"',contenu_fichier,re.M)
# re.M == recherche Multilignes
nv=""

#modifier

for r in matches :
    print(r)

