from typing import TypedDict


class Reservation(TypedDict):
    id: int
    reference_number: str
    client_name: str
    client_phone: str
    barber_name: str
    service_name: str
    service_price: str
    date: str
    time: str
    status: str
    created_at: str
