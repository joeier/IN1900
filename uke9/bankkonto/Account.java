package bankkonto;


public class Account {
    
    private String name;
    private int accNumber;
    private float balance;


    public Account(String name, int accNumber, float balance) {

        this.name = name;
        this.accNumber = accNumber;
        this.balance = balance;

    }

    public void dump() {

        String message = String.format("Account name: %s", name);

        System.out.println(message);

    }

}
