import java.util.Random;
public class Executable {
    public static void main(String[] args) {
        Random r = new Random(36);
        System.out.println(r.nextInt(10000));
    }
}