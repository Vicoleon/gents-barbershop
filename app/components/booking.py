import reflex as rx
from app.states.booking_state import BookingState
from app.states.barbers_state import BarbersState
from app.states.services_state import ServicesState


def step_indicator() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            rx.Var.range(1, 6),
            lambda i: rx.el.div(
                class_name=rx.cond(
                    BookingState.current_step >= i,
                    "h-1 w-full bg-[#D4AF37] transition-all duration-300",
                    "h-1 w-full bg-white/10 transition-all duration-300",
                )
            ),
        ),
        class_name="flex gap-2 mb-8",
    )


def barber_selection_step() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            BarbersState.barbers,
            lambda barber: rx.el.div(
                rx.el.img(
                    src=barber["image"] + rx.cond(BarbersState.upload_timestamp > 0, "?" + BarbersState.upload_timestamp.to_string(), ""),
                    class_name="w-16 h-16 rounded-full object-cover border-2 border-[#D4AF37]/50",
                ),
                rx.el.div(
                    rx.el.h4(barber["name"], class_name="text-white font-bold"),
                    rx.el.p(barber["specialty"], class_name="text-xs text-gray-400"),
                    class_name="flex-1",
                ),
                rx.icon("chevron-right", class_name="text-[#D4AF37]"),
                class_name=rx.cond(
                    BookingState.selected_barber["name"] == barber["name"],
                    "flex items-center gap-4 p-4 rounded-lg bg-[#D4AF37]/10 border border-[#D4AF37] cursor-pointer transition-all",
                    "flex items-center gap-4 p-4 rounded-lg bg-white/5 border border-transparent hover:bg-white/10 cursor-pointer transition-all",
                ),
                on_click=lambda: BookingState.select_barber(barber),
            ),
        ),
        class_name="grid grid-cols-1 gap-3 max-h-[60vh] overflow-y-auto",
    )


def service_selection_step() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            ServicesState.services,
            lambda service: rx.el.div(
                rx.el.div(
                    rx.el.img(
                        src=service["image"],
                        class_name="w-12 h-12 rounded object-cover border border-white/10 mr-4",
                    ),
                    rx.el.div(
                        rx.el.h4(service["name"], class_name="text-white font-bold"),
                        rx.el.p(service["duration"], class_name="text-xs text-[#D4AF37]"),
                        class_name="flex-1",
                    ),
                    class_name="flex items-center"
                ),
                rx.el.span(service["price"], class_name="text-white font-mono"),
                class_name=rx.cond(
                    BookingState.selected_service["name"] == service["name"],
                    "flex items-center justify-between p-4 rounded-lg bg-[#D4AF37]/10 border border-[#D4AF37] cursor-pointer transition-all",
                    "flex items-center justify-between p-4 rounded-lg bg-white/5 border border-transparent hover:bg-white/10 cursor-pointer transition-all",
                ),
                on_click=lambda: BookingState.select_service(service),
            ),
        ),
        class_name="grid grid-cols-1 gap-3 max-h-[60vh] overflow-y-auto",
    )


def datetime_selection_step() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "FECHA",
                class_name="text-xs font-bold text-gray-500 mb-2 block tracking-widest",
            ),
            rx.el.input(
                type="date",
                on_change=BookingState.set_date,
                class_name="w-full bg-[#111111] border border-white/20 rounded-lg p-3 text-white focus:border-[#D4AF37] outline-none transition-colors",
                value=BookingState.selected_date,
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.label(
                "HORA DISPONIBLE",
                class_name="text-xs font-bold text-gray-500 mb-2 block tracking-widest",
            ),
            rx.el.div(
                rx.foreach(
                    BookingState.time_slots,
                    lambda time: rx.el.button(
                        time,
                        on_click=lambda: BookingState.set_time(time),
                        class_name=rx.cond(
                            BookingState.selected_time == time,
                            "py-2 px-1 bg-[#D4AF37] text-black text-sm font-bold rounded border border-[#D4AF37] transition-all",
                            "py-2 px-1 bg-white/5 text-gray-300 text-sm font-medium rounded border border-transparent hover:bg-white/10 hover:border-[#D4AF37]/30 transition-all",
                        ),
                    ),
                ),
                class_name="grid grid-cols-3 sm:grid-cols-4 gap-2 max-h-[40vh] overflow-y-auto pr-2",
            ),
        ),
        rx.el.button(
            "CONTINUAR",
            on_click=BookingState.next_step,
            disabled=~BookingState.can_progress_from_date,
            class_name="w-full mt-6 py-4 bg-[#D4AF37] disabled:bg-gray-700 disabled:text-gray-500 text-black font-bold tracking-widest rounded-lg hover:bg-white transition-all",
        ),
        class_name="flex flex-col",
    )


