public class AppWeekEnd {

    private WeekEnd we;
    private boolean quitter;

    public AppWeekEnd(WeekEnd we) {
        this.we = we;
        this.quitter = false;
    }

    public void run() {
        bienvenue();
        boolean continuer = true;
        while (!quitter) {
            menu();
        }
        au_revoir();
    }

    public void menu() {
        boolean commande_faite = false;
        while (!commande_faite) {
            System.out.println("Que voulez vous faire?");
            System.out.println("P: afficher les personnes du weekend");
            System.out.println("D: afficher les dépenses du weekend");
            System.out.println("T: afficher le total des dépenses du weekend");
            System.out.println("M: afficher la dépense moyenne par personne pour le weekend");
            System.out.println("Q: quitter");
            String commande_brute = System.console().readLine(); // la methode readline permet de récuperer l'entrée
                                                                 // saisie par l'utilisateur
            String commande = commande_brute.strip().toLowerCase(); // On conserve commande brute pour éviter les
                                                                    // erreurs de syntaxe
            if (commande.equals("p")) {
                menu_p();
                commande_faite = true;
            }

            else if (commande.equals("d")) {
                System.out.println("Les dépenses du week end : " + this.we.getDepenses());
                commande_faite = true;
            }

            else if (commande.equals("t")) {
                System.out.println("Le total des dépenes du week end : " + this.we.totalDepenses() + " euros");
                commande_faite = true;
            }

            else if (commande.equals("m")) {
                System.out.println("La dépense moyenne par personne : " + this.we.depensesMoyenne() + " euros");
                commande_faite = true;
            }

            else if (commande.equals("q")) {
                quitter = true;
                commande_faite = true;
            }

            else {
                System.out.println("Commande '" + commande_brute + "' invalide.");
            }
        }
    }

    public void menu_p() {
        boolean p = false;
        Personne personne = null;
        while (!p) {
            System.out.println("P: ajouter une personne au weekend");
            System.out.println("L: liste");
            System.out.println("S: sélection");
            System.out.println("T: total des dépenses de la personne selectionnée");
            System.out.println("A: l'avoir de la personne selectionnée");
            System.out.println("Q: quitter");
            String commande_brute = System.console().readLine(); // la methode readline permet de récuperer l'entrée
                                                                 // saisie par l'utilisateur
            String commande = commande_brute.strip().toLowerCase(); // On conserve commande brute pour éviter les
                                                                    // erreurs de syntaxe
            if(commande.equals("p")){
                System.out.println("Entrez le nom de la personne : ");
                String nom = System.console().readLine();
                System.out.println("Entrez le prénom de la personne : ");
                String prenom = System.console().readLine();
                Personne nouvPersonne = new Personne(nom, prenom);
                this.we.ajouterPersonne(nouvPersonne);
                System.out.println("Vous avez ajouté : " + nouvPersonne.getNom() + " " + nouvPersonne.getPrenom() + " au weekend");
            }else if (commande.equals("l")) {
                System.out.println("Les personnes du week end : " + this.we.getAmis());
            } else if (commande.equals("s")) {
                System.out.println("Selectionner la personne numéro combien ?");
                try {
                    // la methode readline permet de récuperer l'entrée saisie par l'utilisateur
                    int numero = Integer.parseInt(System.console().readLine());
                    System.out.println("vous avez sélectionné : " + this.we.getAmis().get(numero));
                    personne = this.we.getAmis().get(numero);
                } catch (java.lang.IndexOutOfBoundsException e) {
                    System.out.println("Veuillez entrer un nombre entre 0 et " + (this.we.getAmis().size() - 1));
                } catch (java.lang.NumberFormatException e) {
                    System.out.println("Veuillez entrer uniquement des chiffres");
                }
            } else if(commande.equals("t")){
                try{
                    System.out.println(this.we.totalDepensesPersonne(personne) + " euros");
                } catch(java.lang.NullPointerException e){
                    System.out.println("Veuillez d'abord sélectionner une personne");
                }
            } else if(commande.equals("a")){
                try{
                    System.out.println(this.we.avoirPersonne(personne) + " euros");
                } catch(java.lang.NullPointerException e){
                    System.out.println("Veuillez d'abord sélectionner une personne");
                }
            } else if (commande.equals("q")) {
                p = true;
            }

            else {
                System.out.println("Commande '" + commande_brute + "' invalide.");
            }

        }
    }

    /// Affiche un message de bienvenue
    public void bienvenue() {
        System.out.println("╭────────────────────────────────────────────────────────────────────────────────────╮");
        System.out.println("│ Bienvenue! En week-end comme dans la semaine, les bons comptes font les bons amis. │");
        System.out.println("╰────────────────────────────────────────────────────────────────────────────────────╯");
    }

    /// Affiche un message d'au revoir
    public void au_revoir() {
        System.out.println("╭────────────────────────────────────────────────╮");
        System.out.println("│ Au revoir et merci d'utiliser l'application !. │");
        System.out.println("╰────────────────────────────────────────────────╯");
    }

}
