public class Chat{
    /** Nom du chat */
    private String nom;
    /** Cet attribut modélise à quel point le chat est bavard */
    private int bavard;
    /** permet de construire un Chat plus ou moins bavard */
    public Chat(String nomDuChat, int bavard){
        this.nom = nomDuChat;
        this.bavard = bavard;
    }
    /** permet de construire un Chat "normal" */
    public Chat(String nomDuChat){
        this(nomDuChat, 1);
    }    
    public String getNom(){
        return this.nom;
    }
    public void setNom(String nouveauNom){
        this.nom=nouveauNom;
    }
    public void devientMuet(){
        this.bavard = 0;
    }
    /**
     * Cette méthode fait miauler le chat en affichant un message
     * sur la sortie standard (dans le terminal par défaut)
     * Plus le chat est bavard, et plus il miaule
     */
    public void miaule(){
        System.out.print(this.nom);
        for(int i=0; i<this.bavard; i++){
            System.out.print(" Miaou!");
        }
        System.out.println(" ...");
    }
    /**
     * Cette méthode détermine si le chat est endormi
     * @param heure un double compris entre 0 et 24
     * @return true si le chat dort (presque tout le temps) 
     * et false sinon (c'est à dire entre 3 et 4 heures du matin)
     */
    public boolean estEndormi(double heure){
        return (heure<=3 || heure>4);
    }
}
