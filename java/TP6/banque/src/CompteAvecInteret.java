public class CompteAvecInteret extends CompteBanquaire{
    private float taux;

    public CompteAvecInteret(String numero, float solde, String dateOuverture, String nomClient, String prenomClient, String numeroAgence, String numeroBanque, float taux){
        super(numero, solde, dateOuverture, nomClient, prenomClient, numeroAgence, numeroBanque);
        this.taux = taux;
    }
}