import reflex as rx
from typing import TypedDict
import os
import json


class Service(TypedDict):
    id: int
    name: str
    description: str
    duration: str
    price: str
    category: str
    image: str


class ServicesState(rx.State):
    services: list[Service] = []
    
    @rx.event
    def on_load(self):
        self.load_services()
        
    def load_services(self):
        data_path = os.path.join("data", "services.json")
        if os.path.exists(data_path):
            try:
                with open(data_path, "r", encoding="utf-8") as f:
                    self.services = json.load(f)
                return
            except Exception as e:
                print(f"Error loading services: {e}")
        
        # Fallback to defaults if file doesn't exist or error
        self.services = [
            {
                "id": 1,
                "name": "Corte de Autor",
                "description": "Asesoría de imagen, corte personalizado, lavado premium y peinado final.",
                "duration": "45 min",
                "price": "₡12,000",
                "category": "Cortes",
                "image": "https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=2074&auto=format&fit=crop",
            },
            {
                "id": 2,
                "name": "Corte & Barba Ritual",
                "description": "Experiencia completa de grooming con toallas calientes y perfilado a navaja.",
                "duration": "90 min",
                "price": "₡20,000",
                "category": "Combos",
                "image": "https://images.unsplash.com/photo-1622286342621-4bd786c2447c?q=80&w=2070&auto=format&fit=crop",
            },
            {
                "id": 3,
                "name": "Barba Express",
                "description": "Limpieza, hidratación y perfilado rápido para mantener tu estilo impecable.",
                "duration": "30 min",
                "price": "₡8,000",
                "category": "Barba",
                "image": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=2070&auto=format&fit=crop",
            },
            {
                "id": 4,
                "name": "Facial Nunciatura",
                "description": "Limpieza profunda, exfoliación y mascarilla relajante para la piel masculina.",
                "duration": "40 min",
                "price": "₡15,000",
                "category": "Faciales",
                "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1974&auto=format&fit=crop",
            },
        ]
        self.save_services()

    def save_services(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        data_path = os.path.join("data", "services.json")
        try:
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(self.services, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving services: {e}")
    selected_category: str = "Todos"
    categories: list[str] = ["Todos", "Cortes", "Barba", "Faciales", "Combos"]
    new_name: str = ""
    new_desc: str = ""
    new_duration: str = ""
    new_price: str = ""
    new_category: str = "Cortes"
    new_image: str = ""
    upload_timestamp: int = 0

    @rx.var
    def filtered_services(self) -> list[Service]:
        if self.selected_category == "Todos":
            return self.services
        return [s for s in self.services if s["category"] == self.selected_category]

    @rx.event
    def set_filter(self, category: str):
        self.selected_category = category

    @rx.event
    def add_service(self):
        new_id = len(self.services) + 1
        
        # Format price to colones with commas
        price_val = self.new_price.strip()
        if price_val:
            # Extract only digits to format
            numeric_part = "".join(filter(str.isdigit, price_val))
            if numeric_part:
                try:
                    formatted_price = f"₡{int(numeric_part):,}"
                    price_val = formatted_price
                except (ValueError, TypeError):
                    if not price_val.startswith("₡"):
                        price_val = f"₡{price_val}"
        
        # Ensure we have a valid image path or placeholder
        img_path = self.new_image if self.new_image else "/placeholder.svg"
        
        self.services.append(
            {
                "id": new_id,
                "name": self.new_name,
                "description": self.new_desc,
                "duration": self.new_duration,
                "price": price_val or "₡0",
                "category": self.new_category,
                "image": img_path,
            }
        )
        self.new_name = ""
        self.new_desc = ""
        self.new_duration = ""
        self.new_price = ""
        self.new_image = ""
        self.save_services()

    @rx.event
    def delete_service(self, service_id: int):
        self.services = [s for s in self.services if s["id"] != service_id]
        self.save_services()

    @rx.event
    def set_new_name(self, value: str):
        self.new_name = value

    @rx.event
    def set_new_desc(self, value: str):
        self.new_desc = value

    @rx.event
    def set_new_duration(self, value: str):
        self.new_duration = value

    @rx.event
    def set_new_price(self, value: str):
        self.new_price = value

    @rx.event
    def set_new_category(self, value: str):
        self.new_category = value

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
            new_id = len(self.services) + 1
            filename = f"service_{new_id}{ext}"
            outfile = os.path.join(upload_dir, filename)
            
            with open(outfile, "wb") as f:
                f.write(upload_data)
                
            self.new_image = f"/uploads/{filename}"
            self.upload_timestamp = int(os.path.getmtime(outfile))
            
        return ServicesState.add_service
