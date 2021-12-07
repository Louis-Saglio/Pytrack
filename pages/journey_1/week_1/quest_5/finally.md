Créez une fonction main prennant en paramètre nommé test une autre fonction sans paramètre ainsi que on_error qui est aussi une fonction sans paramètre  
main doit ensuite appeller `test`, si une exception se produit dans test il faut appeller on_error  
Dans tous les cas, même si une autre exception est levée par on_error, il faut retourner 'done'  
Attention : vous n'avez droit qu'à un seul mot clef `try`  