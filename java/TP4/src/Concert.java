public class Concert {
    private String nomConcert;
    private String nomGroupe;

    public Concert(String nomConcert, String nomGroupe){
        this.nomConcert = nomConcert;
        this.nomGroupe = nomGroupe;
    }

    public String getNomConcert(){
        return this.nomConcert;
    }

    public String getNomGroupe(){
        return this.nomGroupe;
    }

    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Concert)){return false;}
        Concert concert = (Concert) obj;
        return concert.getNomConcert().equals(obj.getNomConcert()) && concert.getNomGroupe().equals(obj.getNomGroupe());

    }
}


