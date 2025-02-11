public class ExecutableCave{
    public static void main(String[] args){
    // reprendre le code de la question précédente
        Cave maCave = new Cave();
        maCave.ajouteBouteille("Bordeaux", "Pomerol", 2005);
        maCave.ajouteBouteille("Bordeaux", "Pomerol", 2007);
        maCave.ajouteBouteille("Bourgogne", "Nuits St George", 2001);
        maCave.ajouteBouteille("Savoie", "Pinot Noir", 2012);
        maCave.ajouteBouteille("Bordeaux", "Pomerol", 2007);
        maCave.ajouteBouteille("Loire", "Chinon", 2017);
        assert 6 == maCave.nbBouteilles();
        assert 3 == maCave.nbBouteillesDeRegion("Bordeaux");

        Bouteille bouteille = maCave.plusVielleBouteille();
        assert "Nuits St George".equals(bouteille.getAppellation());
        System.out.println(maCave.contient("Bordeaux", "Pomerol", 2007));
        assert maCave.contient("Bordeaux", "Pomerol", 2007);
        assert !maCave.contient("Bordeaux", "Pomerol", 2003);
    }
}        