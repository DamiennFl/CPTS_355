/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

public class BallGame { 

    public static void main(String[] args) {
  
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
            //toLowerCase just in case of any capitalization
    		ballTypes[i] = args[index].toLowerCase();
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	Player player = new Player();
    	
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        //ArrayList of balls
        ArrayList<BasicBall> balls = new ArrayList<BasicBall>();
        //For each ball in the list,
        for(int i = 0; i < numBalls; i++) {
            //If basic, add a BasicBall, if shrink, add a ShrinkBall, etc.
            if(ballTypes[i].equals("basic")) {
                BasicBall ball = new BasicBall(ballSizes[i], Color.RED);
                balls.add(ball);
            } else if(ballTypes[i].equals("shrink")) {
                BasicBall ball = new ShrinkBall(ballSizes[i], Color.BLUE);
                balls.add(ball);
            } else if (ballTypes[i].equals("bounce")) {
                BasicBall ball = new BounceBall(ballSizes[i], Color.GREEN);
                balls.add(ball);
            } else if (ballTypes[i].equals("split")) {
                BasicBall ball = new SplitBall(ballSizes[i], Color.YELLOW);
                balls.add(ball);
            //Should not happen if input is correct.
            } else {
                System.out.println("Ball not added, input was incorrect.");
            }
        }
        //The amount of balls is the size of the ArrayList.
   		numBallsinGame = balls.size();
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

            //For each ball, call it's move method. BounceBall is the only
            //ball type with an overriden move method, the rest call the default one.
            for(int i = 0; i < balls.size(); i++) {
                BasicBall ball = balls.get(i);
                ball.move();
            }

            //Synchronization object to help concurrency issues. Necessary for Java thread synchronization
            final Object ballsLock = new Object();
            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //For each ball,
                for(int i = 0; i < balls.size(); i++) {
                    //Get the ball,
                    BasicBall ball = balls.get(i);
                    //If it is hit,
                    if (ball.isHit(x,y)) {
                        //Increase total hits,
                        player.totalHits++;
                        //For each type, add the specific hit and add score.
                        if(ball.getType().equals("basic")) {
                            player.basicHits++;
                            player.score += ball.getScore();
                        }
                        if(ball.getType().equals("shrink")) {
                            player.shrinkHits++;
                            player.score += ball.getScore();
                        }
                        if(ball.getType().equals("bounce")) {
                            player.bounceHits++;
                            player.score += ball.getScore();
                        }
                        //For the split balls, we also add another copy of the initial ball to the ArrayList.
                        if(ball.getType().equals("split")) {
                            //Synchronize to help concurrency errors.
                            synchronized(ballsLock) {
                                player.splitHits++;
                                player.score += ball.getScore();
                                //Initially this was a method in BasicBall. You can see it there.
                                SplitBall newBall = new SplitBall(ball.radius, ball.color);
                                //Add the ball
                                balls.add(newBall);
                            }
                        }
                        //All of the balls need to be reset once hit, so this calls for any type of ball.
                    	ball.reset();
                    }
                }
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //For each ball, if it is not out, draw it.
            for(int i = 0; i < balls.size(); i++) {
                BasicBall ball = balls.get(i);
                if (ball.isOut == false) { 
                    ball.draw();
                    numBallsinGame++;
                }
            }
            
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.65, 0.85, "Total Hits: "+ String.valueOf(player.totalHits));
            StdDraw.text(-0.65, 0.80, "Total Score: "+ String.valueOf(player.score));
            StdDraw.show();
            StdDraw.pause(20);
        }
        //Once game is over, print final score and stats.
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            StdDraw.setPenColor(StdDraw.YELLOW);
            font = new Font("Arial", Font.BOLD, 18);
            StdDraw.setFont(font);
            //Final score and hits for each type of ball.
            StdDraw.text(0.0, -0.10, "Score: "+ String.valueOf(player.score));
            StdDraw.text(0.0, -0.15, "Basic Hits: "+ String.valueOf(player.basicHits));
            StdDraw.text(0.0, -0.20, "Split Hits: "+ String.valueOf(player.splitHits));
            StdDraw.text(0.0, -0.25, "Shrink Hits: "+ String.valueOf(player.shrinkHits));
            StdDraw.text(0.0, -0.30, "Bounce Hits: "+ String.valueOf(player.bounceHits));
            StdDraw.show();
            StdDraw.pause(20);            StdDraw.show();
            StdDraw.pause(10);           
        }
    }
}