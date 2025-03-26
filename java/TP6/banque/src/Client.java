public class Client extends Personne{
    private String numero;
    private String nom;
    private String prenom;
    private String adresse;

    public Client(String numero, String nom, String prenom, String adresse){
        super(nom, prenom, adresse);
        this.numero = numero;
    }
    
}
