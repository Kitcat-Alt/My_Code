# Rapport SAE Image
## A.0
La première partie du fichier est l'en tête du fichier :
- les 2 premier octets 42 4D correspondent au format du fichier 42 qui fait B en Ascii et 4D qui fait M.
![Image](/SAE/Image/Screenshots/entete.png)
- Ensuite il y a 4 octets : 99 73 0C 00 qui donnent la taille du fichier avec cela oon peut avoir la taille du fichier en octets. Cependant il faut inverser tout les octets pour convertir car c'est du little endian : 9 + 9x16^1 + 3x16^2 + 7x16^3 + 12x16^4 = 816025
L'erreur avec display vient du fait que la taille du fichier en octet sur okteta ne correspond pas à la taille réelle en octet 
![Image](/SAE/Image/Screenshots/TailleImgOctet.jpg)
Ici on voit que l'image fait 816026 octets or sur le fichier il est indiqué 816025 octets il faut donc rajouter 1 bit dans le fichier pour qu'il n'y ai plus d'erreur avec display. Il faut donc changer 99 en 9A pour avoir : 10 + 9x16^1 + 3x16^2 + 7x16^3 + 12x16^4 = 816026
![Image](/SAE/Image/Screenshots/entetebonne.png)

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

![Image](/SAE/Image/Screenshots/ImageTestScreenShot.png)

Ici on a juste changé les pixels pour avoir d'autres couleurs par exemple 00 FF 00 pour avoir du vert. Pour les couleurs non primaire il a fallu convertir leur code rgb en décimal en hexadécimal et le mettre en little endian sur le code. Par exemple pour le bleu céruléen, on a le code 15, 157, 232 qui donne en hexadécimal : 0F, 9D, E8 qui donne en little endian E8 9D 0F.

## A.3
En enelevant 12 octets à la taille de l'image et en en rajoutant 40 , on obtient une nouvelle taille de 72-12+40 = 102 octets 

Voici le code de l'image convertie
![Image](/SAE/Image/Screenshots/CodeImage1.png)
Sur ce code nous pouvons voir que la taille de l'image est toujours à l'adresse 0x02 sur octets. Ici la valeur à cette adresse est de 66 soit 102 en décimal. On retrouve bien la taille calculée précedemment.  
On remarque aussi qu'un autre en tête a été ajouté à partir de 18 00 à l'adresse 0x1C.
1. Il y a toujours 24 bits par pixels (18 = 24 en décimal)

2. La taille des données pixels est de 48 octets.Cette valeur s'obtient grace à la valeur 30 à l'adresse 0x22 qui est la taille des données pixels de l'image. 30 = 48 en décimal soit 48 octets de pixels.

3. La compression de l'image est indiquée à l'adresse 0x1E, cette compression est codée sur 4 octets. Dans notre cas à l'adresse 0x1E il y a que des zéros, l'image n'est donc pas compréssée.

4. Non le codage des pixels n'a pas changé, on code toujours le pixels sur 3 octets en little endian.

## A.4
En convertissant l'image on obtient ce code :
![Image](/SAE/Image/Screenshots/CodeImage2.png)
1. Il y a 1 bit par pixel. ce nombre ce trouve à l'adresse 0x1C.

2. La taille des données pixels se trouve à l'adresse 0x22. A cette adresse on trouve le nombre 10 qui en décimal nous donne 16. La taille des données pixels est donc de 16 octets.

3. La compression utilisée est indiquée à l'adresse 0x1E. A cette adresse on ne trouve que des zéros donc il n'y a pas de compréssion utilisée pour cette image.

4.

5. la palette de couleur est composée de deux couleurs. On trouve cette information à l'adresse 0x2E ou l'on trouve 2 en hexadécimal soit 2 en décimal donc 2 couleurs utilisées pour la palette.

6. Oui le codage des pixels a changé. Dans ce code, chaque pixel est représenté par 1 seul bit alors que dans es images précédente on utilisait 24 bits pour représenter un pixel.

7. Avec ce code :

    ![Image](/SAE/Image/Screenshots/CodeImageBleue.png)
    on obtient cette image :

    ![Image](/SAE/Image/Screenshots/ScreenShotImageBleue.png)

    Pour obtenir cette image il faut modifier la valeur d'une des deux couleurs de notre palette, ici c'est le rouge qu'il fallait changer. Il fallait donc remplacer le 00 00 FF 00 (qui correspond au rouge avec un octet réservé à la fin) à l'adresse 0x36 et mettre FF 00 00 00 pour avoir du bleu.

