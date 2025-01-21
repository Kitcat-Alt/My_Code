public class Vaisseau{
    private String nom;
    private int puissance;
    private int passagers;

    public Vaisseau(String nom, int puissance, int passagers){
        this.nom = nom;
        this.puissance = puissance;
        this.passagers = passagers;
    }

    public Vaisseau(String nom, int puissance){
        this.passagers = 0;
        this.puissance = puissance;
        this.nom = nom;
    }

    public String getNom(){
        return this.nom;
    }


    public int getNombrePassagers(){
        return this.passagers;
    }

    public int getPuissance(){
        return this.puissance;
    }

    public boolean transportePassagers(){
        return this.passagers > 0;

    }

}