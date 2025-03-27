public class Bulle{
    
    private double posX;
    private double posY;
    private double vitesseX;

    public Bulle(double posX, double posY, double vitesse){
        this.posX = posX;
        this.posY = posY;
        this.vitesseX = vitesse;
    }

    public void remonte(){

    }

    public Dessin getDessin(){
        Dessin dessin = new Dessin();
        return dessin;
    }
}
