public class JavaLogicalOperators2 {
    public static void main(String[] args) {
        boolean isLoggedIn = true;
        boolean isAdmin = false;

        System.out.println("Regular user: " + (isLoggedIn && !isAdmin));
        System.out.println("Has access: " + (isLoggedIn || isAdmin));
        System.out.println("Not Logged in: " + (!isLoggedIn));
    }
}