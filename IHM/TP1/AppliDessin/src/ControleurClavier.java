import javafx.scene.input.KeyEvent;
import javafx.scene.input.KeyCode;
import javafx.event.EventHandler;

public class ControleurClavier implements EventHandler<KeyEvent>{
    private AppliDessin appli;
    
    public ControleurClavier(AppliDessin appli){
        this.appli = appli;
    }
    
    public void handle(KeyEvent e){       
        if (e.getCode().equals(KeyCode.ADD) || e.getCode().equals(KeyCode.EQUALS)){
            System.out.println("+");
            this.appli.augmenteLeDernierCercle();
        }

        if(e.getCode().equals(KeyCode.SUBTRACT) || e.getCode().equals(KeyCode.MINUS)){
            System.out.println("-");
            this.appli.diminueLeDernierCercle();
        }

        if(e.getCode().equals(KeyCode.MULTIPLY) ||  e.getCode().equals(KeyCode.ASTERISK)){
            System.out.println("*");
            this.appli.changeCouleurDernierCercleAleatoirement();
        }
    }
}
