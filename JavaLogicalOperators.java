public class JavaLogicalOperators {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c = 30;

        // Using logical AND (&&) operator
        if (a < b && b < c) {
            System.out.println("Both conditions are true: a < b and b < c");
        }

        // Using logical OR (||) operator
        if (a > b || b < c) {
            System.out.println("At least one condition is true: a > b or b < c");
        }

        // Using logical NOT (!) operator
        if (!(a > b)) {
            System.out.println("Condition is false: a is not greater than b");
        }
    }
}