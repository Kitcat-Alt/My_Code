import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurReset implements EventHandler<ActionEvent>{
    private AppliSomme appli;
    
    public ControleurReset(AppliSomme appli){
        this.appli = appli;
    }
    
    public void handle(ActionEvent e){
        System.out.println("Reset");
        this.appli.efface();
    }
}
