import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurAdditionner implements EventHandler<ActionEvent>{
    private AppliSomme appli;
    
    public ControleurAdditionner(AppliSomme appli){
        this.appli = appli;
    }
    
    public void handle(ActionEvent e){
        System.out.println("Addition");
    }
}
