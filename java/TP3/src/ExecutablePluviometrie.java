public class ExecutablePluviometrie{
    public static void main(String[] args){
    Pluviometrie s35 = new Pluviometrie(2022, 35);
    s35.setPrecipitation(0, 3);
    s35.setPrecipitation(2, 0);
    s35.setPrecipitation(3, 0);
    s35.setPrecipitation(4, 16);
    s35.setPrecipitation(5, 3);
    s35.setPrecipitation(6, 0);
    System.out.println(s35.getPluie(1));
    //null
    System.out.println(s35.quantiteTotale());
    //22
    System.out.println(s35.quantiteMax());
    //16
    System.out.println(s35.estPluvieuse());
    //true

    assert s35.getPluie(0) == 3;
    assert s35.quantiteMax() == 16;
    assert s35.quantiteTotale() == 22;
    assert s35.estPluvieuse();

    Pluviometrie s36 = new Pluviometrie(2025, 36);
    s36.setPrecipitation(0, 0);
    s36.setPrecipitation(1, 8);
    s36.setPrecipitation(3, 0);
    s36.setPrecipitation(4, 42);
    s36.setPrecipitation(5, 0);
    s36.setPrecipitation(6, 14);

    assert s36.getPluie(4) == 42;
    assert s36.quantiteMax() == 42;
    assert s36.quantiteTotale() == 64;
    assert !s36.estPluvieuse();
    }
}
