package vektorlek;
public class Vector {

    private static int numberOfVectors = 0;

    private int x;
    private int y;
    private int z;
    

    public static int getVectorNumber() {

        return numberOfVectors;

    }

    public Vector(int x, int y, int z) {

        numberOfVectors++;

        this.x = x;
        this.y = y;
        this.z = z;

    }

}
