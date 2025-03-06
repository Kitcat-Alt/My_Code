public class Executable {
    public static void main(String[] args) {
    Spectateur paul = new Spectateur("Smith","Paul");
    Spectateur julie = new Spectateur("Martin","Julie");
    Concert concert1 = new Concert("divide","u2");
    Concert concert2 = new Concert("alive","daft punk");
    Concert concert3 = new Concert("memento","depeche mode");
    Festival fest1 = new Festival("festival");
    fest1.ajouterConcert(concert1);
    fest1.ajouterConcert(concert2);
    fest1.ajouterConcert(concert3);
    fest1.reserver(paul, concert2 ,50);
    fest1.reserver(julie, concert1 ,40);
    fest1.reserver(julie, concert2 ,40);
    fest1.reserver(paul, concert3, 90);
    System.out.println(fest1.nombreConcert());
    //3
    System.out.println(fest1.nombreBilletConcert(concert2));
    //2
    }
}
