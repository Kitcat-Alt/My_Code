public class Plateau{
    private int nbLignes;
    private int nbColonnes;
    private int pourcentageDeBombe;
    private int nbBombes;

    public Plateau(int nbLignes, int nbColonnes, int pourcentage){
        this.nbLignes = nbLignes;
        this.nbColonnes = nbColonnes;
        this.pourcentageDeBombe = pourcentage;
        this .nbBombes = 0;
    }

    private void creerLesCasesVides(){

    }

    private void rendLesCasesIntelligentes(){

    }

    protected void poseDesBombesAleatoirement(){

    }

    public int getNbLignes() {
        return this.nbLignes;
    }

    public int getNbColonnes(){
        return this.nbColonnes;
    }

    public int getNbTotalBombes(){
        return this.nbBombes;
    }

    public CaseIntelligente getCase(int numLigne, int numColonne){
        return null;

    }

    public int getNbCasesMarquees(){
        return 0;
    }

    public void poseBombe(int x, int y){
        
    }

    public void reset(){

    }
}