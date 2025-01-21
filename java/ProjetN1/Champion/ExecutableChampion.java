public class ExecutableChampion {
    public static void main(String [] args) {
        /* Création des instances */
        Champion teemo = new Champion("Teemo", 37, 7, 0);
        Champion darius = new Champion("Darius", 38, 11, 0);     
        Champion sona =  ...
        System.out.println(sona.toString());
        // Sona : pv=27, attaque=3, soin=3
        teemo.combat(darius);
        teemo.boitUnePotionDeSoin();
        System.out.println("premier combat");
        System.out.println(darius.toString());
        System.out.println(teemo.toString());        
        while (teemo.estEnVie() || darius.estEnVie()){
             sona.soigne(teemo);
             teemo.combat(darius);
        }
        System.out.println("fin du combat");
        System.out.println(darius.toString());
        System.out.println(teemo.toString());            
   }
}
