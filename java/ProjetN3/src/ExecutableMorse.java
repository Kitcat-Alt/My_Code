public class ExecutableMorse {
    public static void main(String[] Args){
        Lettre n = new Lettre('N');
        Texte phrase = new Texte("BA BA");
        assert n.toChar() == 'N';
        assert n.toMorse().equals("===_=");

        Lettre a = new Lettre("=_===");
        assert a.toMorse().equals("=_===");
        assert a.toChar() == 'A';

        assert n.toNumero() == 13;

        System.out.println(phrase.toString());
        System.out.println(phrase.toMorse());


        System.out.println(Texte.decode("===_=_=_=___=_===_______===_=_=_=___=_==="));
    }
}