8. Avec ce code : 

    ![Image](/SAE/Image/Screenshots/CodeImageBleueInversee.png)

    on obtient cette image :

    ![Image](/SAE/Image/Screenshots/ScreenShotImageBleueInversee.png)

    Dans ce code comme les pixels sont codés sur 1 seul bit et qu'il n'y a que deux couleurs dans la palette, on peut en déduire que le 0 correspond au bleu et le 1 au blanc. Si on regarde pour les A0 dans les données pixels, ils donnent en binaire 1010 0000 soit en big endian : 0000 1010 ce qui nous donne blanc, bleu, blanc, bleu. Pour les 50, on a en binaire 0101 0000 qui donne en big endian 0000 0101 : bleu, blanc, bleu, blanc. En faisaint cela 4fois on retrouve le patern du damier précédent. Pour l'inverser, il suffisait de seulement changer les 50 en A0 et les A0 en 50. 

9. Avec ce code :
    ![Image](/SAE/Image/Screenshots/CodeImage3.png)

    on obtient cette image : 

    ![Image](/SAE/Image/Screenshots/ScreenShotImage3.png)

    Pour ce code, il a fallu remettre le rouge dans la palette de couleur avec 00 00 FF 00 à l'adresse 0x36. Pour la ligne de pixel blancs, il a fallu mettre F0 en hexa. En effet une ligne de pixels blanc correspond à une suite de 1 en binaire : 1111 qui en little endian donne 1111 0000 et en hexa donne F0. Ensuite, le 0 correspondant au rouge en binaire, il a fallu laisser les octets à 0 sur deux lignes pour avoir les deux lignes de pixels rouges sur l'image. Enfin pour la dernière ligne, il fallait alterner entre deux couleur (1 sur 2) comme dans la question précédente. Il fallait donc coder cette suite en binaire : 1010 soit blanc, rouge, blanc, rouge. En little endian cela donne 0000 1010 qui donne A0 en hexa.

    L'en tête de l'image convertie :

    ![Image](/SAE/Image/Screenshots/EnTeteImgExempleConvertie.png)

11. On trouve le nombre de couleur dans la palette à l'adresse 0x2E. ici on trouve 10 en hexa soit 16 en décimal donc 16 couleurs dans la palette.

12. La couleur blanche pure en RGB est codée en hexa par FF FF FF. Il faut donc trouver la couleur dans la palette dont le code se rapproche le plus de celui du blanc pur. On trouve FE FE FD à l'adresse 0x66 qui est couleur à dominante blanc.

13. Le tableau de pixel commence à l'adresse 0x76. On trouve cette information à l'adresse 0x0A qui donne l'adresse de la zone de définition de l'image ici c'est 76. 

14. 
    L'image avec les pixels bleus rajoutés : 
    ![Image](/SAE/Image/Screenshots/PixelsBleusImageExemple.png)

    Le code de cette nouvelle image : 
    ![Image](/SAE/Image/Screenshots/CodeImageExemplePixelsBleus.png)

    Pour rajouter ces pixels bleus en bas à gauche, il a fallu rajouter des A pour chaque octets au début de la zone de définition de l'image. Mais pourquoi ? On sait que l'image a 16 couleurs grace au 10 à l'adresse 0x2E qui nous donne 16 en décimal. Ensuite, on sait que la palette de couleur commence à l'adresse 0x36 et que la zone de définition de l'image commence à l'adresse 0x76. On peut donc en déduire que la palette de couleur va de l'adresse 0x36 à l'adresse 0x76. Il faut maintenant trouver une couleur qui donne bleu parmi les 16 que contient la palette. Cependant, nous sommes en little endian il ne faut donc pas oublier d'inverser le rouge et le bleu pour passer de BGR à RGB. J'ai choisi la couleur CD 92 3D (3D 92 CD en big endian) qui donne le bleu des pixels qu'on voit sur la première image. Après avoir choisi la couleur, il faut la coder de sorte à ce que les pixels soit en bleus. Pour cela il faut d'abord regarder la position de la couleur dans la palette, ici elle se trouve à l'adresse 0x5E et en comptant à partir du début de la palette on trouve que c'est la 10ème couleur de la palette. Enfin, on sait qu'un pixel est codé sur 4bits et que par conséquent un octet permet de coder 2 pixels. En convertissant 10 en binaire on a 1010 (ce qui tient bien sur 4 bits) et en hexa cela nous donne A. En remplaçant les CC par des AA dans les premiers octets, on modifie pour chaque octet la couleur de 2 pixels en bleus
