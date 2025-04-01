import javafx.scene.input.MouseEvent;
import javafx.event.EventHandler;

public class ControleurSouris implements EventHandler<MouseEvent>{
    private AppliDessin appli;
    
    public ControleurSouris(AppliDessin appli){
        this.appli = appli;
    }
    
    public void handle(MouseEvent event){
        System.out.println("Click");
        this.appli.ajouteCercle(event.getX(), event.getY());
    }
}
