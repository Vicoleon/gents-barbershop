import reflex as rx
from app.states.admin_state import AdminState
from app.states.services_state import ServicesState
from app.states.barbers_state import BarbersState
from app.components.admin_sidebar import admin_sidebar
from app.models import Reservation


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "GENTS",
                    class_name="text-4xl font-black tracking-widest text-white block text-center mb-2",
                ),
                rx.el.span(
                    "ADMINISTRATION",
                    class_name="text-xs font-bold tracking-[0.5em] text-[#D4AF37] block text-center mb-10",
                ),
                rx.el.div(
                    rx.el.label(
                        "CONTRASEÑA",
                        class_name="text-[10px] font-bold tracking-widest text-gray-500 mb-2 block",
                    ),
                    rx.el.input(
                        type="password",
                        placeholder="••••••••",
                        on_change=AdminState.set_password,
                        class_name="w-full bg-[#111111] border border-white/10 rounded p-4 text-white focus:border-[#D4AF37] outline-none transition-all mb-4",
                    ),
                    rx.cond(
                        AdminState.login_error != "",
                        rx.el.p(
                            AdminState.login_error,
                            class_name="text-red-500 text-xs mb-4 font-bold",
                        ),
                    ),
                    rx.el.button(
                        "INGRESAR",
                        on_click=AdminState.check_login,
                        class_name="w-full py-4 bg-[#D4AF37] text-black font-bold tracking-widest rounded hover:bg-white transition-all",
                    ),
                ),
                class_name="w-full max-w-sm bg-[#0A0A0A] p-8 border border-white/5 rounded-2xl shadow-2xl",
            ),
            class_name="flex items-center justify-center min-h-screen bg-[#050505]",
        )
    )


def status_badge(status: str) -> rx.Component:
    return rx.match(
        status,
        (
            "confirmed",
            rx.el.span(
                "CONFIRMADO",
                class_name="px-2 py-1 bg-green-500/10 text-green-500 text-[10px] font-bold tracking-wider rounded border border-green-500/20",
            ),
        ),
        (
            "pending",
            rx.el.span(
                "PENDIENTE",
                class_name="px-2 py-1 bg-yellow-500/10 text-yellow-500 text-[10px] font-bold tracking-wider rounded border border-yellow-500/20",
            ),
        ),
        (
            "completed",
            rx.el.span(
                "COMPLETADO",
                class_name="px-2 py-1 bg-blue-500/10 text-blue-500 text-[10px] font-bold tracking-wider rounded border border-blue-500/20",
            ),
        ),
        (
            "cancelled",
            rx.el.span(
                "CANCELADO",
                class_name="px-2 py-1 bg-red-500/10 text-red-500 text-[10px] font-bold tracking-wider rounded border border-red-500/20",
            ),
        ),
        rx.el.span(status),
    )


def reservation_row(res: Reservation) -> rx.Component:
    return rx.el.tr(
        rx.el.td(res["time"], class_name="py-4 text-white font-mono font-bold"),
        rx.el.td(
            rx.el.div(res["client_name"], class_name="text-white font-bold"),
            rx.el.div(res["client_phone"], class_name="text-xs text-gray-500"),
            class_name="py-4",
        ),
        rx.el.td(res["barber_name"], class_name="py-4 text-gray-400 text-sm"),
        rx.el.td(
            rx.el.div(res["service_name"], class_name="text-gray-300 text-sm"),
            rx.el.div(
                res["service_price"], class_name="text-[#D4AF37] text-xs font-mono"
            ),
            class_name="py-4",
        ),
        rx.el.td(status_badge(res["status"]), class_name="py-4"),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("check", size=16),
                    on_click=lambda: AdminState.update_status(res["id"], "completed"),
                    class_name="p-2 hover:bg-green-500/20 text-green-500 rounded transition-colors",
                    title="Marcar completado",
                ),
                rx.el.button(
                    rx.icon("x", size=16),
                    on_click=lambda: AdminState.update_status(res["id"], "cancelled"),
                    class_name="p-2 hover:bg-red-500/20 text-red-500 rounded transition-colors",
                    title="Cancelar",
                ),
                class_name="flex gap-2",
            ),
            class_name="py-4",
        ),
        class_name="border-b border-white/5 hover:bg-white/5 transition-colors",
    )


