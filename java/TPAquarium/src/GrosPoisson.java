public class GrosPoisson {
    private double posX;
    private double posY;
    private double vitesseX;

    public GrosPoisson(double posX, double posY, double vitesseX){
        this.posX = posX;
        this.posY = posY;
        this.vitesseX = vitesseX;
    }

    public void nage(){

    }

    public Dessin getDessin(){
        Dessin dessin = new Dessin();
        return dessin;
    }
}