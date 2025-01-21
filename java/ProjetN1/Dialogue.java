public class Dialogue{
    public static void main(String [] args){
        Chat felix = new Chat("Felix");
        Chat chloe = new Chat("Chloé", 5);
        Chat ozone = new Chat("Ozone", 1);
        System.out.println(chloe.getNom()); 
        chloe.miaule(); 
        System.out.println(felix.getNom());
        felix.miaule(); 
        System.out.println(ozone.getNom());
        ozone.miaule();
  }
}
