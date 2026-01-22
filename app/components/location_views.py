import reflex as rx


def location_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "SAN JOSÉ, COSTA RICA",
                    class_name="text-[#D4AF37] tracking-[0.5em] text-xs font-bold mb-4 block",
                ),
                rx.el.h1(
                    "NUNCIATURA",
                    rx.el.span("· ROHRMOSER", class_name="text-gray-500"),
                    class_name="text-5xl md:text-7xl font-black text-white leading-tight mb-8 tracking-tighter",
                ),
                rx.el.p(
                    "Ubicados estratégicamente en el corazón de la zona más exclusiva del oeste. Rodeados de arquitectura moderna y el dinamismo urbano.",
                    class_name="text-gray-400 text-lg max-w-2xl leading-relaxed mb-10",
                ),
                class_name="relative z-10",
            ),
            class_name="max-w-7xl mx-auto px-6 pt-32 pb-20",
        ),
        class_name="bg-[#0A0A0A] border-b border-white/5",
    )


def info_card(icon: str, title: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=24, class_name="text-[#D4AF37] mb-4"),
        rx.el.h3(
            title,
            class_name="text-white font-bold tracking-widest uppercase mb-2 text-sm",
        ),
        rx.el.p(text, class_name="text-gray-400 text-sm leading-relaxed"),
        class_name="p-6 bg-[#111111] border border-white/5 hover:border-[#D4AF37]/30 transition-all",
    )


def location_details() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            "MAPA INTERACTIVO",
                            class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-white font-bold tracking-[0.2em] bg-black/50 px-6 py-3 backdrop-blur-md rounded border border-white/10",
                        ),
                        class_name="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=2074&auto=format&fit=crop')] bg-cover bg-center grayscale opacity-60 hover:opacity-100 transition-all duration-700",
                    ),
                    class_name="w-full h-[500px] bg-[#1A1A1A] rounded-sm relative overflow-hidden border border-white/5 mb-12",
                ),
                rx.el.div(
                    info_card(
                        "github",
                        "PARQUEO",
                        "Contamos con espacios privados para clientes frente al local y convenio con parqueo Torre Rohrmoser.",
                    ),
                    info_card(
                        "map-pin",
                        "DIRECCIÓN",
                        "Bv. Ernesto Rohrmoser, 200m Oeste del Estadio Nacional. Edificio Vistas de Nunciatura, Local 2.",
                    ),
                    info_card(
                        "bus",
                        "ACCESO",
                        "Fácil acceso desde Ruta 27 y General Cañas. A pasos de paradas de autobús y tren urbano.",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
                ),
                class_name="max-w-7xl mx-auto px-6 pb-24",
            )
        ),
        class_name="bg-[#0A0A0A]",
    )
