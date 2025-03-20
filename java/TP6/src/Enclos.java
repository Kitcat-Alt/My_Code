import java.util.List;
import java.util.ArrayList;

public class Enclos {
    private String nomEnclos;
    private double superficie;

    public Enclos(String nom, double superficie){
        this.nomEnclos = nom;
        this.superficie = superficie;
    }

    public String getnomEnclos(){
        return this.nomEnclos;
    }

    public double getSuperficie(){
        return this.superficie;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Animal)){return false;}
        Enclos enclos = (Enclos) obj;
        return this.nomEnclos.equals(enclos.getnomEnclos()) && this.superficie == enclos.getSuperficie();
    }
}
