public class JavaIncrementingandDecrementing2 {
    public static void main(String[] args) {
        int peopleInRoom = 0;

        // 3 people enter
        peopleInRoom++;
        peopleInRoom++;
        peopleInRoom++;

        System.out.println(peopleInRoom); // 3

        // 1 person leaves
        peopleInRoom--;

        System.out.println(peopleInRoom); // 2
    }
}