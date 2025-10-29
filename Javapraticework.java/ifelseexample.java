public class IfElseExample {
    public static void main(String[] args) {
        example1();
        example2();
        example3();
    }

    private static void example1() {
        int number = 10;
        if (number > 15) {
            System.out.println("The number is greater than 15.");
        } else {
            System.out.println("The number is 15 or less.");
        }
    }

    private static void example2() {
        int number = 20;
        if (number % 2 == 0) {
            System.out.println("The number is even.");
        } else {
            System.out.println("The number is odd.");
        }
    }

    private static void example3() {
        int number = 10;
        if (number > 0) {
            System.out.println("The number is positive.");
        } else if (number < 0) {
            System.out.println("The number is negative.");
        } else {
            System.out.println("The number is zero.");
        }
    }
}

int number = 20;
if (number > 5) {
  System.out.println("Greater than 5");
}