import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.text.Text;
import javafx.scene.text.Font;
import javafx.scene.paint.Color;
import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.event.ActionEvent;
import javafx.util.Duration;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.KeyCode;



public class Executable extends Application {
    private Pane root;
    private Group caracteres;
    private Aquarium aquarium;
    private int hauteurTexte;
    private int largeurCaractere;
    public static void main(String[] args) {
        launch(args);
    }

    private void afficherCaracteres(){
        caracteres.getChildren().clear();
        int hauteur = (int) root.getHeight();
        for(ChainePositionnee c : aquarium.getDessin().getDessin())
        {
            Text t = new Text (c.getPosX()*largeurCaractere,
                               hauteur - c.getPosY()*hauteurTexte, 
                               c.getChaine());
            t.setFont(Font.font ("Monospaced", 10));
						t.setFill(Color.web(c.getCouleur()));
            caracteres.getChildren().add(t);
        }
    }

    private void lancerAnimation() {
        Timeline timeline = new Timeline(
                new KeyFrame(Duration.seconds(0),
                    new EventHandler<ActionEvent>() {
                        @Override public void handle(ActionEvent actionEvent) {
                            afficherCaracteres();
                        }
                    }),
                new KeyFrame(Duration.seconds(0.025))
                );
        timeline.setCycleCount(Animation.INDEFINITE);
        timeline.play();
        timeline = new Timeline(
                new KeyFrame(Duration.seconds(0),
                    new EventHandler<ActionEvent>() {
                        @Override public void handle(ActionEvent actionEvent) {
                            aquarium.evolue();
                        }
                    }),
                new KeyFrame(Duration.seconds(0.5))
                );
        timeline.setCycleCount(Animation.INDEFINITE);
        timeline.play();
    }


    @Override
        public void start(Stage primaryStage) {
            primaryStage.setTitle("Aqua IUTO");
            caracteres = new Group();
            root= new AnchorPane(caracteres);
            aquarium = new Aquarium();
            Text t=new Text("█");
            t.setFont(Font.font("Monospaced",10));
            hauteurTexte =(int) t.getLayoutBounds().getHeight();
            largeurCaractere = (int) t.getLayoutBounds().getWidth();

            Scene scene = new Scene(root,aquarium.getLargeur()*largeurCaractere,aquarium.getHauteur()*hauteurTexte);
            /*scene.addEventHandler(KeyEvent.KEY_PRESSED, (key) -> {
                if(key.getCode()==KeyCode.LEFT)
                    aquarium.toucheGauche();
                if(key.getCode()==KeyCode.RIGHT)
                    aquarium.toucheDroite();
                if(key.getCode()==KeyCode.SPACE)
                    aquarium.toucheEspace();
            });
						*/
            primaryStage.setScene(scene);
            primaryStage.setResizable(false);
            primaryStage.show();
            lancerAnimation();

        }
}
