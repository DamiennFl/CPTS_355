import java.awt.Color;

/**
 * BounceBall Class
 * The BounceBall class creates and modifies a BounceBall
 * which bounces against the sides of the window 3 times before disappearing.
 */
public class BounceBall extends BasicBall {
    
    //Amount of bounces
    public int bounceCount;
    
    //Constructor
    public BounceBall(double r, Color c) {
        //Call super constructor
        super(r,c);
        this.bounceCount = 0;
    }

    //Overriden move Method
    //This overriden move method bounces the ball if the bouncecount is less than 3,
    //otherwise lets the ball exit the screen.
    @Override
    public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if (bounceCount <= 3) {
            //Set isOut to false so the ball doesn't register as out
            isOut = false;
            //Minus the radius for a nicer looking bounce
            if (Math.abs(rx) > 1.0 - radius) {
                //Reverse
                vx = -vx;
                bounceCount++;
            }
            //Minus the radius for a nicer looking bounce
            if (Math.abs(ry) > 1.0 - radius) {
                //Reverse
                vy = -vy;
                bounceCount++;
            }
        //Once desired amount of bounces has been reached, let the ball exit.
        } else {
            isOut = true;
        }
    }

    //Overriden reset Method
    //This overriden reset method resets the ball in the same way as the BasicBall,
    //but also resets the amount of bounces.
    @Override
    public int reset() {
        super.reset();
        this.bounceCount = 0;
        return 1;
    }

    //Return BounceBall score
    @Override
    public int getScore() {
        return 15;
    }

    //getType Method
    //Returns the type of BounceBall as a String.
    @Override
    public String getType() {
        return "bounce";
    }
}