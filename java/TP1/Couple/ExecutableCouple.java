
public class ExecutableCouple {
public static void main(String [] args) {
    Couple unCouple = new Couple(5, -4);
    System.out.println(unCouple.toString()); // (1)
    System.out.println(unCouple.somme()); // (2)
    Couple unAutreCouple = new Couple();
    unAutreCouple.setPremier(7);
    unAutreCouple.permuter();
    System.out.println(unAutreCouple.toString()); // (3)
    System.out.println(unCouple.produit());
    Couple autreCouple = new Couple(5);
    System.out.println(autreCouple.toString());

    // Tests pour les méthodes somme() et produit() de Couple
    Couple exemple;
    exemple = new Couple(3, -8);
    assert exemple.somme() == -15; // FAUX !!!
    assert exemple.produit() == -24;
    exemple = new Couple();
    assert exemple.somme() == 0;
    assert exemple.produit() == 0;
    exemple = new Couple(7);
    assert exemple.somme() == 14;
    assert exemple.produit() == 49;
    }
}