15. L'image avec seulement 4 couleurs : 
    ![Image](/SAE/Image/images/ImageExempleIndexBMP3_4.bmp)

    Visuellement, on remarque qu'il manque des couleurs comme le orange et que des pixels qui étaient avant des nuances de certaines couleurs comme le bleu on été remplacés par du blanc.

    Le code de l'image : 
    ![Image](/SAE/Image/Screenshots/CodeImageExemple4Couleurs.png)
    Au niveau de l'hexa on peut voir qu'une bonne partie de la palette de couleur a été remplacé par des 0 puisqu'il n'y a plus que 4 couleurs. Les pixels on changés puisque qu'il n'y a plus les mêmes couleurs qu'avant. Cependant on peut voir que selon l'hexa le nombre de couleurs n'a pas changé puisqu'à l'adresse 0x2E on retrouve toujours 10 en hexa soit 16 en décimal donc 16 couleurs alors qu'il n'y en a que 4.

## A.5 
2. En changeant la hauteur de 04 00 00 00 à FC FF FF FF, on passe la hauteur de 4 à -4. Pour avoir ce nombre négatif, il fallait passer par le C2 : 4 en binaire donne 0000 0000 0000 0100 et en C2 cela donne 1111 1111 1111 1100 qui donne en hexa : FF FF FF FC.

    Dans le code cela donne : 

    ![Image](/SAE/Image/Screenshots/CodeImage3Inverse.png)

    On peut voir qu'on a remplacé la hauteur de l'image par FC FF FF FF

    cela donne l'image :

    ![Image](/SAE/Image/Screenshots/ScreenShotImage3Inverse.png)

    On peut voir qu'en passant la hauteur de l'image en négatif, l'image c'est retournée.

3. Pour cette image, il suffit de faire le même calcul que précedement : on converti la hauteur de l'image en binaire : 00 00 01 A9 -> 0000 0001 1010 1001. Puis on inverse les bits à gauche du premier 1 rencontré dans notre chiffre : 1111 1110 0101 0111. Ce qui donne en hexa FF FF FE 57 et en little endian 57 FE FF FF 

    Dans le code cela donne ceci :

    ![Image](/SAE/Image/Screenshots/CodeImageExempleInverse.png)

    On retrouve bien le 57 FE FF FF à l'adresse 0x16

    Avec ce code on obtient cette image : 

    ![Image](/SAE/Image/Screenshots/ScreenShotImageExempleInverse.png)

## A.6
1. Le poid du nouveau fichier est de 1120 octets alors qu'avant la compression il n'en faisait que 102. On a donc multiplié par 10 la taille du fichier. Cela peut s'expliquer en regardant le nouveau code de cette image : 

    ![Image](/SAE/Image/Screenshots/CodeImage4.png)

    On peut remarquer que l'en tête du fichier a beaucoup changé. En effet on peut voir que la palette de couleur est composé de 256 couleurs(dont toutes sont du noirs sauf les deux première qui sont rouge et blanc) car on a 8 bits par pixels soit 2⁸ = 256. De plus à l'adresse du nombre de couleur utilisées on trouve qu'il y en a 0 soit le maximum.
    Enfin on peut voir que le nombre de bits par pixels a diminué, on est passé de 24 bits par pixels à 8 bits par pixels.

2. L'offset du début des pixels se trouve à l'adresse 0x0A. Cet offset nous donne une adresse :0x436

    Le codage des pixels : 
    ![Image](/SAE/Image/Screenshots/CodagePixelsImage4.png)

