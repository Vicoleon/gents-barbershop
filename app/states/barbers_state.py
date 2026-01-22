import reflex as rx
from typing import TypedDict
import os
import json


class Barber(TypedDict):
    name: str
    specialty: str
    experience: str
    bio: str
    image: str


class BarbersState(rx.State):
    barbers: list[Barber] = []
    
    @rx.event
    def on_load(self):
        self.load_barbers()
        
    def load_barbers(self):
        data_path = os.path.join("data", "barbers.json")
        if os.path.exists(data_path):
            try:
                with open(data_path, "r", encoding="utf-8") as f:
                    self.barbers = json.load(f)
                return
            except Exception as e:
                print(f"Error loading barbers: {e}")
        
        # Fallback to defaults
        self.barbers = [
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
        self.save_barbers()

    def save_barbers(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        data_path = os.path.join("data", "barbers.json")
        try:
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(self.barbers, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving barbers: {e}")
    new_name: str = ""
    new_specialty: str = ""
    new_experience: str = ""
    new_bio: str = ""
    new_image: str = ""
    upload_timestamp: int = 0

    @rx.event
    def add_barber(self):
        exp_val = self.new_experience.strip()
        if exp_val:
            numeric_part = "".join(filter(str.isdigit, exp_val))
            if numeric_part and "años" not in exp_val.lower():
                exp_val = f"{numeric_part} años"
        elif not exp_val:
            exp_val = "0 años"
            
        self.barbers.append(
            {
                "name": self.new_name,
                "specialty": self.new_specialty,
                "experience": exp_val,
                "bio": self.new_bio,
                "image": self.new_image or "/placeholder.svg",
            }
        )
        self.new_name = ""
        self.new_specialty = ""
        self.new_experience = ""
        self.new_bio = ""
        self.new_image = ""
        self.save_barbers()

    @rx.event
    def delete_barber(self, name: str):
        self.barbers = [b for b in self.barbers if b["name"] != name]
        self.save_barbers()

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

    @rx.event
    async def handle_image_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
            
        upload_dir = os.path.join("assets", "uploads")
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
            
        for file in files:
            upload_data = await file.read()
            ext = os.path.splitext(file.filename)[1]
            new_id = len(self.barbers) + 1
            filename = f"barber_{new_id}{ext}"
            outfile = os.path.join(upload_dir, filename)
            
            with open(outfile, "wb") as f:
                f.write(upload_data)
                
            self.new_image = f"/uploads/{filename}"
            self.upload_timestamp = int(os.path.getmtime(outfile))
            
        return BarbersState.add_barber
