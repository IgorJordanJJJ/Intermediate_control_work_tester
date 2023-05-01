import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyStore {
    private List<Toy> toys = new ArrayList<>();
    private List<Toy> prizeToys = new ArrayList<>();

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void updateToyDropoutFrequency(String toyId, int newDropoutFrequency) {
        for (Toy toy : toys) {
            if (toy.getId() == Integer.parseInt(toyId)) {
                toy.setDropoutFrequency(newDropoutFrequency);
                return;
            }
        }
    }

    public void getPrizeToy() {
        Random random = new Random();
        int totalDropoutFrequency = 0;
        for (Toy toy : toys) {
            totalDropoutFrequency += toy.getDropoutFrequency();
        }
        int randomNumber = random.nextInt(100) + 1; // random number between 1 and 100
        int cumulativeDropoutFrequency = 0;
        for (Toy toy : toys) {
            cumulativeDropoutFrequency += toy.getDropoutFrequency();
            if (randomNumber <= (cumulativeDropoutFrequency * 100 / totalDropoutFrequency)) {
                toy.setQuantity(toy.getQuantity() - 1);
                prizeToys.add(toy);
                return;
            }
        }
    }

    public void writePrizeToysToFile(String filename) throws IOException {
        FileWriter writer = new FileWriter(filename);
        for (Toy toy : prizeToys) {
            writer.write(toy.getId() + "," + toy.getName() + "\n");
        }
        writer.close();
        prizeToys.clear();
    }

    public List<Toy> getToys() {
        return new ArrayList<>(toys);
    }

    public List<Toy> getPrizeToys() {
        return new ArrayList<>(prizeToys);
    }
}
