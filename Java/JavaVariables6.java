public class JavaVariables6 {
    public static void main(String[] args){
        final int myNumber = 15;
        myNumber = 20; // will generate an error: cannot assign a value to a final variable
        System.out.println(myNumber);
    }
}