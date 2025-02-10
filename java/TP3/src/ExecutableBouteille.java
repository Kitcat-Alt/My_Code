public class ExecutableBouteille{
    public static void main(String[] args){
        Bouteille pomerol = new Bouteille("Bordeaux", "Pomerol", 2007);
        assert "Bordeaux".equals(pomerol.getRegion());
        assert "Pomerol".equals(pomerol.getAppellation());
        assert 2007 == pomerol.getMillesime();
        Bouteille pomerol2007 = new Bouteille("Bordeaux", "Pomerol", 2007);
        Bouteille pomerol2003 = new Bouteille("Bordeaux", "Pomerol", 2003);
        assert pomerol.equals(pomerol2007);
        assert !pomerol.equals(pomerol2003);
    }   
}