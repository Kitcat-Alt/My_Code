public class Magasin{
    private String nom;
    private boolean ouvertLundi;
    private boolean ouvertDimanche;

    /**
     * 
     * @param nom
     * @param lundi
     * @param dimanche
     */
    public Magasin(String nom, boolean lundi, boolean dimanche){
        this.nom = nom;
        this.ouvertLundi = lundi;
        this.ouvertDimanche = dimanche;
    }

    public String getNom(){
        return this.nom;
    }

    public boolean getOuvertLundi(){
        return this.ouvertLundi;
    }

    public boolean getOuvertDimanche(){
        return this.ouvertDimanche;
    }

    @Override
    public String toString(){
        String  res = "Magasin " + this.nom;

        if (this.ouvertLundi){
            res += ", ouvert le lundi";
        }
        else{
            res += ", fermé le lundi";
        }

        if(this.ouvertDimanche){
            res += ", ouvert le dimanche";
        }
        else{
            res += ", fermé le dimanche";
        }
        res += "\n";
        return res;
    }


}
