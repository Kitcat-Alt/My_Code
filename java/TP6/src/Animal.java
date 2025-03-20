public class Animal {
    protected String nom;
    protected double poid;
    protected String nomEnclos;

    public Animal(String nom, double poid, String nomEnclos){
        this.nom = nom;
        this.poid = poid;
        this.nomEnclos = nomEnclos;
    }

    public String getNom(){
        return this.nom;
    }

    public double getPoid(){
        return this.poid;
    }

    public String getnomEnclos(){
        return this.nomEnclos;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Animal)){return false;}
        Animal animal = (Animal) obj;
        return this.nom.equals(animal.getNom()) && this.poid == animal.getPoid();
    }
}
