import java.awt.Color;

/**
 * ShrinkBall Class
 * The ShrinkBall class creates and modifies a ShrinkBall which shrinks each time it is clicked.
 * Once it is smaller than 25% of it's original size, it will reset at the initial size.
 */
public class ShrinkBall extends BasicBall{
    
    //Save initial radius
    public double initialRadius;

    //Constructor
    public ShrinkBall(double r, Color c) {
        //Call the superclass constructor
        super(r, c);
        initialRadius = r;
    }

    //Overriden reset Method
    //This overriden reset method resets the ball with a smaller radius, or
    //back to the initial radius.
    @Override
    public int reset() {
        //If radius is smaller than 25% of original, reset
        if(radius <= 0.25 * initialRadius) {
            radius = initialRadius;
            rx = 0.0;
            ry = 0.0;  	
            this.vx = StdRandom.uniform(-0.01, 0.01);
            this.vy = StdRandom.uniform(-0.01, 0.01);
        } else {
            //Scale ball down
            radius = radius * 0.66;
            rx = 0.0;
            ry = 0.0;
            this.vx = StdRandom.uniform(-0.01, 0.01);
            this.vy = StdRandom.uniform(-0.01, 0.01);
        }
        return 1;
    }

    //return score for ShrinkBall
    @Override
    public int getScore() {
        return 20;
    }

    //getType Method
    //Returns the type of the ball as a String.
    @Override
    public String getType() {
        return "shrink";
    }

}