def admin_dashboard() -> rx.Component:
    return rx.el.div(
        admin_sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1("Dashboard", class_name="text-3xl font-bold text-white mb-8"),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "FECHA",
                            class_name="text-[10px] font-bold tracking-widest text-gray-500 mb-2 block",
                        ),
                        rx.el.input(
                            type="date",
                            on_change=AdminState.set_date,
                            class_name="bg-[#111111] border border-white/10 rounded p-2 text-white outline-none focus:border-[#D4AF37]",
                            default_value=AdminState.selected_date,
                        ),
                    ),
                    class_name="flex justify-between items-end mb-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Agendar Walk-In / Telefónico",
                        class_name="text-white font-bold mb-4",
                    ),
                    rx.el.div(
                        rx.el.input(
                            placeholder="Nombre Cliente",
                            on_change=AdminState.set_walk_in_client,
                            class_name="bg-[#111111] border border-white/10 rounded p-2 text-white text-sm",
                            default_value=AdminState.walk_in_client,
                        ),
                        rx.el.input(
                            placeholder="Teléfono",
                            on_change=AdminState.set_walk_in_phone,
                            class_name="bg-[#111111] border border-white/10 rounded p-2 text-white text-sm",
                            default_value=AdminState.walk_in_phone,
                        ),
                        rx.el.div(
                            rx.el.select(
                                rx.el.option(
                                    "Elegir Servicio", value="", disabled=True
                                ),
                                rx.foreach(
                                    ServicesState.services,
                                    lambda s: rx.el.option(s["name"], value=s["name"]),
                                ),
                                on_change=AdminState.set_walk_in_service,
                                class_name="w-full bg-[#111111] border border-white/10 rounded p-2 text-white text-sm appearance-none pr-8 focus:border-[#D4AF37] outline-none transition-colors",
                                value=AdminState.walk_in_service,
                            ),
                            rx.icon(
                                "chevron-down",
                                size=14,
                                class_name="absolute right-2 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none",
                            ),
                            class_name="relative",
                        ),
                        rx.el.div(
                            rx.el.select(
                                rx.el.option("Elegir Barbero", value="", disabled=True),
                                rx.foreach(
                                    BarbersState.barbers,
                                    lambda b: rx.el.option(b["name"], value=b["name"]),
                                ),
                                on_change=AdminState.set_walk_in_barber,
                                class_name="w-full bg-[#111111] border border-white/10 rounded p-2 text-white text-sm appearance-none pr-8 focus:border-[#D4AF37] outline-none transition-colors",
                                value=AdminState.walk_in_barber,
                            ),
                            rx.icon(
                                "chevron-down",
                                size=14,
                                class_name="absolute right-2 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none",
                            ),
                            class_name="relative",
                        ),
                        rx.el.input(
                            type="datetime-local",
                            on_change=AdminState.set_walk_in_datetime,
                            class_name="bg-[#111111] border border-white/10 rounded p-2 text-white text-sm focus:border-[#D4AF37] outline-none transition-colors",
                            default_value=AdminState.walk_in_datetime,
                        ),
                        rx.el.button(
                            "AGREGAR",
                            on_click=AdminState.add_walk_in,
                            class_name="bg-[#D4AF37] text-black font-bold px-4 py-2 rounded text-sm hover:bg-white transition-colors",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-6 gap-2 items-center",
                    ),
                    class_name="bg-[#111111] p-6 rounded-xl border border-white/5 mb-8 relative",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "HORA",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                                rx.el.th(
                                    "CLIENTE",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                                rx.el.th(
                                    "BARBERO",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                                rx.el.th(
                                    "SERVICIO",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                                rx.el.th(
                                    "ESTADO",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                                rx.el.th(
                                    "ACCIONES",
                                    class_name="text-left text-[10px] font-bold tracking-widest text-gray-500 pb-4",
                                ),
                            ),
                            class_name="border-b border-white/10",
                        ),
                        rx.el.tbody(
                            rx.foreach(AdminState.reservations, reservation_row)
                        ),
                        class_name="w-full",
                    ),
                    class_name="bg-[#111111] rounded-xl border border-white/5 p-8 overflow-x-auto",
                ),
            ),
            class_name="ml-64 p-10 min-h-screen bg-[#0A0A0A]",
        ),
    )
