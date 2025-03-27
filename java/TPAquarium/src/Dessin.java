import java.util.List;
import java.util.ArrayList;
public class Dessin {
    private List<ChainePositionnee> chaines;
    public Dessin() {
        this.chaines= new ArrayList<>();
    }

    public List<ChainePositionnee> getDessin() {
        return this.chaines;
    }
    
    public void ajouteChaine(int x, int y, String c, String couleur){
        this.chaines.add(new ChainePositionnee(x, y, c, couleur));}

    public void union(Dessin e){
        for(ChainePositionnee c : e.chaines)
            chaines.add(c);
    }

    public boolean contient(int posx, int posy){
        for(ChainePositionnee c: this.chaines){
            if (c.getPosX() <= posx  && c.getPosY() == posy 
                && posx < c.getPosX() + c.getChaine().length())
                return true;
        }
        return false;

    }
    public void vider(){ this.chaines.clear();}
}
