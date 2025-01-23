public class ExecutablePokemon {
public static void main(String [] args) {

Pokemon poke;
poke = new Pokemon("Bulbizarre", 30);
poke.evoluer("Herbizarre", 37);
poke.evoluer("Florizarre");
System.out.println(poke.toString()); // (1)

Pokemon poke2 = new Pokemon("Abo", 10);
poke2.evoluer("Arbock",24);
System.out.println(poke2.toString());

assert poke2.getNom() == "Arbock";
}
}
