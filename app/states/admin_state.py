import reflex as rx
from app.models import Reservation
from datetime import datetime
import logging
from collections import Counter


class AdminState(rx.State):
    is_authenticated: bool = False
    password_input: str = ""
    login_error: str = ""
    selected_date: str = datetime.now().strftime("%Y-%m-%d")
    all_reservations_data: list[Reservation] = []
    reservations: list[Reservation] = []
    total_bookings: int = 0
    total_revenue: float = 0
    top_barber_name: str = "N/A"
    top_barber_count: int = 0
    top_service_name: str = "N/A"
    status_distribution: list[dict[str, str | int]] = []
    daily_bookings: list[dict[str, str | int]] = []
    service_distribution: list[dict[str, str | int]] = []
    walk_in_client: str = ""
    walk_in_phone: str = ""
    walk_in_service: str = ""
    walk_in_barber: str = ""
    walk_in_datetime: str = ""

    @rx.event
    def set_walk_in_client(self, value: str):
        self.walk_in_client = value

    @rx.event
    def set_walk_in_phone(self, value: str):
        self.walk_in_phone = value

    @rx.event
    def set_walk_in_service(self, value: str):
        self.walk_in_service = value

    @rx.event
    def set_walk_in_barber(self, value: str):
        self.walk_in_barber = value

    @rx.event
    def set_walk_in_datetime(self, value: str):
        self.walk_in_datetime = value

    @rx.event
    def check_login(self):
        if self.password_input == "gents2024":
            self.is_authenticated = True
            self.login_error = ""
            return rx.redirect("/admin")
        else:
            self.login_error = "Contraseña incorrecta"

    @rx.event
    def logout(self):
        self.is_authenticated = False
        return rx.redirect("/admin/login")

    @rx.event
    def set_password(self, value: str):
        self.password_input = value

    @rx.event
    def set_date(self, date: str):
        self.selected_date = date
        return AdminState.load_reservations

    @rx.event
    def load_reservations(self):
        self.reservations = [
            r for r in self.all_reservations_data if r["date"] == self.selected_date
        ]

    @rx.event
    def load_analytics(self):
        self.total_bookings = len(self.all_reservations_data)
        revenue = 0.0
        barber_counts = Counter()
        service_counts = Counter()
        status_counts = Counter()
        date_counts = Counter()
        for r in self.all_reservations_data:
            try:
                price_str = r["service_price"].replace("₡", "").replace(",", "").strip()
                if price_str:
                    revenue += float(price_str)
            except Exception as e:
                logging.exception(f"Error parsing price {r['service_price']}: {e}")
            barber_counts[r["barber_name"]] += 1
            service_counts[r["service_name"]] += 1
            status_counts[r["status"]] += 1
            date_counts[r["date"]] += 1
        self.total_revenue = revenue
        if barber_counts:
            top_barber = barber_counts.most_common(1)[0]
            self.top_barber_name = top_barber[0]
            self.top_barber_count = top_barber[1]
        if service_counts:
            self.top_service_name = service_counts.most_common(1)[0][0]
        self.status_distribution = [
            {"name": k, "value": v} for k, v in status_counts.items()
        ]
        sorted_dates = sorted(date_counts.keys())
        self.daily_bookings = [
            {"date": d, "count": date_counts[d]} for d in sorted_dates
        ]
        self.service_distribution = [
            {"name": k, "value": v} for k, v in service_counts.most_common(5)
        ]

    @rx.event
    def update_status(self, reservation_id: int, new_status: str):
        for r in self.all_reservations_data:
            if r["id"] == reservation_id:
                r["status"] = new_status
                break
        return AdminState.load_reservations

    @rx.event
    async def add_walk_in(self):
        from app.states.services_state import ServicesState

        services_state = await self.get_state(ServicesState)
        walk_in_date = self.selected_date
        walk_in_time = "12:00 PM"
        service_price = "₡0"
        for s in services_state.services:
            if s["name"] == self.walk_in_service:
                service_price = s["price"]
        if self.walk_in_datetime:
            try:
                dt_obj = datetime.fromisoformat(self.walk_in_datetime)
                walk_in_date = dt_obj.strftime("%Y-%m-%d")
                walk_in_time = dt_obj.strftime("%I:%M %p")
            except Exception as e:
                logging.exception(
                    f"Error parsing walk-in datetime {self.walk_in_datetime}: {e}"
                )
        new_id = len(self.all_reservations_data) + 1
        self.all_reservations_data.append(
            {
                "id": new_id,
                "reference_number": "WALK-IN",
                "client_name": self.walk_in_client,
                "client_phone": self.walk_in_phone,
                "barber_name": self.walk_in_barber or "Sin asignar",
                "service_name": self.walk_in_service or "Sin asignar",
                "service_price": service_price,
                "date": walk_in_date,
                "time": walk_in_time,
                "status": "pending",
                "created_at": datetime.now().isoformat(),
            }
        )
        self.walk_in_client = ""
        self.walk_in_phone = ""
        self.walk_in_datetime = ""
        self.walk_in_service = ""
        self.walk_in_barber = ""
        yield AdminState.load_reservations
