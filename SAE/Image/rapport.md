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

## A.1
Avec ce code :
```
42 4D 4A 00 00 00 00 00 00 00 1A 00 00 00 0C 00
00 00 04 00 04 00 01 00 18 00 00 00 FF FF FF FF
00 00 FF FF FF FF FF FF FF 00 00 FF FF FF FF 00
00 FF 00 00 FF FF FF FF 00 00 FF FF FF FF FF FF
FF 00 00 FF FF FF FF 00 00 FF
```
on obtient cette image

![Image](/SAE/Image/Image0ScreenShot.png)

Les suite FF FF FF sont les pixels de couleur blanc et les 00 00 FF sont pour le rouge (B = 0, G = 0, R = 255 car on est en little endian)
4A est la taille du fichier en octet (sur 4 octets), 1A est l'adresse à laquelle commence l'image (le début des pixels)
le 0C donne la taille de la deuxième partie de l'entête. Enfin le 18 vient du fait que l'on utilise 3 octets pour coder la couleur d'un pixel (RGB), on utilise donc 8x3 = 24 bits pour coder un pixel et en hexadecimal 24 = 18 bits.


## A.2
Avec ce code :
```
42 4D 4A 00 00 00 00 00 00 00 1A 00 00 00 0C 00
00 00 04 00 04 00 01 00 18 00 FF FF 00 FF 00 FF
E8 9D 0F FF FF FF 00 00 FF 00 00 FF 00 00 FF FF
00 00 00 00 FF 00 00 FF 00 00 FF 00 00 FF 00 00
FF 00 FF 00 00 00 FF 00 00 FF 
```
on obtient cette image

![Image](/SAE/Image/ImageTestScreenShot.png)

Ici on a juste changé les pixels pour avoir d'autres couleurs par exemple 00 FF 00 pour avoir du vert. Pour les coleurs non primaire il a fallu convertir leur code rgb en décimal en hexadécimal et le mettre en little endian sur le code. Par exemple pour le bleu céruléen, on a le code 15, 157, 232 qui donne en hexadécimal : 0F, 9D, E8 qui donne en little endian E8 9D 0F.

## A.3
En enelevant 12 octets à la taille de l'image et en en rajoutant 40 , on obtient une nouvelle taille de 72-12+40 = 102 octets

En convertissant l'image en bmp3, on obtient bien une nouvelle taille de 102 octets 

Voici le code de l'image convertie
![Image](/SAE/Image/CodeImage1.png)
On remarque qu'un autre en tête a été ajouté à partir de 18 00.
1. Il y a toujours2' bits par pixels 