3. On sait que le codage des pixels commence à l'adresse 0x436. Il faut maintenant comprendre comment fonctionne la compression RLE : la compression RLE code nos pixels grâce à deux octets. Le premier octet nous donne le nombre de pixels à coder et le deuxième nous donne la couleur de ce pixel (sa position dans la palette de couleur). Par exemple le premier couple d'octet que l'on rencontre est : 01 00. Le premier octet dit que l'on va coder 1 fois un pixel et le deuxième octet dit que c'est la première couleur de la palette que l'on va coder (ici le rouge) : en effet, si on regarde la palette de couleur le rouge est bien la première couleur de la palette et on la code bien une seule fois (on commence en bas à gauche de l'image). ce processus ce répète pour chaque pixels (01 01 signifie 1 pixel de couleur blanche)

    ![Image](/SAE/Image/Screenshots/Image0ScreenShot.png)

## A.7
1. L'entête de l'image convertie : 
    
    ![Image](/SAE/Image/Screenshots/EnteteImage5.png)

    Le codage des pixels de cette image :

    ![Image](/SAE/Image/Screenshots/CodagePixelsImage5.png)

    Le fichier fait 1102 octets. C'est 18 octets de moins que le fichier précédent car si on regarde le codage des pixels, on remarque qu'il y a moins de données pixels qu'avant.

    Voici l'image obtenue : 

    ![Image](/SAE/Image/Screenshots/ScreenShotImage3.png)
2. La compression étant la même, la manière de coder les pixels n'a pas changé. Prenons la première ligne de pixels blanc en bas à gauche de l'image. Ces pixels sont codés comme ceci : 04 01. Le premier octet (04) signifie que l'on va coder 4 pixels et le deuxième octet (01) signifie qu'on va coder la deuxième couleur de la palette (On commence à 0 donc c'est bien la deuxième), ici cette couleur correspond au blanc. C'est la même chose pour les 2 lignes rouges qui suivent : 04 00, 4 pixels codés en rouge (00 correspondant à la première couleur de la palette soit le rouge ici). Pour la dernière ligne, c'est la même façon qu'à la question précédente 01 01 un pixel de couleur blanche, 01 00 un pixel de couleur rouge. A noter qu'on sépare chaque ligne de pixels par deux octets à zéro.

## A.8
Le codage des pixels de l'image obtenue :

![Image](/SAE/Image/Screenshots/CodagePixelsImage6.png)

Par rapport à l'image d'avant, on a modifié la première ligne de pixels. On a remplacé 04 00 00 00 
par 02 01 01 00 01 01 00 00. 02 01 pour avoir les deux premier pixels blancs, 01 00 pour ensuite avoir 1 pixel rouge et enfin 01 01 pour avoir 1 pixel blanc.

Cela donne l'image : 

![Image](/SAE/Image/Screenshots/ScreenShotImage6.png)

L'entête de l'image :

![Image](/SAE/Image/Screenshots/EnTeteImage6.png)

La seule chose qu'il a fallu changer par rapport à l'image5 est la taille de l'image car on a rajouté des données pixels, donc la taille n'était plus la même. Ici la nouvelle image fait 1106 octets soit 452 en hexa et 52 04 00 00 en little endian.

## A.9
L'image obtenue : 

![Image](/SAE/Image/Screenshots/ScreenShotImage7.png)

L'en tête de l'image : 

![Image](/SAE/Image/Screenshots/EnTetetImage7.png)

J'ai remplacé deux couleurs noires de la palette par les couleurs vert et bleu dans la palette, ici on trouve le bleu à l'adresse 0x3E (FF 00 00 00) et le vert à l'adresse 0x41 (00 FF 00 00).

Le codage des pixels : 

![Image](/SAE/Image/Screenshots/CodagePixelsImage7.png)

Pour la première ligne (en bas), il fallait changer le pixel qui était rouge en bleu. Pour cela j'ai changé le deuxième couple d'ocets à l'adresse 0x438.
J'ai donc remplacé le couple 01 00 par le couple 01 02. 01 pour 1 fois un pixel et 02 pour la deuxième couleur de la palette, ici c'est le bleu. Enfin j'ai changé le couple 04 00 à l'adresse 0x442 en 04 03. 04 pour quatre pixels et 03 pour la 3ème couleur de la palette ici le vert.

## A.10
1. L'image obtenue :  

    ![Image](/SAE/Image/Screenshots/ScreenShotImage8.png)

    L'entête de l'image:

    ![Image](/SAE/Image/Screenshots/EnTeteImage8.png)

    Dans cette entête, seule la taille a été modifée par rapport à l'image précedente car des données pixels on été ajoutées cela a donc fait passé la taile de 1106 octets à 1114 octets soit 45A en hexa et 5A 04 00 00 en litlle endian sur 32 bits.

    Le codage des pixels : 

    ![Image](/SAE/Image/Screenshots/CodagePixelsImage8.png)

    Par rapport à l'image précedente, ce sont les lignes 2 et 3 qui on été modifiées. Pour la deuxième ligne (en partant du bas), on a 01 00 01 03 02 00. Le premier couple d'octet 01 00 veut dire qu'on code un seul pixel avec la première couleur de la palette (le rouge ici). Le deuxième couple d'octet 01 03 veut dire qu'on code un pixel avec la 3ème couleur de la palette (ici le vert). Enfin le dernier couple d'octet 02 00 veut dire que l'on code deux pixels avec la première couleur de la palette (le rouge). Pour la 3ème ligne on a 02 03 01 00 01 03. Le premier couple d'octet 02 03 veut dire que l'on code deux pixels avec la 3ème couleur de la palette (ici le vert). Le deuxième couple d'octet 01 00 veut dire que l'on code un pixel avec la première couleur de la palette (le rouge) et le dernier couple d'octet 01 03 veut dire que l'on code un pixel avec la 3ème couleur de la palette.

2. 

## B.1
Pour créer la transposée d'une image il faut inverser les lignes et les colonnes.
Voici le programme qui permet de faire cela :

![Image](/SAE/Image/Screenshots/ScreenShotB.1.png)

Tout d'abord, on ouvre l'image à transposer et on en fait une copie (lignes 3 et 4). Ensuite, on définit une fonction qui va parcourir l'image ligne par ligne en partant en haut à droite. c'est ce que font les deux boucles for. La ligne 9 va s'occuper de récupérer la valeur de chaque pixel que l'on rencontre. C'est-à-dire qu'elle va stocker un tuple qui va stocker la couleur comme ceci : (R,G,B). Quand on a récupéré un pixel, on le met sur l'image copiée et on inverse ligne et colonne dans "putpixel". Quand on a fini de parcourir l'image, on enregistre l'image transposée (ligne 11).

## B.2
![Image](/SAE/Image/Screenshots/ScreenShotB.2.png)

Pour inverser une image comme dans un miroir il faut que le dernier pixel d'une ligne, devienne le premier pixel de cette ligne et inversement (le premier doit devenir le dernier). Il faut faire cela pour chaque ligne de l'image.
On va donc commencer par définir une variable "colonneInverse" qui stockera l'indice de la colonne opposée du pixel qu'on est entrain de lire. Comme précédement, on commence par ouvrir l'image à inverser et on en fait une copie(lignes 5 et 6). Ensuite, on parcour l'image par lignes et par colones avec les deux boucles for. 
La ligne 11 permet de parcourir l'image de droite à gauche. En effet, on prend la longueur de l'image à laquelle on enlève la colone ou on se trouve en lui ajoutant 1 car on commence à 0. Cela permet d'aller récuperer le pixel opposé à celui que l'on regarde.
Quand on a cet indice, on va aller chercher la valeur du pixel à cet indice et on le met sur l'image copiée (ligne 12 et 13). Enfin on enregistre l'image copiée.

## B.3
![Image](/SAE/Image/Screenshots/ScreenShotB.3.png)

les lignes 3 et 4 permettent d'ouvrir l'image que l'on veut passer en niveau de gris et d'en faire une copie. La variable pixel_gray à la ligne 5 va permettre de stocker la valeur d'un pixel passé en niveau de gris. Ensuite dans le fonction, on parcour l'image de gauce à droite en partant d'en haut à gauche. Pour chaque indice (colone, ligne) on récupère la valeur du pixel grâce à la ligne 10 puis on passe ce pixel en niveau de gris grace à la formule donnée : Gris=(R+V+B)/3. On fait cela pour le rouge, le vert et le bleu (ligne 11). Après avoir passé le pixel en gris on le met sur la copie de l'image originale (ligne 12). Enfin quand on a fini de parcourir l'image originale, on enregistre l'image copiée.

## B.4
![Image](/SAE/Image/Screenshots/ScreenShotB.4.png)
Pour passer l'image en noir en blanc, on doit utiliser cette formule : (R * R+V * V+B * B) > 255 * 255 * 3/2. A la ligne 5 on défini la deuxième partie de la formule qui nous servira de comparaison pour savoir si l'on met un pixel noir ou blanc. Quand on récupère la valeur d'un pixel (ligne 10), on calcule la partie gauche de la formule. Ensuite on compare les deux parties entre elles, si la partie gauche est supérieure à la partie droite, on met un pixel blanc sinon, on met un pixel noir.

## B.5