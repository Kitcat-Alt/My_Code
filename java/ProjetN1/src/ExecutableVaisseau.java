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
  }
}
