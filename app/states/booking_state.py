import reflex as rx
from app.states.barbers_state import Barber
from app.states.services_state import Service
from app.models import Reservation
from datetime import datetime
import random
import string


class BookingState(rx.State):
    is_open: bool = False
    current_step: int = 1
    selected_barber: Barber | None = None
    selected_service: Service | None = None
    selected_date: str = ""
    selected_time: str = ""
    client_name: str = ""
    client_phone: str = ""
    booking_reference: str = ""
    time_slots: list[str] = [
        "10:00 AM",
        "10:30 AM",
        "11:00 AM",
        "11:30 AM",
        "12:00 PM",
        "12:30 PM",
        "01:00 PM",
        "01:30 PM",
        "02:00 PM",
        "02:30 PM",
        "03:00 PM",
        "03:30 PM",
        "04:00 PM",
        "04:30 PM",
        "05:00 PM",
        "05:30 PM",
        "06:00 PM",
        "06:30 PM",
        "07:00 PM",
        "07:30 PM",
    ]

    @rx.event
    def open_modal(self):
        self.is_open = True
        self.current_step = 1
        self.selected_date = datetime.now().strftime("%Y-%m-%d")
        self.selected_time = ""
        self.client_name = ""
        self.client_phone = ""
        self.booking_reference = ""

    @rx.event
    def close_modal(self):
        self.is_open = False

    @rx.event
    def set_step(self, step: int):
        self.current_step = step

    @rx.event
    def next_step(self):
        if self.current_step < 6:
            self.current_step += 1

    @rx.event
    def prev_step(self):
        if self.current_step > 1:
            self.current_step -= 1

    @rx.event
    def select_barber(self, barber: Barber):
        self.selected_barber = barber
        self.next_step()

    @rx.event
    def select_service(self, service: Service):
        self.selected_service = service
        self.next_step()

    @rx.event
    def set_date(self, date: str):
        self.selected_date = date

    @rx.event
    def set_time(self, time: str):
        self.selected_time = time

    @rx.event
    def set_client_name(self, name: str):
        self.client_name = name

    @rx.event
    def set_client_phone(self, phone: str):
        self.client_phone = phone

    @rx.event
    async def confirm_booking(self):
        from app.states.admin_state import AdminState

        admin_state = await self.get_state(AdminState)
        self.booking_reference = "GENTS-" + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        barber_name = (
            self.selected_barber["name"] if self.selected_barber else "No seleccionado"
        )
        service_name = (
            self.selected_service["name"]
            if self.selected_service
            else "No seleccionado"
        )
        service_price = self.selected_service["price"] if self.selected_service else "0"
        new_id = len(admin_state.all_reservations_data) + 1
        new_res: Reservation = {
            "id": new_id,
            "reference_number": self.booking_reference,
            "client_name": self.client_name,
            "client_phone": self.client_phone,
            "barber_name": barber_name,
            "service_name": service_name,
            "service_price": service_price,
            "date": self.selected_date,
            "time": self.selected_time,
            "status": "confirmed",
            "created_at": datetime.now().isoformat(),
        }
        admin_state.all_reservations_data.append(new_res)
        self.next_step()

    @rx.event
    def start_booking_with_barber(self, barber: Barber):
        self.selected_barber = barber
        self.selected_service = None
        self.is_open = True
        self.current_step = 2

    @rx.event
    def start_booking_with_service(self, service: Service):
        self.selected_service = service
        self.selected_barber = None
        self.is_open = True
        self.current_step = 1

    @rx.var
    def step_title(self) -> str:
        if self.current_step > 5:
            return "CONFIRMADO"
        return [
            "SELECCIONA TU BARBERO",
            "ELIGE EL SERVICIO",
            "FECHA Y HORA",
            "TUS DATOS",
            "CONFIRMACIÓN",
        ][self.current_step - 1]

    @rx.var
    def can_progress_from_date(self) -> bool:
        return self.selected_date != "" and self.selected_time != ""

    @rx.var
    def can_progress_from_client_info(self) -> bool:
        return self.client_name != "" and self.client_phone != ""
