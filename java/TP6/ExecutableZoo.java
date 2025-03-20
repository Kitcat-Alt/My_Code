public class ExecutableZoo {
    public static void main(String Args[]){

        Zoo beauval = new Zoo("Beauval");

        Enclos domestique = new Enclos("domestique", 40);
        Enclos savane = new Enclos("savane", 200);

        Animal chat = new Animal("Danette", 3.6, "domestique");
        Animal chien = new Animal("Juna", 10, "domestique");
        Animal elephant = new Animal("Simba", 6000, "savane");
        Animal giraffe = new Animal("celestine", 50, "savane");

        beauval.ajouteEnclos(domestique);
        beauval.ajouteEnclos(savane);

        beauval.ajouteAnimal(chat);
        beauval.ajouteAnimal(chien);
        beauval.ajouteAnimal(elephant);
        beauval.ajouteAnimal(giraffe);

        System.out.println("test");
        System.out.println(beauval.toString());
        



    }
}
