import reflex as rx
from typing import TypedDict


class Barber(TypedDict):
    name: str
    specialty: str
    experience: str
    bio: str
    image: str


class BarbersState(rx.State):
    barbers: list[Barber] = [
        {
            "name": "Alejandro M.",
            "specialty": "Master Barber & Fade Expert",
            "experience": "12 años",
            "bio": "Especialista en cortes urbanos y técnicas europeas. Apasionado por la precisión.",
            "image": "https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=1974&auto=format&fit=crop",
        },
        {
            "name": "Cristian V.",
            "specialty": "Beard Stylist & Rituals",
            "experience": "8 años",
            "bio": "Experto en el ritual de la toalla caliente y cuidado profundo de la barba.",
            "image": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=2080&auto=format&fit=crop",
        },
        {
            "name": "Julian R.",
            "specialty": "Classic Scissor Cuts",
            "experience": "15 años",
            "bio": "Maestro en técnicas clásicas a tijera y estilos tradicionales de caballero.",
            "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=2070&auto=format&fit=crop",
        },
    ]
    new_name: str = ""
    new_specialty: str = ""
    new_experience: str = ""
    new_bio: str = ""
    new_image: str = ""

    @rx.event
    def add_barber(self):
        self.barbers.append(
            {
                "name": self.new_name,
                "specialty": self.new_specialty,
                "experience": self.new_experience,
                "bio": self.new_bio,
                "image": self.new_image or "/placeholder.svg",
            }
        )
        self.new_name = ""
        self.new_specialty = ""
        self.new_experience = ""
        self.new_bio = ""
        self.new_image = ""

    @rx.event
    def delete_barber(self, name: str):
        self.barbers = [b for b in self.barbers if b["name"] != name]

    @rx.event
    def set_new_name(self, value: str):
        self.new_name = value

    @rx.event
    def set_new_specialty(self, value: str):
        self.new_specialty = value

    @rx.event
    def set_new_experience(self, value: str):
        self.new_experience = value

    @rx.event
    def set_new_bio(self, value: str):
        self.new_bio = value

    @rx.event
    def set_new_image(self, value: str):
        self.new_image = value
