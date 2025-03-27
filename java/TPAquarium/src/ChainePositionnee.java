public class ChainePositionnee{
    private int posX;
	private int posY;
    private String chaine;
    private String couleur;
  	public ChainePositionnee(int posX,int posY, String chaine, String couleur)
		{
			this.chaine = chaine;
			this.posX = posX;
			this.posY = posY;
			this.couleur=couleur;
		}
	public int getPosX() {
		return this.posX;
	}
	public int getPosY() {
		return this.posY;
	}
	public String getChaine() {
		return this.chaine;
	}
	public String getCouleur() {
		return this.couleur;
	}
}
