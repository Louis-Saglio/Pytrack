## Les variables et types de bases
Pour déclarer une variable en Python la syntaxe est la suivante :
```
nom_de_ma_variable = <expression>
```
```python
ma_variable = 42
```
Il existe plusieurs types de donnée de base en Python. Les plus utilisés sont :
* str (chaine de charactères)
* int (entier)
* float (nombre à virgule)
* tuple (array immutable)
* list (array)
* dict (clé/valeur, similaire au HashMap de Java ou object de JS)
* set (ensemble non ordonné avec un test d'inclusion de complexité O(1))
* bool (booléen)
* None (valeur nulle)
### Exercice
Dans un fichier nommé exercise_1.p
* Créer une variable nommée `my_tuple` contenant les valeurs `42`, `'abc'` et `True`
* Créer une variable nommée `my_list` contenant `my_tuple`, `'lorem ipsum`' et une référence vers elle même
* Créer une variable nommée `my_dict` contenant les paires clé/valeur suvantes : `'hello'`/`'world'`, `42`/`None`, `True`/`False`
#### Contraintes
Ne pas créer plus de variable que strictement nécessaire