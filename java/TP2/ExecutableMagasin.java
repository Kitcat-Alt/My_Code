public class ExecutableMagasin {
    public static void main(String[] Args){
        Magasin fleurus = new Magasin("Fleurus", true, false);
        Ville trainou = new Ville("Trainou");
        trainou.ajouteMagasin("BeauMagasin", true, true);
        trainou.ajouteMagasin("Venir", false, true);
        trainou.ajouteMagasin("Magnifique", false, true);
        trainou.ajouteMagasin("Bauchamp", true, false);

        trainou.ouvertsLeLundi();
        trainou.toString();

        assert "Fleurus".equals(fleurus.getNom());
        assert fleurus.getOuvertDimanche() == false;
        assert fleurus.getOuvertLundi() == true;

    }    
}
