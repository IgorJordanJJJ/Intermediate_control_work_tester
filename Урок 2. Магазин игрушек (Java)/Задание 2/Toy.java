public class Toy {
    private int id;
    private String name;
    private int quantity;
    private double dropoutFrequency;

    public Toy(int id, String name, int quantity, double dropoutFrequency) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.dropoutFrequency = dropoutFrequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getDropoutFrequency() {
        return dropoutFrequency;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void setDropoutFrequency(double dropoutFrequency) {
        this.dropoutFrequency = dropoutFrequency;
    }
}
