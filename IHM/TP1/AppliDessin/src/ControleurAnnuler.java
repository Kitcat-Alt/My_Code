import javafx.event.ActionEvent;
import javafx.event.EventHandler;


public class ControleurAnnuler implements EventHandler<ActionEvent>{
    private AppliDessin appli;
    
    public ControleurAnnuler(AppliDessin appli){
        this.appli = appli;
    }
    
    public void handle(ActionEvent e){
        System.out.println("Annulation");
        this.appli.annule();
    }
}
