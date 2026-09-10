from people.customer import Customer
from people.cinema_staff import Cleaner


class CinemaHall():
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self, movie_name: str, customers: list["Customer"],
        cleaning_staff: "Cleaner"
    ) -> None:
        print("The movie started")
        customers.watch_movie()
        print("The movie finished")
        cleaning_staff.clean_hall()
