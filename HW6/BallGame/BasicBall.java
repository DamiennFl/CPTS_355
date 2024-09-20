/******************************************************************************
 *  Compilation:  javac ColoredBall.java
 *  Execution:    java ColoredBall
 *  Dependencies: StdDraw.java
 *
 *  Implementation of a 2-d ball moving in square with coordinates
 *  between -1 and +1. Bounces off the walls upon collision.
 *  
 *
 ******************************************************************************/

import java.awt.Color;
//import java.util.ArrayList;

public class BasicBall { 
    protected double rx, ry;         // position
    protected double vx, vy;         // velocity
    protected double radius;         // radius
    protected final Color color;     // color
    public boolean isOut;
    

    // constructor
    public BasicBall(double r, Color c) {
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        radius = r;
        color = c;
        isOut = false;
    }
   
    // move the ball one step
    public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        	isOut = true;
    }

    // draw the ball
    public void draw() { 
    	if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
    	} else
    		isOut = true;
    	
    }

    //reset ball position and randomize movement
    public int reset() {
        rx = 0.0;
        ry = 0.0;  	
        //Change movement
        this.vx = StdRandom.uniform(-0.01, 0.01);
        this.vy = StdRandom.uniform(-0.01, 0.01);
        return 1;
    }

    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
			return true;
		else return false; 

    }
    public int getScore() {
    	return 25;
    }
    
    public double getRadius() {
    	return radius;
    }

    //getType Method
    //getType returns the type of this ball as a String.
    public String getType() {
        return "basic";
    }

    //Tried to make this a method within BasicBall, however I found that by putting it in the game code,
    //there was a lower chance of there being thread synchronization problems. When too many balls are clicked at the
    //same time, it produces a heap error because the list of ball is trying to be modified by too many threads.
    //When it's in BallGame.java, it crashes less, honestly not sure why.

    /*public synchronized void addBall(ArrayList<BasicBall> balls, double r, Color c) {
        SplitBall newBall = new SplitBall(r, c);
        balls.add(newBall);
    }*/
}
