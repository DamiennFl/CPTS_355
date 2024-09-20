import java.awt.Color;

/**
 * SplitBall Class
 * The SplitBall class creates a ball which can be split into two other balls.
 * The implementation for the split is in BallGame.java, since it is
 * impractical to implement within this class.
 */
public class SplitBall extends BasicBall {

    //Constructor
    public SplitBall(double r, Color c) {
        //Call super constructor
        super(r,c);
    }

    //Return score of split ball
    @Override
    public int getScore() {
        return 10;
    }

    //Return String representation of SplitBall's type.
    @Override
    public String getType() {
        return "split";
    }
}
