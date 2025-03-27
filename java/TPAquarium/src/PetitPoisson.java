public class PetitPoisson {
    private double posX;
    private double posY;
    private double vitesseX;

    public PetitPoisson(double posX, double posY, double vitesseX){
        this.posX = posX;
        this.posY = posY;
        this.vitesseX = vitesseX;
    }

    public void nage(){
        this.posX += vitesseX;

    }

    public Dessin getDessin(){
        Dessin petitpoisson = new Dessin();
        String couleur = "0x0000F0";
        petitpoisson.ajouteChaine((int)this.posX, (int)this.posY, "<><", couleur);
        return petitpoisson;
    }
}
