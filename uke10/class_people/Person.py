class Person:

    def __init__(self, name: str, age: int, gender: str):

        self._name = name
        self._age = age
        self._gender = gender


    def __str__(self):

        return f"{self._name}, {self._age}, {self._gender}"


    def update_name(self, new: str):
        self._name = new

    def update_age(self, new: int):
        self._age = new

    def update_gender(self, new: str):
        self._gender = new