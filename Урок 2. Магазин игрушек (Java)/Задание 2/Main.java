import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();
        store.addToy(new Toy(1, "Doll", 10, 20));
        store.addToy(new Toy(2, "Action figure", 5, 30));
        store.addToy(new Toy(3, "Puzzle", 8, 10));

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter toy id to change dropout frequency: ");
        String toyId = scanner.nextLine();
        System.out.print("Enter new dropout frequency: ");
        int dropoutFrequency = scanner.nextInt();
        scanner.nextLine(); // consume newline character
        store.updateToyDropoutFrequency(toyId, dropoutFrequency);

        System.out.println("\nBefore drawing:");
        for (Toy toy : store.getToys()) {
            System.out.println(toy.getName() + ": " + "quantity=" + toy.getQuantity() + ", dropoutFrequency=" + toy.getDropoutFrequency());
        }

        System.out.println("\nDrawing...");
        store.getPrizeToy();

        try {
            store.writePrizeToysToFile("prizeToys.txt");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        System.out.println("\nAfter drawing:");
        for (Toy toy : store.getToys()) {
            System.out.println(toy.getName() + ": " + "quantity=" + toy.getQuantity() + ", dropoutFrequency=" + toy.getDropoutFrequency());
        }
    }
}
