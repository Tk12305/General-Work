public class JavaVariables6 {
    public static void main(String[] args){
        final int myNum = 15;
        myNum = 20; // will generate an error: cannot assign a value to a final variable
        System.out.println(myNum);
    }
}