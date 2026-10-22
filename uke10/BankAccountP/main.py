from BankAccountP import BankAccountP


class Main:

    def main():

        Main.test_BankAccountP()
        

    def test_BankAccountP():

        acc1, acc2 = [BankAccountP(0, 0, 0, 100) for i in range(2)]
        assert acc1.get_balance() == 100, "Method get_balance() is not working properly"
        
        acc1.deposit(20)
        assert acc1.get_balance() == 120, "Method deposit() is not working properly"

        acc1.withdraw(50)
        assert acc1.get_balance() == 70, "Method withdraw() is not working properly"

        acc1.transfer(acc2, 30)
        assert (acc1.get_balance(), acc2.get_balance()) == (40, 130), "Method transfer() is not working properly"


if __name__ == "__main__":

    Main.main()