import reflex as rx
from app.states.navigation_state import NavigationState
from app.states.booking_state import BookingState


def nav_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-gray-300 hover:text-[#D4AF37] transition-colors duration-300 font-medium text-sm tracking-widest uppercase",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "GENTS", class_name="text-2xl font-bold tracking-[0.2em] text-white"
                ),
                rx.el.span(
                    "BARBERSHOP",
                    class_name="text-[0.6rem] block tracking-[0.4em] text-[#D4AF37] -mt-1 font-semibold",
                ),
                class_name="flex flex-col cursor-pointer",
            ),
            rx.el.div(
                nav_link("Inicio", "/"),
                nav_link("Servicios", "/servicios"),
                nav_link("Barberos", "/barberos"),
                nav_link("Ubicación", "/#ubicacion"),
                class_name="hidden md:flex items-center gap-10",
            ),
            rx.el.div(
                rx.el.button(
                    "RESERVAR",
                    on_click=BookingState.open_modal,
                    class_name="px-6 py-2 bg-[#C9A227] hover:bg-[#D4AF37] text-black font-bold text-xs tracking-widest transition-all duration-300 rounded-sm shadow-lg transform hover:scale-105",
                ),
                rx.el.button(
                    rx.icon("menu", size=24, class_name="text-white"),
                    on_click=NavigationState.toggle_menu,
                    class_name="md:hidden ml-4",
                ),
                class_name="flex items-center",
            ),
            class_name="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between",
        ),
        rx.cond(
            NavigationState.is_menu_open,
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("x", size=32),
                        on_click=NavigationState.toggle_menu,
                        class_name="absolute top-6 right-6 text-white",
                    ),
                    rx.el.nav(
                        rx.el.a(
                            "INICIO",
                            href="/",
                            on_click=NavigationState.close_menu,
                            class_name="text-2xl font-bold text-white hover:text-[#D4AF37]",
                        ),
                        rx.el.a(
                            "SERVICIOS",
                            href="/servicios",
                            on_click=NavigationState.close_menu,
                            class_name="text-2xl font-bold text-white hover:text-[#D4AF37]",
                        ),
                        rx.el.a(
                            "BARBEROS",
                            href="/barberos",
                            on_click=NavigationState.close_menu,
                            class_name="text-2xl font-bold text-white hover:text-[#D4AF37]",
                        ),
                        rx.el.a(
                            "UBICACIÓN",
                            href="/#ubicacion",
                            on_click=NavigationState.close_menu,
                            class_name="text-2xl font-bold text-white hover:text-[#D4AF37]",
                        ),
                        class_name="flex flex-col items-center gap-8 mt-20",
                    ),
                    class_name="bg-[#0A0A0A] w-full h-full p-10 relative",
                ),
                class_name="fixed inset-0 z-[100] md:hidden",
            ),
        ),
        class_name="fixed top-0 left-0 right-0 z-50 bg-[#0A0A0A]/90 backdrop-blur-md border-b border-white/5",
    )
