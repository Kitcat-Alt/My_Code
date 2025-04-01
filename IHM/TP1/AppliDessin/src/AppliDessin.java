import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.Group; 
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.control.Slider ;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;
import javafx.geometry.Pos;
import javafx.scene.text.Font;
import javafx.geometry.Orientation;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.Background;
import javafx.event.EventHandler;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class AppliDessin extends Application {
    private Group boite;
    private int nombreDeDisques;
    private Slider slider;
    private int LARGEUR = 600;
    private int HAUTEUR = 300;
    
    @Override
    public void init(){
        // cette méthode est utilisée pour initialiser les éléments 
        // non graphiques et événtuellement graphiques autres que la Scène et le Stage
        this.slider = new Slider(5, 50, 20);
        this.boite = new Group();
        this.nombreDeDisques = 0;
    }    
    
    @Override
    public void start(Stage stage){
        // Cette méthode est le point d'entrée principal pour toutes les applications JavaFX.
        // La méthode start est appelée après le retour de la méthode init()
        // Elle doit créer la Scène et le Stage
        BorderPane root = new BorderPane();
        this.ajouteTop(root);
        this.ajouteBoutons(root);
        this.ajouteBoiteADessin(root);
        this.ajouteSlider(root);
        this.ajouteCouleurs(root);
        Scene scene = new Scene(root);
        scene.setFill(Color.OLDLACE);        
        // On connecte un Controleur de souris à la boite
        scene.setOnKeyPressed(new ControleurClavier(this)); 
        stage.setTitle("Dessinons des disques");
        stage.setScene(scene);
        stage.show();
    }

    /**
     * Ajoute un disque au dessin
     * la couleur de ce cercle est aléatoire
     * le rayon du cercle est déterminé par la valeur du curseur
     * 
     * @param  centerX l'abscisse du centre du cercle
     * @param  centerY l'ordonnée du centre du cercle
    */
    public void ajouteCercle(double centerX, double centerY){
        Circle cercle = new Circle(centerX, centerY, this.slider.getValue());
        cercle.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        this.boite.getChildren().add(cercle);
        this.nombreDeDisques++;
    }
    
    /**
     * Cette méthode supprime le dernier cercle dessiné
     */
    public void annule(){
        if (this.nombreDeDisques > 0){
            this.boite.getChildren().remove(this.boite.getChildren().size()-1);
            this.nombreDeDisques--;
        }  
    }

    /**
     * Cette méthode augmente le rayon du dernier cercle dessiné
     */
    public void augmenteLeDernierCercle(){
        Circle c = (Circle) this.boite.getChildren().get(this.boite.getChildren().size()-1);
        c.setRadius(c.getRadius()+5);
    }

    /**
     * Cette méthode diminue le rayon du dernier cercle dessiné
     */
    public void diminueLeDernierCercle(){
        Circle c = (Circle) this.boite.getChildren().get(this.boite.getChildren().size()-1);
        c.setRadius(c.getRadius()-5);
    }
    
        /**
     * Cette méthode permet de quitter l'application
     */
    public void quitter(){
        Platform.exit();
    }

    public void changeCouleurDernierCercleAleatoirement(){
        Circle c = (Circle) this.boite.getChildren().get(this.boite.getChildren().size()-1);
        c.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
    }

    /**
     * Ajoute la boite a dessin grise au milieu de la fenêtre (borderpane)
     */
    private void ajouteBoiteADessin(BorderPane border){
        Rectangle rectangle = new Rectangle(0, 0, this.LARGEUR, this.HAUTEUR);
        rectangle.setFill(Color.DARKGREY);
        this.boite.getChildren().add(rectangle);
        // On connecte un Gestionnaire d'événement souris à cette boite
        this.boite.setOnMouseClicked(new ControleurSouris(this));
        border.setCenter(boite);
    }
    /**
     * Pour afficher le "mode d'emploi" en haut de la fenêtre (borderpane)
     */
    private void ajouteTop(BorderPane border){
        Label labelA = new Label("Pour ajouter un disque :\n - utiliser le curseur à droite pour déterminer son rayon\n - cliquer dans le bloc gris au centre\n\nBouton Annuler pour effacer le dernier disque\nTouche '+' pour agrandir le rayon du dernier disque\nTouche '-' pour diminiuer le rayon du dernier disque");        
        labelA.setFont(Font.font("Arial", 20));
        BorderPane.setMargin(labelA, new Insets(20));
        border.setTop(labelA);
    }

    /**
     * Ajoute des boutons en bas de la fenêtre (borderpane)
     */
    private void ajouteBoutons(BorderPane border){
        HBox hbox = new HBox(20);
        Button boutonAnnuler = new Button("Annuler");
        Button boutonQuitter = new Button("Quitter");
        hbox.getChildren().addAll(boutonAnnuler, boutonQuitter);
        hbox.setAlignment(Pos.CENTER);  
        border.setBottom(hbox);
        BorderPane.setMargin(hbox, new Insets(20));
        boutonQuitter.setOnAction(new ControleurQuitter(this));                  
        boutonAnnuler.setOnAction(new ControleurAnnuler(this));
    }

    /**
     * Ajoute un curseur à droite de la fenêtre (borderpane)
     */
    private void ajouteSlider(BorderPane border){
        this.slider.setOrientation(Orientation.VERTICAL);
        this.slider.setShowTickMarks(true);
        this.slider.setShowTickLabels(true);
        BorderPane.setMargin(this.slider, new Insets(20));
        border.setRight(this.slider);
    }

    /**
     * Ajoute une boite de couleurs à gauche de la fenêtre (borderpane)
     */
    private void ajouteCouleurs(BorderPane border){
        List<Color> couleurs = Arrays.asList(Color.BLUE, Color.BISQUE, Color.BROWN, Color.CYAN, Color.FUCHSIA);
        GridPane gridpane = new GridPane();
        for (int i=0; i<couleurs.size(); i++){
            Button button = new Button();
            button.setBackground(new Background(new BackgroundFill(couleurs.get(i) ,null, new Insets(1))));
            gridpane.add(button, 1, i);
            gridpane.add(new Label(couleurs.get(i).toString()), 0, i);
        }
        BorderPane.setMargin(gridpane, new Insets(20));
        border.setLeft(gridpane);
    }
}
