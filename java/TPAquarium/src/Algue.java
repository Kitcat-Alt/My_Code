import javax.crypto.spec.DESKeySpec;

public class Algue {
    private double posX;

    public Algue(double posX){
        this.posX = posX;
    }

    public void ondule(){

    }

    public Dessin getDessin(){
        Dessin dessin = new Dessin();
        return dessin;
    }
}
