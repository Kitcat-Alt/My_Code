# Rapport SAE Image
## A.0
La première partie du fichier est l'en tête du fichier :
- les 2 premier octets 42 4D correspondent au format du fichier 42 qui fait B en Ascii et 4D qui fait M.
![Image](/SAE/Image/entete.png)
- Ensuite il y a 4 octets : 99 73 0C 00 qui donnent la taille du fichier avec cela oon peut avoir la taille du fichier en octets. Cependant il faut inverser tout les octets pour convertir car c'est du little endian : 9 + 9x16^1 + 3x16^2 + 7x16^3 + 12x16^4 = 816025
L'erreur avec display vient du fait que la taille du fichier en octet sur okteta ne correspond pas à la taille réelle en octet 
![Image](/SAE/Image/TailleImgOctet.jpg)
Ici on voit que l'image fait 816026 octets or sur le fichier il est indiqué 816025 octets il faut donc rajouter 1 bit dans le fichier pour qu'il n'y ai plus d'erreur avec display. Il faut donc changer 99 en 9A pour avoir : 10 + 9x16^1 + 3x16^2 + 7x16^3 + 12x16^4 = 816026
![Image](/SAE/Image/entetebonne.png)