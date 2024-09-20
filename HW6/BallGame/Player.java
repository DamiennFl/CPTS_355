
/**
 * Player Class
 * Player class creates and modifies a Player object which has information about the score,
 * and amount of hits for each type of ball.
 */
public class Player {

    //Since integers are immutable, we can just make them public and not have to write
    //getters and setters.
    public int score;
    public int totalHits;
    public int basicHits;
    public int splitHits;
    public int shrinkHits;
    public int bounceHits;

    //Constructor
    public Player() {
        //Set all initial values to 0
        this.score = 0;
        this.totalHits = 0;
        this.basicHits = 0;
        this.splitHits = 0;
        this.shrinkHits = 0;
        this.bounceHits = 0;
    }
}