public class Bouteille{
    private String region;
    private String appellation;
    private int millesime;

    public Bouteille(String region, String appellation, int millesime){
        this.region = region;
        this.appellation = appellation;
        this.millesime = millesime;
    }

    public String getRegion(){
        return this.region;
    }

    public String getAppellation(){
        return this.appellation;
    }

    public int getMillesime(){
        return this.millesime;
    }

    public boolean equals(Bouteille bouteille){
        boolean res;
        if(bouteille == null){
            return false;
        }
        if(this.region == bouteille.getRegion()){
            res = true;
        }

        if(this.appellation == bouteille.getAppellation()){
            res = true;
        }

        if(this.millesime == bouteille.getMillesime()){
            res = true;
        }

        else{
            res = false;
        }
        return res;
    }
}