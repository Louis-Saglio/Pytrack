# Raid : Brainfuck
Pour ce raid vous devrez développer un interpréteur Brainfuck.  
Les règles de ce langage sont très simples :  
On commence avec une tableau de nombre de taille 30000 dont les valeurs sont toutes initialisées à 0.  
On a également un variable appellée "pointeur" qui est un nombre initialisé à 0.  
Brainfuck ne propose que 8 instructions qui permettent de faire des opérations sur le tableau et le pointeur :
* `>` augmente la valeur du pointeur de 1. Si la valeur du pointeur est égale à la taille du tableau alors il revient à 0.
* `<` diminue la valeur du pointeur de 1. Si le pointeur arrive à -1 alors on lui assigne immédiatement la valeur `taille_du_tableau - 1`
* `+` augmente de 1 la case du tableau à l'index `pointeur`. Si une case atteint la valeur 256 alors on lui assigne immédiatement la valeur 0 (le tableau stocke en réalité des octets)
* `-` diminue de 1 la case du tableau à l'index `pointeur`. Si un case atteint la valeur -1 alors on lui assigne immédiatement la valeur 255
* `[` si la valeur de la case à l'indexe `pointeur` est différente de 0 alors on passe à l'instruction suivante. Sinon on saute à l'instruction après le `]` correspondant. (Attention au `[` imbriqués !)
* `]` revient à l'instruction `[` correspondante
* `.` affiche le caractère ASCII dont le code correspond à la valeur de la case du tableau à l'indexe `pointeur`
* `,` la case du tableau à l'indexe `pointeur` prend la valeur du code ASCII de la valeur entrée par l'utilisateur

Théoriquement la taille du tableau doit être 30000, pour les besoins de cette exercice un tableau de taille 100 suffira emplement.


Votre mission consiste à développer une fonction `main` qui prend en paramètre une string correspondant à une suite d'instructions Brainfuck valide et qui retourne la liste des caractères ASCII retournés par l'instruction Brainfuck `.` sous forme de string.  
Par exemple :
```python
def main(src):
    """Votre code"""


src = """>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+."""
main(src)
# returns "Hello, World!"
```
## Bonus
Développez une fonction `detect` qui prend en entrée une suite d'instruction Brainfuck sous forme de string et qui renvoi True si ce code source contient une boucle infinie et False sinon ;)
## Resources
http://brainfuck.org/brainfuck.html
