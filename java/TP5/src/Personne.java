public class Personne {
    private String prenom;
    private int age;

    public Personne(String prenom, int age){
        this.prenom = prenom;
        this.age = age;
    }

    public String getPrenom(){
        return this.prenom;
    }

    public int getAge(){
        return this.age;
    }

    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Personne)){return false;}
        Personne pers = (Personne) obj;
        return this.prenom.equals(pers.getPrenom()) && this.age == pers.getAge();  
    }
}
