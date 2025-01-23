
public class Couple {
private int premier;
private int second;
public Couple(int x, int y) {
    this.premier = x;
    this.second = y;
}

public Couple() {
    this(0, 0);
}

public Couple(int x){
    this.premier = x;
    this.second = x;
}

    public void setPremier(int premier) {
    this.premier = premier;
}

public void permuter() {
    int aux;
    aux = this.premier;
    this.premier = this.second;
    this.second = aux;
}

public int produit(){
    return this.premier * this.second;
}

public int somme() {
    return this.premier + this.second;
}

@Override
public String toString() {
    return "(" + this.premier +", "+ this.second + ")";
    }
}