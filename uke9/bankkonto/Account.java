class Account {
    
    private String name;
    private int accNumber;
    private float balance;
    private int transactions;


    public Account(String name, int accNumber, float balance) {

        this.name = name;
        this.accNumber = accNumber;
        this.balance = balance;
        this.transactions = 1;

    }

    public void deposit(float amount) {
        balance += amount;
        transactions += 1;

    }

    public void withdraw(float amount) {
        balance -= amount;
        transactions += 1;
    }

    public void dump() {

        System.out.printf("Account name: %s%n", name);
        System.out.printf("Account number: %d%n", accNumber);
        System.out.printf("Balance: %f%n%n", balance);
        System.out.printf("Total number of transactions: %d%n", transactions);

    }

}
