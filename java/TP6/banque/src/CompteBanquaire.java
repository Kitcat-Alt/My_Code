public class CompteBanquaire {
       private String numero;
       private float solde;
       private String dateOuverture;
       private String nomClient;
       private String prenomClient;
       private String numeroAgence;
       private String numeroBanque;
       
       public CompteBanquaire(String numero, float solde, String dateOuverture, String nomClient, String prenomClient, String numeroAgence, String numeroBanque){
            this.numero = numero;
            this.solde = solde;
            this.dateOuverture = dateOuverture;
            this.nomClient = nomClient;
            this.prenomClient = prenomClient;
            this.numeroAgence = numeroAgence;
            this.numeroBanque = numeroBanque;
       }
}
