import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class ControleurAdditionner implements EventHandler<ActionEvent>{
    private AppliSomme appli;
    
    public ControleurAdditionner(AppliSomme appli){
        this.appli = appli;
    }
    
    public void handle(ActionEvent e){
        try{
            this.appli.additionne();
            System.out.println("Addition");
        }catch(NumberFormatException y){
            System.out.println("Veuillez entrer uniquement des nombres");
        }
    }
}
