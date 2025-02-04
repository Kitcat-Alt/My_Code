public class ExecutableMorse {
    public static void main(String[] Args){
        Lettre n = new Lettre('N');
        assert n.toChar () == 'N';
        assert n.toMorse ().equals("===_=");

        Lettre a = new Lettre("=_===");
        assert a.toMorse ().equals("=_===");
        assert a.toChar () == 'A';

        assert n.toNumero() == 13;

    }
}
