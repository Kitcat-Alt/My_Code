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

Les suite FF FF FF sont les pixels de couleur blanc et les 00 00 FF sont pour le rouge (B = 0, G = 0, R = 255 car on es en little endian)
4A est la taille du fichier en octet (sur 4 octets), 1A est l'adresse à laquelle commence l'image (le début des pixels)
le 0C donne la taille de la deuxième partie de l'entête. Enfin le 18 vient du fait que l'on utilise 3 octets pour coder la couleur d'un pixel (RGB), on utilise donc 8x3 = 24 bits pour coder un pixel et en hexadecimal 24 = 18.


## A.2
En convertissant l'image en bmp3, on obtient bien une nouvelle taille de 102 octets
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

Ici on a juste changé les pixels pour avoir d'autres couleurs par exemple 00 FF 00 pour avoir du vert. Pour les couleurs non primaire il a fallu convertir leur code rgb en décimal en hexadécimal et le mettre en little endian sur le code. Par exemple pour le bleu céruléen, on a le code 15, 157, 232 qui donne en hexadécimal : 0F, 9D, E8 qui donne en little endian E8 9D 0F.

## A.3
En enelevant 12 octets à la taille de l'image et en en rajoutant 40 , on obtient une nouvelle taille de 72-12+40 = 102 octets 

Voici le code de l'image convertie
![Image](/SAE/Image/CodeImage1.png)
Sur ce code nous pouvons voir que la taille de l'image est toujours à l'adresse 0x02 sur octets. Ici la valeur à cette adresse est de 66 soit 102 en décimal. On retrouve bien la taille calculée précedemment.  
On remarque aussi qu'un autre en tête a été ajouté à partir de 18 00 à l'adresse 0x1C.
1. Il y a toujours 24 bits par pixels (18 = 24 en décimal)

2. La taille des données pixels est de 48 octets.Cette valeur s'obtient grace à la valeur 30 à l'adresse 0x22 qui est la taille des données pixels de l'image. 30 = 48 en décimal soit 48 octets de pixels.

3. La compression de l'image est indiquée à l'adresse 0x1E, cette compression est codée sur 4 octets. Dans notre cas à l'adresse 0x1E il y a que des zéros, l'image n'est donc pas compréssée.

4. Non le codage des pixels n'a pas changé, on code toujours le pixels sur 3 octets en little endian.

## A.4
En convertissant l'image on obtient ce code :
![Image](/SAE/Image/CodeImage2.png)
1. Il y a 1 bit par pixel. ce nombre ce trouve à l'adresse 0x1C.

2. La taille des données pixels se trouve à l'adresse 0x22. A cette adresse on trouve le nombre 10 qui en décimal nous donne 16. La taille des données pixels est donc de 16 octets.

3. La compression utilisée est indiquée à l'adresse 0x1E. A cette adresse on ne trouve que des zéros donc il n'y a pas de compréssion utilisée pour cette image.

4.

5. la palette de couleur est composée de deux couleurs. On trouve cette information à l'adresse 0x2E ou l'on trouve 2 en hexadécimal soit 2 en décimal donc 2 couleurs utilisées pour la palette.

6. Oui le codage des pixels a changé. Dans ce code, chaque pixel est représenté par 1 seul bit alors que dans es images précédente on utilisait 24 bits pour représenter un pixel.

7. Avec ce code :

    ![Image](/SAE/Image/CodeImageBleue.png)
    on obtient cette image :

    ![Image](/SAE/Image/ScreenShotImageBleue.png)

    Pour obtenir cette image il faut modifier la valeur d'une des deux couleurs de notre palette, ici c'est le rouge qu'il fallait changer. Il fallait donc remplacer le 00 00 FF 00 (qui correspond au rouge avec un octet réservé à la fin) à l'adresse 0x36 et mettre FF 00 00 00 pour avoir du bleu.

8. Avec ce code : 

    ![Image](/SAE/Image/CodeImageBleueInversee.png)

    on obtient cette image :

    ![Image](/SAE/Image/ScreenShotImageBleueInversee.png)

    Dans ce code comme les pixels sont codés sur 1 seul bit et qu'il n'y a que deux couleurs dans la palette, on peut en déduire que le 0 correspond au bleu et le 1 au blanc. Si on regarde pour les A0 dans les données pixels, ils donnent en binaire 1010 0000 soit en big endian : 0000 1010 ce qui nous donne blanc, bleu, blanc, bleu. Pour les 50, on a en binaire 0101 0000 qui donne en big endian 0000 0101 : bleu, blanc, bleu, blanc. En faisaint cela 4fois on retrouve le patern du damier précédent. Pour l'inverser, il suffisait de seulement changer les 50 en A0 et les A0 en 50. 

