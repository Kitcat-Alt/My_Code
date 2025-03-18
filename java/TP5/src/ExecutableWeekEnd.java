public class ExecutableWeekEnd {
    public static void main (String[] Args){
        Personne davy = new Personne("Davy", 37);
        Personne elie = new Personne("Elie", 27);
        Personne gaby = new Personne("Gaby", 24);
        Personne anna = new Personne("Anna", 31);
        
        Depense pain = new Depense(davy, 12, "pain");
        Depense pizza = new Depense(elie, 100, "pizza");
        Depense essence = new Depense(davy, 70, "essence");
        Depense vin = new Depense(gaby, 15, "vin");
        Depense vin2 = new Depense(elie, 10, "vin");

        WeekEnd weekend = new WeekEnd("21/09");
        
        weekend.ajoutePerticipant("Davy", 37);
        weekend.ajoutePerticipant("Elie", 27);
        weekend.ajoutePerticipant("Gaby", 24);
        weekend.ajoutePerticipant("Anna", 31);

        weekend.ajouteDepense(12, "pain", "Davy");
        weekend.ajouteDepense(100, "pizza", "Elie");
        weekend.ajouteDepense(70, "essence", "Davy");
        weekend.ajouteDepense(15, "vin", "Gaby");
        weekend.ajouteDepense(10, "vin", "Elie");

        
        //System.out.println(weekend.totalDepense(elie));
        //System.out.println(weekend.totalDepense());
        assert weekend.totalDepense() == 207;
        assert weekend.totalDepense(elie) == 110;
        //System.out.println(weekend.avoirPersonne(gaby));
        assert weekend.avoirPersonne(gaby) == 26.4;
    }


}
