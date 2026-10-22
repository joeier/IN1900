from Person import Person


class Main:

    def main():

        person = Person("John", 55, "Male")
        print(person)

        person.update_name("Karin")
        person.update_gender("Female")

        print(person)


if __name__ == "__main__":

    Main.main()