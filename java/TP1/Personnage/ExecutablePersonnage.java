public class ExecutablePersonnage {
    public static void main(String [] args) {
        Personnage nain = new Personnage("Gimli", 65, 15);
        System.out.println(nain.getNom());
        System.out.println(nain.getTailleDesOreilles());
        System.out.println(nain.getBarbe());
        // Tests
        assert nain.getTailleDesOreilles() == 15;
        assert nain.getBarbe() == 65;  
    }
}
