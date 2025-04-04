import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurQuitter implements EventHandler<ActionEvent>{
    private AppliSomme appli;
    
    public ControleurQuitter(AppliSomme appli){
        this.appli = appli;
    }
    
    public void handle(ActionEvent e){
        this.appli.quitte();
    }
}
