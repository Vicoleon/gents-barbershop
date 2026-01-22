import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.services_preview import services_preview
from app.components.why_us import why_us
from app.components.footer import footer
from app.states.services_state import ServicesState, Service
from app.states.barbers_state import BarbersState, Barber
from app.components.booking import booking_modal
from app.components.location_views import location_hero, location_details
from app.states.booking_state import BookingState
from app.pages.admin import (
    login_page,
    admin_dashboard,
    admin_analytics,
    admin_services,
    admin_barbers,
)
from app.states.admin_state import AdminState


def service_item_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=service["image"] + rx.cond(ServicesState.upload_timestamp > 0, "?" + ServicesState.upload_timestamp.to_string(), ""),
                class_name="w-full h-48 object-cover grayscale group-hover:grayscale-0 transition-all duration-700",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-black/40 group-hover:bg-black/10 transition-all"
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    service["name"],
                    class_name="text-lg font-bold text-white tracking-widest uppercase",
                ),
                rx.el.span(service["price"], class_name="text-[#D4AF37] font-bold"),
                class_name="flex justify-between items-center mb-2",
            ),
            rx.el.p(
                service["description"],
                class_name="text-gray-500 text-xs leading-relaxed mb-4",
            ),
            rx.el.div(
                rx.el.span(
                    rx.icon("clock", size=12),
                    service["duration"],
                    class_name="flex items-center gap-1 text-[10px] text-gray-400 font-bold tracking-widest uppercase",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                "RESERVAR ESTE SERVICIO",
                on_click=lambda: BookingState.start_booking_with_service(service),
                class_name="w-full py-3 bg-transparent border border-[#D4AF37]/50 text-[#D4AF37] hover:bg-[#D4AF37] hover:text-black transition-all text-[10px] font-black tracking-[0.2em]",
            ),
            class_name="p-6 bg-[#111111]",
        ),
        class_name="group border border-white/5 hover:border-[#D4AF37]/30 transition-all shadow-xl",
    )


def services_page() -> rx.Component:
    return rx.el.main(
        navbar(),
        booking_modal(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "CATÁLOGO DE EXPERIENCIAS",
                        class_name="text-[#D4AF37] tracking-[0.4em] text-xs font-bold block mb-4",
                    ),
                    rx.el.h1(
                        "SERVICIOS & PRECIOS",
                        class_name="text-5xl md:text-7xl font-black text-white tracking-tighter mb-8",
                    ),
                    class_name="text-center mb-20 pt-32",
                ),
                rx.el.div(
                    rx.foreach(
                        ServicesState.categories,
                        lambda cat: rx.el.button(
                            cat,
                            on_click=lambda: ServicesState.set_filter(cat),
                            class_name=rx.cond(
                                ServicesState.selected_category == cat,
                                "px-6 py-2 bg-[#D4AF37] text-black font-bold text-xs tracking-widest rounded-full transition-all",
                                "px-6 py-2 bg-white/5 text-gray-400 hover:text-white font-bold text-xs tracking-widest rounded-full transition-all",
                            ),
                        ),
                    ),
                    class_name="flex flex-wrap justify-center gap-4 mb-16",
                ),
                rx.el.div(
                    rx.foreach(ServicesState.filtered_services, service_item_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
                ),
                class_name="max-w-7xl mx-auto px-6 py-20",
            ),
            class_name="bg-[#0A0A0A] min-h-screen",
        ),
        footer(),
        class_name="bg-[#0A0A0A] font-['Inter']",
    )


def barber_card(barber: Barber) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=barber["image"] + rx.cond(BarbersState.upload_timestamp > 0, "?" + BarbersState.upload_timestamp.to_string(), ""),
                class_name="w-full h-[400px] object-cover grayscale group-hover:grayscale-0 transition-all duration-700",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        barber["name"],
                        class_name="text-2xl font-black text-white tracking-tighter mb-1",
                    ),
                    rx.el.span(
                        barber["specialty"],
                        class_name="text-[#D4AF37] text-xs font-bold tracking-widest uppercase",
                    ),
                    class_name="absolute bottom-8 left-8",
                ),
                class_name="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-90",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "EXPERIENCIA",
                    class_name="text-[10px] text-gray-500 font-bold tracking-widest mb-1 block",
                ),
                rx.el.span(
                    barber["experience"], class_name="text-white font-bold text-sm"
                ),
                class_name="mb-4",
            ),
            rx.el.p(
                barber["bio"], class_name="text-gray-400 text-sm leading-relaxed mb-8"
            ),
            rx.el.button(
                "AGENDAR CITA",
                on_click=lambda: BookingState.start_booking_with_barber(barber),
                class_name="w-full py-4 bg-[#D4AF37] text-black font-black text-[10px] tracking-[0.2em] hover:bg-white transition-all",
            ),
            class_name="p-8 bg-[#111111]",
        ),
        class_name="group border border-white/5 hover:border-[#D4AF37]/30 transition-all",
    )


def barbers_page() -> rx.Component:
    return rx.el.main(
        navbar(),
        booking_modal(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "MAESTROS DEL DETALLE",
                        class_name="text-[#D4AF37] tracking-[0.4em] text-xs font-bold block mb-4",
                    ),
                    rx.el.h1(
                        "NUESTRO EQUIPO",
                        class_name="text-5xl md:text-7xl font-black text-white tracking-tighter mb-8",
                    ),
                    rx.el.p(
                        "Profesionales apasionados por elevar tu imagen al siguiente nivel.",
                        class_name="text-gray-500 max-w-xl mx-auto",
                    ),
                    class_name="text-center mb-20 pt-32",
                ),
                rx.el.div(
                    rx.foreach(BarbersState.barbers, barber_card),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-6 py-20",
            ),
            class_name="bg-[#0A0A0A] min-h-screen",
        ),
        footer(),
        class_name="bg-[#0A0A0A] font-['Inter']",
    )


def location_page() -> rx.Component:
    return rx.el.main(
        navbar(),
        booking_modal(),
        location_hero(),
        location_details(),
        footer(),
        class_name="bg-[#0A0A0A] font-['Inter'] min-h-screen selection:bg-[#D4AF37] selection:text-black",
    )


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        booking_modal(),
        hero(),
        why_us(),
        services_preview(),
        footer(),
        class_name="bg-[#0A0A0A] font-['Inter'] min-h-screen selection:bg-[#D4AF37] selection:text-black",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/", on_load=[ServicesState.on_load, BarbersState.on_load])
app.add_page(services_page, route="/servicios", on_load=ServicesState.on_load)
app.add_page(barbers_page, route="/barberos", on_load=BarbersState.on_load)
app.add_page(location_page, route="/ubicacion")
app.add_page(login_page, route="/admin/login")
app.add_page(admin_dashboard, route="/admin", on_load=AdminState.on_load)
app.add_page(admin_services, route="/admin/servicios", on_load=ServicesState.on_load)
app.add_page(admin_barbers, route="/admin/barberos", on_load=BarbersState.on_load)
app.add_page(
    admin_analytics, route="/admin/analytics", on_load=AdminState.load_analytics
)
