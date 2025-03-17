public class Demineur extends Plateau {
    private boolean gameOver;
    private int score;

    public Demineur(int nbLignes, int nbColonnes, int pourcentage){
        super(nbLignes,nbColonnes,pourcentage);
        this.gameOver = false;
        this.score = 0;
    }

    public int getScore(){
        return this.score;
    }

    public void reveler(int x, int y){
        getCase(x, y).reveler();
    }

    public void marquer(int x, int y){
        getCase(x, y).marquer();
    }

    public boolean estGagnee(){
        for(int i=0; i<getNbLignes(); ++i){
            for(j=0; j<getNbColonnes(); ++j){}
        }
    }

    public boolean estPerdue(){
        if(!(this.gameOver)){
            return true;
        }
        return false;
    }

    @Override
    public void reset(){
        this.gameOver = false;
        reset();
    }

    public void affiche(){
        System.out.println("JEU DU DEMINEUR");
        // affichage de la bordure supérieure
        System.out.print("  ");
        for (int j=0; j<this.getNbColonnes(); j++){
            System.out.print("  "+j+" ");
        }
        System.out.print(" \n");
        
        // affichage des numéros de ligne + cases
        System.out.print("  ┌");
        for (int j=0; j<this.getNbColonnes()-1; j++){
                System.out.print("───┬");
        }
        System.out.println("───┐");
        
        // affichage des numéros de ligne + cases
        for (int i = 0; i<this.getNbLignes(); i++){
            System.out.print(i+" ");
            for (int j=0; j<this.getNbColonnes(); j++){
                System.out.print("│ "+this.getCase(i, j).toString() + " ");
            }
            System.out.print("│\n");
            
            if (i!=this.getNbLignes()-1){
                // ligne milieu
                System.out.print("  ├");
                for (int j=0; j<this.getNbColonnes()-1; j++){
                        System.out.print("───┼");
                }
                System.out.println("───┤");
            }
        }

        // affichage de la bordure inférieure
        System.out.print("  └");
        for (int j=0; j<this.getNbColonnes()-1; j++){
                System.out.print("───┴");
        }
        System.out.println("───┘");
        
        // affichage des infos 
        System.out.println("Nombres de bombes à trouver : " + this.getNbTotalBombes());
        System.out.println("Nombres de cases marquées : " + this.getNbCasesMarquees());
        System.out.println("Score : " + this.getScore());
    }

    public void nouvellePartie(){
        
    }

    //Scannner scanner = new Scanner(System.in);
}
