public class Pion{
    private int posX;
    private int posY;
    private String nom;

    public Pion(int x , int y , String nom){
        this.posX = x;
        this.posY = y;
        this.nom = nom;
    }

    public int getPosX(){
        return this.posX;
    }

    public int getPosY(){
        return this.posY;
    }

    public void deplacer(int nextX, int nextY){
        this.posX = nextX;
        this.posY = nextY;
    }

}