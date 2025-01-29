public class ExecutableVaisseau{
  public static void main(String [] args){
    Vaisseau faucon = new Vaisseau("Faucon Millenium", 4, 6);
    System.out.println(faucon.getNom()); 
    System.out.println(faucon.getNombrePassagers()); 
    System.out.println(faucon.getPuissance()); 
    System.out.println(faucon.transportePassagers());
    assert "Faucon Millenium".equals(faucon.getNom()); 
    assert 6 == faucon.getNombrePassagers(); 
    assert 4 == faucon.getPuissance(); 
    assert faucon.transportePassagers() : "Le Faucon Millenium transporte des passagers";
    Vaisseau chasseur = new Vaisseau("Chasseur Tie", 8);
    assert "Chasseur Tie".equals(chasseur.getNom()); 
    assert 0 == chasseur.getNombrePassagers(); 
    assert 8 == chasseur.getPuissance(); 
    assert !chasseur.transportePassagers() : "Le Chasseur Tie ne transporte pas de passagers";

    Vaisseau executor = new Vaisseau("Super Star Destroyer", 250, 38000);
    Vaisseau corvette = new Vaisseau("Corvette", 2, 80);

    Flotte empire = new Flotte();
    empire.ajoute(chasseur);
    empire.ajoute(executor);

    assert "Nouvelle Flotte".equals(empire.getNom());
    assert 2 == empire.nombreVaisseaux();
    assert 250 + 8 == empire.totalPuissance();

    Flotte alliance = new Flotte("Alliance rebelle");
    alliance.ajoute(faucon);
    alliance.ajoute("A-Wing", 11);
    alliance.ajoute("Nautilian", 175, 10000);
    alliance.ajoute(corvette);
    alliance.ajoute(new Vaisseau("B-Wing", 7, 0));

    assert "Alliance rebelle".equals(alliance.getNom());
    assert 5 == alliance.nombreVaisseaux();
    assert 4 + 11 + 175 + 2 + 7 == alliance.totalPuissance();

    assert 1 == empire.nombreDeVaisseauxSansPassagers();
    assert 2 == alliance.nombreDeVaisseauxSansPassagers();
    assert 250 == empire.puissanceDeFeuMax();
    assert 175 == alliance.puissanceDeFeuMax();
    //assert "Chasseur Tie".equals(empire.nomDuVaisseauLeMoinsPuissant());
    //assert "Corvette".equals(alliance.nomDuVaisseauLeMoinsPuissant());
  }
}