def client_info_step() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "NOMBRE COMPLETO",
                class_name="text-xs font-bold text-gray-500 mb-2 block tracking-widest",
            ),
            rx.el.input(
                placeholder="Ej. Juan Pérez",
                on_change=BookingState.set_client_name,
                class_name="w-full bg-[#111111] border border-white/20 rounded-lg p-4 text-white focus:border-[#D4AF37] outline-none transition-colors mb-6",
                value=BookingState.client_name,
            ),
        ),
        rx.el.div(
            rx.el.label(
                "TELÉFONO / WHATSAPP",
                class_name="text-xs font-bold text-gray-500 mb-2 block tracking-widest",
            ),
            rx.el.input(
                placeholder="Ej. 8888-8888",
                on_change=BookingState.set_client_phone,
                class_name="w-full bg-[#111111] border border-white/20 rounded-lg p-4 text-white focus:border-[#D4AF37] outline-none transition-colors",
                value=BookingState.client_phone,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "CONTINUAR",
            on_click=BookingState.next_step,
            disabled=~BookingState.can_progress_from_client_info,
            class_name="w-full mt-2 py-4 bg-[#D4AF37] disabled:bg-gray-700 disabled:text-gray-500 text-black font-bold tracking-widest rounded-lg hover:bg-white transition-all",
        ),
        class_name="flex flex-col",
    )


def confirmation_step() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "CLIENTE",
                    class_name="text-xs text-gray-500 tracking-widest block mb-1",
                ),
                rx.el.h3(
                    BookingState.client_name, class_name="text-lg font-bold text-white"
                ),
                rx.el.p(
                    BookingState.client_phone, class_name="text-sm text-gray-400 mb-4"
                ),
                class_name="border-b border-white/10 pb-4 mb-4",
            ),
            rx.el.div(
                rx.el.span(
                    "BARBERO & SERVICIO",
                    class_name="text-xs text-gray-500 tracking-widest block mb-1",
                ),
                rx.el.h3(
                    BookingState.selected_barber["name"],
                    class_name="text-lg font-bold text-white",
                ),
                rx.el.div(
                    rx.el.span(
                        BookingState.selected_service["name"], class_name="text-white"
                    ),
                    rx.el.span(" • ", class_name="text-gray-500"),
                    rx.el.span(
                        BookingState.selected_service["price"],
                        class_name="text-[#D4AF37] font-mono",
                    ),
                    class_name="text-sm",
                ),
                class_name="border-b border-white/10 pb-4 mb-4",
            ),
            rx.el.div(
                rx.el.span(
                    "FECHA & HORA",
                    class_name="text-xs text-gray-500 tracking-widest block mb-1",
                ),
                rx.el.h3(
                    f"{BookingState.selected_date} @ {BookingState.selected_time}",
                    class_name="text-xl font-bold text-white",
                ),
                class_name="mb-6",
            ),
            class_name="bg-white/5 p-6 rounded-lg mb-6",
        ),
        rx.el.button(
            "CONFIRMAR RESERVA",
            on_click=BookingState.confirm_booking,
            class_name="w-full py-4 bg-[#D4AF37] text-black font-bold tracking-widest rounded-lg hover:bg-white transition-all",
        ),
    )


def success_step() -> rx.Component:
    return rx.el.div(
        rx.icon(
            "lamp_wall_down", size=64, class_name="text-[#D4AF37] mb-6 animate-bounce"
        ),
        rx.el.h2(
            "¡RESERVA CONFIRMADA!", class_name="text-2xl font-black text-white mb-2"
        ),
        rx.el.div(
            rx.el.span(
                "REFERENCIA:",
                class_name="text-xs text-gray-500 font-bold tracking-widest",
            ),
            rx.el.p(
                BookingState.booking_reference,
                class_name="text-[#D4AF37] font-mono text-xl font-bold",
            ),
            class_name="bg-white/5 px-6 py-3 rounded border border-dashed border-[#D4AF37]/50 mb-6 text-center",
        ),
        rx.el.p(
            "Tu cita ha quedado registrada exitosamente. Te esperamos en Gents.",
            class_name="text-gray-400 text-center mb-8",
        ),
        rx.el.button(
            "CERRAR",
            on_click=BookingState.close_modal,
            class_name="w-full py-4 bg-white/10 text-white font-bold tracking-widest rounded-lg hover:bg-white/20 transition-all",
        ),
        class_name="flex flex-col items-center py-10",
    )


def booking_modal() -> rx.Component:
    return rx.cond(
        BookingState.is_open,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            BookingState.step_title,
                            class_name="text-lg font-bold text-[#D4AF37] tracking-widest",
                        ),
                        rx.el.button(
                            rx.icon(
                                "x",
                                size=24,
                                class_name="text-gray-400 hover:text-white transition-colors",
                            ),
                            on_click=BookingState.close_modal,
                        ),
                        class_name="flex justify-between items-center mb-6",
                    ),
                    step_indicator(),
                    rx.match(
                        BookingState.current_step,
                        (1, barber_selection_step()),
                        (2, service_selection_step()),
                        (3, datetime_selection_step()),
                        (4, client_info_step()),
                        (5, confirmation_step()),
                        (6, success_step()),
                        rx.el.div("Error"),
                    ),
                    rx.cond(
                        (BookingState.current_step > 1)
                        & (BookingState.current_step < 6),
                        rx.el.button(
                            "ATRÁS",
                            on_click=BookingState.prev_step,
                            class_name="mt-4 text-xs font-bold text-gray-500 hover:text-white transition-colors tracking-widest",
                        ),
                    ),
                    class_name="bg-[#111111] w-full max-w-md rounded-xl p-8 shadow-2xl border border-white/10 relative overflow-hidden",
                ),
                class_name="fixed inset-0 z-[60] flex items-center justify-center p-4",
            ),
            rx.el.div(
                class_name="fixed inset-0 bg-black/90 backdrop-blur-sm z-[55]",
                on_click=BookingState.close_modal,
            ),
        ),
    )
