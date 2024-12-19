import pygame
import time
import sys
import matrice

class MatriceGraphique(object):
    """Classe simple d'affichage d'une matrice."""

    def __init__(self, la_matrice, titre='Le Labyrinthe', size=(640, 640), couleur=(255, 0, 0)):
        """Method docstring."""
        self.couleur = couleur
        self.la_matrice = la_matrice
        self.nb_col = matrice.get_nb_colonnes(la_matrice)
        self.nb_lig = matrice.get_nb_lignes(la_matrice)
        pygame.init()
        fenetre = pygame.display.set_mode(size,pygame.RESIZABLE|pygame.DOUBLEBUF)
        pygame.display.set_caption(titre)
        self.surface = pygame.display.get_surface()
        self.mise_a_jour_parametres()
        self.dico_images = {}
        self.set_dico("dico.txt","./img/")

    def set_dico(self, nom_fichier, dossier_image="./"):
        self.dico_images = {}
        fichier = open(nom_fichier, "r")
        for ligne in fichier:
            (cle, nom_image) = ligne.split()
            image = pygame.image.load(dossier_image + nom_image)
            self.dico_images[cle] = image
        fichier.close()

    def mise_a_jour_parametres(self):
        self.surface = pygame.display.get_surface()
        self.hauteur = self.surface.get_height()*8//10 - (self.nb_lig + 1)
        self.largeur = self.surface.get_width()*8//10 - (self.nb_col + 1)
        self.deltah = self.hauteur//(self.nb_lig + 1)
        self.deltal = self.largeur//(self.nb_col + 1)
        self.finh = self.deltah*(self.nb_lig + 1)
        self.finl = self.deltal*(self.nb_col + 1)
        self.taille_font = min(self.deltah, self.deltal)*2//3

    def affiche_message(self, le_message):
        font = pygame.font.Font(None, self.taille_font)
        texte = font.render(le_message, 1, self.couleur)
        textpos = texte.get_rect()
        textpos.y = self.finh + self.deltah
        textpos.x = 15
        self.surface.blit(texte, textpos)
        pygame.display.flip()

    def dessine_grille(self):
        self.surface.fill((0,0,0))
        font = pygame.font.Font(None, self.taille_font)
        for i in range(0, self.nb_lig):
            text = font.render(str(i), 1, self.couleur)
            textpos = text.get_rect()
            textpos.centerx = self.deltal//2
            textpos.centery = (i + 1)*self.deltah + self.deltah//2
            self.surface.blit(text, textpos)
        for i in range(0, self.nb_col):
            text = font.render(str(i), 1, self.couleur)
            textpos = text.get_rect()
            textpos.centerx = (i + 1)*self.deltal + self.deltal//2
            textpos.centery = self.deltah//2
            self.surface.blit(text, textpos)
        for i in range(1, self.nb_lig + 2):
            pygame.draw.line(self.surface, self.couleur, (self.deltal, i*self.deltah), (self.finl, i*self.deltah))
        for i in range(1, self.nb_col + 2):
            pygame.draw.line(self.surface, self.couleur, (i*self.deltal,self.deltah), (i*self.deltal, self.finh))
            
    def remplit_grille(self):
        for i in range(self.nb_lig):
            for j in range(self.nb_col):
                try:
                    s=pygame.transform.smoothscale(self.dico_images[str(matrice.get_val(self.la_matrice, i, j))],(self.deltal-8, self.deltah-8))
                    self.surface.blit(s, ((j+1)*self.deltal + 4, (i+1)*self.deltah + 4))
                except:
                    s=pygame.Surface((self.deltal - 8, self.deltah - 8))
                    s.fill((0, 0, 0))
                    self.surface.blit(s, ((j+1)*self.deltal + 4, (i+1)*self.deltah + 4))
        pygame.display.flip()

    def parcoursChemin(self,chemin,val):
        if chemin != []:
            (x1, y1) = chemin.pop(0)
            matrice.set_val(self.la_matrice, x1, y1, val)
            self.affiche_grille()
            for (x2, y2) in chemin:
                time.sleep(1)
                matrice.set_val(self.la_matrice, x1, y1, 0)
                matrice.set_val(self.la_matrice, x2, y2, val)
                self.affiche_grille()
                x1 = x2
                y1 = y2

    def affiche_matrice(self):
        self.dessine_grille()
        self.remplit_grille()

    def detruire(self):
        pygame.quit()




