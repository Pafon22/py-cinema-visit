from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_instances_list = [
        Customer(customer.name, customer.food)
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for i in range(len(customers_instances_list)):
        CinemaBar.sell_product(
            product=customers_instances_list[i].food,
            customer=customers_instances_list[i]
        )
    CinemaHall.movie_session(
        movie_name=movie, customers=customers, cleaning_staff=cleaner
    )
    cleaner.clean_hall(hall_number)