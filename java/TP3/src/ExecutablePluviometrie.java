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
    }
}
