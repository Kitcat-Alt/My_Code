public class Vecteur3F {
    private double x;
    private double y;
    private double z;

    public Vecteur3F(double x, double y, double z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3F(double x, double y){
        this.x = x;
        this.y = y;
    }
    

    public double getX(){
        return this.x;
    }

    public double getY(){
        return this.y;
    }

    public double getZ(){
        return this.z;
    }

    public void modifier(double nouvX, double nouvY, double nouvZ){
        this.x = nouvX;
        this.y = nouvY;
        this.z = nouvZ;
    }

    public double getNorme(){
        return Math.sqrt((this.getX()*this.getX())+(this.getY()*this.getY())+(this.getZ()*this.getZ()));
    }

    @Override
    public String toString(){
        return "Vecteur3f : " + "<" + this.getX() + " " + this.getY() + " " + this.getZ() + "> De norme : " + this.getNorme();
    }


}
