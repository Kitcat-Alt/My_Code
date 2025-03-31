public class Personne implements Comparable<Personne>{
    private String prenom;
    private int age;

    public Personne(String prenom, int age){
        this.prenom = prenom;
        this.age = age;
    }

    public int getAge(){
        return this.age;
    }
    
    @Override
    public int compareTo(Personne p){
        return this.prenom.compareTo(p.prenom);
    }

    @Override
    public String toString(){
        return this.prenom + " "  + this.age;
    }

    @Override
    public boolean equals(Object o){
        if(o == null){return false;}
        if(o == this){return true;}
        if(!(o instanceof Personne)){return false;}
        Personne pers = (Personne) o;
        return this.prenom.equals(pers.prenom) && this.age == pers.age;
    }
}
