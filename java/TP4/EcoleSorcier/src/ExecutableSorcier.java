public class ExecutableSorcier{
    public static void main(String[] Args){
        Sorcier harry = new Sorcier("harry", 10, 5);
        Sorcier hermione = new Sorcier("hermione", 9, 10);
        Sorcier ron = new Sorcier("ron", 7, 6);
        Sorcier drago = new Sorcier("drago", 5, 0);

        assert harry.estCourageux();
        assert !ron.estCourageux();

        Maison grifondor = new Maison("Grifondor");
        grifondor.ajouter("harry", 10, 5);
        grifondor.ajouter("hermione", 9, 10);
        grifondor.ajouter("ron", 7, 6);

        Maison serpentar = new Maison("Serpentar");
        serpentar.ajouter("drago", 5, 0);


        assert grifondor.nombreEleve() == 3;
        assert grifondor.contientCourageux();
        assert !serpentar.contientCourageux();

        assert grifondor.leMoinsCourageux().equals(ron);
        assert grifondor.lePlusSage().equals(hermione);

        Ecole poudlard = new Ecole("Poudlard");
        poudlard.ajouter(grifondor);
        poudlard.ajouter(serpentar);

        assert poudlard.plusGrandeMaison().equals(grifondor);

        harry.toString();

    }
}