9. Avec ce code :
    ![Image](/SAE/Image/CodeImage3.png)

    on obtient cette image : 

    ![Image](/SAE/Image/ScreenShotImage3.png)

    Pour ce code, il a fallu remettre le rouge dans la palette de couleur avec 00 00 FF 00 à l'adresse 0x36. Pour la ligne de pixel blancs, il a fallu mettre F0 en hexa. En effet une ligne de pixels blanc correspond à une suite de 1 en binaire : 1111 qui en little endian donne 1111 0000 et en hexa donne F0. Ensuite, le 0 correspondant au rouge en binaire, il a fallu laisser les octets à 0 sur deux lignes pour avoir les deux lignes de pixels rouges sur l'image. Enfin pour la dernière ligne, il fallait alterner entre deux couleur (1 sur 2) comme dans la question précédente. Il fallait donc coder cette suite en binaire : 1010 soit blanc, rouge, blanc, rouge. En little endian cela donne 0000 1010 qui donne A0 en hexa.

    L'en tête de l'image convertie :

    ![Image](/SAE/Image/EnTeteImgExempleConvertie.png)

11. On trouve le nombre de couleur dans la palette à l'adresse 0x2E. ici on trouve 10 en hexa soit 16 en décimal donc 16 couleurs dans la palette.

12. La couleur blanche pure en RGB est codée en hexa par FF FF FF. Il faut donc trouver la couleur dans la palette dont le code se rapproche le plus de celui du blanc pur. On trouve FE FE FD à l'adresse 0x66 qui est couleur à dominante blanc.

13. Le tableau de pixel commence à l'adresse 0x76. On trouve cette information à l'adresse 0x0A qui donne l'adresse de la zone de définition de l'image ici c'est 76. 

14. 
    L'image avec les pixels bleus rajoutés : 
    ![Image](/SAE/Image/PixelsBleusImageExemple.png)

    Le code de cette nouvelle image : 
    ![Image](/SAE/Image/CodeImageExemplePixelsBleus.png)

    Pour rajouter ces pixels bleus en bas à gauche, il a fallu rajouter des A pour chaque octets au début de la zone de définition de l'image. Mais pourquoi ? On sait que l'image a 16 couleurs grace au 10 à l'adresse 0x2E qui nous donne 16 en décimal. Ensuite, on sait que la palette de couleur commence à l'adresse 0x36 et que la zone de définition de l'image commence à l'adresse 0x76. On peut donc en déduire que la palette de couleur va de l'adresse 0x36 à l'adresse 0x76. Il faut maintenant trouver une couleur qui donne bleu parmi les 16 que contient la palette. Cependant, nous sommes en little endian il ne faut donc pas oublier d'inverser le rouge et le bleu pour passer de BGR à RGB. J'ai choisi la couleur CD 92 3D (3D 92 CD en big endian) qui donne le bleu des pixels qu'on voit sur la première image. Après avoir choisi la couleur, il faut la coder de sorte à ce que les pixels soit en bleus. Pour cela il faut d'abord regarder la position de la couleur dans la palette, ici elle se trouve à l'adresse 0x5E et en comptant à partir du début de la palette on trouve que c'est la 10ème couleur de la palette. Enfin, on sait qu'un pixel est codé sur 4bits et que par conséquent un octet permet de coder 2 pixels. En convertissant 10 en binaire on a 1010 (ce qui tient bien sur 4 bits) et en hexa cela nous donne A. En remplaçant les CC par des AA dans les premiers octets, on modifie pour chaque octet la couleur de 2 pixels en bleus
15. L'image avec seulement 4 couleurs : 
    ![Image](/SAE/Image/ImageExempleIndexBMP3_4.bmp)

    Visuellement, on remarque qu'il manque des couleurs comme le orange et que des pixels qui étaient avant des nuances de certaines couleurs comme le bleu on été remplacés par du blanc.

    Le code de l'image : 
    ![Image](/SAE/Image/CodeImageExemple4Couleurs.png)
    Au niveau de l'hexa on peut voir qu'une bonne partie de la palette de couleur a été remplacé par des 0 puisqu'il n'y a plus que 4 couleurs. Les pixels on changés puisque qu'il n'y a plus les mêmes couleurs qu'avant. Cependant on peut voir que selon l'hexa le nombre de couleurs n'a pas changé puisqu'à l'adresse 0x2E on retrouve toujours 10 en hexa soit 16 en décimal donc 16 couleurs alors qu'il n'y en a que 4.

## A.5 