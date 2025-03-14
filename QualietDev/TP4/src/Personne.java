public class Personne{
    private String nom;
    private String prenom;
    public Personne( String n, String p) {this.nom = n; this.prenom = p;}
    @Override
    public String toString() {return this.prenom + " " + this.nom + " ";  }
    public String getNom() {return this.nom;}
    public String getPrenom() {return this.prenom;}
}
