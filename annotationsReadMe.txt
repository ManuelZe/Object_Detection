En ce qui concerne le code de "annotations.py" prenez ceci comme explications 
du code
Une bibliothèque d'annotations qui dessine des superpositions sur l'aperçu de
 la caméra Pi.

Les annotations comprennent des cadres de délimitation et des superpositions
 de texte.

Les annotations prennent en charge l'opacité partielle, mais uniquement en ce
 qui concerne le contenu l'aperçu.
Une valeur de remplissage transparente couvrira la superposition précédemment
 dessinée en dessous, mais pas le contenu de la caméra en dessous.
 
Une couleur de None peut être donnée, qui ne couvrira alors pas le contenu de
 superposition dessiné sous la région.
Remarque: Les superpositions ne sont pas prises en charge jusqu'au stockage,
ce qui veut dire que si vous enregistrez une image grâce à la caméra alors
les superpositions ne seront pas visibles.


"def _round_up(value, n) :"

Cette fonction donne la valeur du nombre suivant celui enregistreé, et donc 
la valeur peut être divisible par n.
Le résultat de la valeur arrondie sera un multiple de n
   value : Entier qui sera arrondie
   n : Le nombre qui devra être divisible par la valeur

"def _init_(self, camera,default_color=None)"

Cette fonction arrondie les dimensions de l'image superposée
D'après la documentation de PiCamera.add_overlay, la source de données
(l'image en ce qui nous concerne) doit avoir une largeur arrondie à un multiple 
de 32 et la hauteur à un multiple de 16.
	dims : dimensions de l'image
	retourne les dimensions arrondies dans un tuple.


"def bounding_box(self, rect, outiline=None, fill=None):"

Fonction dessinant une zone delimitant sur un rectangle spécifié

rect (x1, y1, x2, y2) est le rectangle qui sera dessiné où (x1, y1) et 
(x2,y2) seront aux corners opposés du rectangle désiré.
Outline : PIL.ImageColor (bibliothèque) sera utilisé pour dessiner les 
délimitations
fill : PIL.ImageColor quand à lui sera utilisé pour remplir les différents
rectangle de délimitations dessinés.

def text(self, location, text, color=None)

Ecris le texte donné à la position donnée
location : (x, y) endroit auquel nous écriverons le texte (coin supérieur 
geuche)
text : texte qui sera écrit
color : PIL.ImageColor pour dessiner le texte dans le rectangle
