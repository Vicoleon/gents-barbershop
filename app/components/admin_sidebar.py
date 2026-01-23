import reflex as rx
from app.states.admin_state import AdminState


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, size=20, class_name="text-gray-400 group-hover:text-[#D4AF37]"),
        rx.el.span(text, class_name="text-gray-300 font-medium group-hover:text-white"),
        href=url,
        class_name="group flex items-center gap-3 p-3 rounded-lg hover:bg-white/5 transition-all",
    )


def admin_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "GENTS", class_name="text-xl font-bold tracking-widest text-white"
                ),
                rx.el.span(
                    "ADMIN",
                    class_name="text-[0.6rem] block tracking-[0.3em] text-[#D4AF37]",
                ),
                class_name="mb-10",
            ),
            rx.el.nav(
                sidebar_item("Reservas", "calendar", "/admin"),
                sidebar_item("Servicios", "scissors", "/admin/servicios"),
                sidebar_item("Barberos", "users", "/admin/barberos"),
                sidebar_item("Analytics", "bar-chart-2", "/admin/analytics"),
                class_name="flex flex-col gap-2",
            ),
            class_name="flex-1",
        ),
        rx.el.button(
            rx.icon("log-out", size=20),
            "Cerrar Sesión",
            on_click=AdminState.logout,
            class_name="flex items-center gap-3 text-red-400 hover:text-red-300 transition-colors text-sm font-medium",
        ),
        class_name="w-64 bg-[#111111] border-r border-white/5 min-h-screen p-6 flex flex-col fixed left-0 top-0",
    )