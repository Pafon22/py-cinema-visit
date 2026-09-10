class CinemaHall():
    def __init__(self, number: int) -> None:
        self.number = number
    
    def movie_session(movie_name: str, customers: list["Customer"], cleaning_staff: "Cleaner") -> None:
        print("The movie started")
        customers.watch_movie()
        print("The movie finished")
        cleaning_staff.clean_hall()
