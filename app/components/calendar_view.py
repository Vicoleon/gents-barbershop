import reflex as rx
from app.states.admin_state import AdminState
from app.states.barbers_state import BarbersState
from datetime import datetime



def reservation_block(res: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(res["time"], class_name="text-[10px] font-bold opacity-80"),
        rx.el.div(res["client_name"], class_name="text-xs font-bold truncate"),
        rx.el.div(res["service_name"], class_name="text-[10px] truncate opacity-80"),
        class_name=res["full_class"].to(str),
        style={
            "top": res["top_position"],
            "height": "60px", # logical height for approx 45-60 mins
            "left": "4px",
            "right": "4px",
        },
        on_click=lambda: AdminState.start_edit_reservation(res),
    )

def day_view() -> rx.Component:
    return rx.el.div(
        # Date Header
        rx.el.div(
            rx.el.h2(
                AdminState.selected_date,
                class_name="text-xl font-bold text-[#D4AF37] px-6 py-4"
            ),
            class_name="border-b border-white/10 flex justify-center items-center"
        ),
        # Header (Barbers)
        rx.el.div(
            rx.el.div("", class_name="w-16 flex-shrink-0"), # Time col placeholder
            rx.foreach(
                BarbersState.barbers,
                lambda b: rx.el.div(
                    rx.el.div(
                        rx.el.img(src=b["image"], class_name="w-8 h-8 rounded-full object-cover mr-2"),
                        rx.el.span(b["name"], class_name="font-bold text-sm text-white"),
                        class_name="flex items-center justify-center p-4 border-b border-white/10"
                    ),
                    class_name="flex-1 min-w-[150px]",
                )
            ),
            class_name="flex border-b border-white/10 sticky top-0 bg-[#0A0A0A] z-20"
        ),
        # Body (Time slots + Grid)
        rx.el.div(
            # Time Axis
            rx.el.div(
                rx.foreach(
                    list(range(8, 21)), # 8 AM to 8 PM
                    lambda h: rx.el.div(
                        rx.cond(h <= 12, h.to_string(), (h - 12).to_string()) + " " + rx.cond(h < 12, "AM", "PM"), 
                        class_name="h-[80px] text-[10px] text-gray-500 text-right pr-2 -mt-2 border-r border-white/10"
                    )
                ),
                class_name="w-16 flex-shrink-0 py-4"
            ),
            # Barber Columns
            rx.foreach(
                BarbersState.barbers,
                lambda b: rx.el.div(
                    # Grid lines matched to time axis height (80px per hour)
                    rx.foreach(
                        list(range(8, 21)),
                        lambda _: rx.el.div(class_name="h-[80px] border-b border-white/5")
                    ),
                    # Reservations Overlay
                    rx.el.div(
                        rx.foreach(
                            AdminState.day_reservations[b["name"]],
                            reservation_block
                        ),
                        class_name="absolute inset-0 top-4" # top-4 to check alignment with time labels
                    ),
                    class_name="flex-1 min-w-[150px] relative border-r border-white/5"
                )
            ),
            class_name="flex relative overflow-y-auto max-h-[600px]"
        ),
        class_name="bg-[#111111] rounded-xl border border-white/5 overflow-hidden flex flex-col"
    )

def week_view_item(date_str: str) -> rx.Component:
    count = AdminState.heatmap_data[date_str]
    
    return rx.el.button(
        rx.el.div(
            date_str, 
            class_name="text-[10px] font-mono mb-2 opacity-80"
        ),
        rx.el.div(
            rx.cond(
                count > 0,
                count.to_string() + " reservas",
                "Libre"
            ),
            class_name="text-sm font-bold"
        ),
        class_name=AdminState.heatmap_metadata[date_str].to(str),
        on_click=lambda: [AdminState.set_date(date_str), AdminState.set_view_mode("day")]
    )

def week_view() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Mapa de Demanda Semanal", class_name="text-white font-bold mb-4"),
        rx.el.div(
            rx.foreach(
                AdminState.week_dates,
                week_view_item
            ),
            class_name="flex gap-2 overflow-x-auto pb-4"
        ),
        class_name="mb-8"
    )


def calendar_view() -> rx.Component:
    return rx.el.div(
        # View Switcher
        rx.el.div(
            rx.el.button(
                rx.icon("list", size=18, class_name="mr-2"),
                "Lista",
                class_name=rx.cond(AdminState.view_mode == "list", "flex items-center px-4 py-2 rounded-l-lg border border-white/10 bg-[#D4AF37] text-black", "flex items-center px-4 py-2 rounded-l-lg border border-white/10 bg-[#111111] text-white hover:bg-white/5"),
                on_click=lambda: AdminState.set_view_mode("list")
            ),
            rx.el.button(
                rx.icon("layout-grid", size=18, class_name="mr-2"),
                "Semana",
                class_name=rx.cond(AdminState.view_mode == "week", "flex items-center px-4 py-2 border-y border-white/10 bg-[#D4AF37] text-black", "flex items-center px-4 py-2 border-y border-white/10 bg-[#111111] text-white hover:bg-white/5"),
                on_click=lambda: AdminState.set_view_mode("week")
            ),
            rx.el.button(
                rx.icon("calendar", size=18, class_name="mr-2"),
                "Día (Agenda)",
                class_name=rx.cond(AdminState.view_mode == "day", "flex items-center px-4 py-2 rounded-r-lg border border-white/10 bg-[#D4AF37] text-black", "flex items-center px-4 py-2 rounded-r-lg border border-white/10 bg-[#111111] text-white hover:bg-white/5"),
                on_click=lambda: AdminState.set_view_mode("day")
            ),
            class_name="flex mb-6"
        ),
        
        # Content Areas
        rx.cond(
            AdminState.view_mode == "week",
            week_view(),
        ),
        rx.cond(
            AdminState.view_mode == "day",
            day_view(),
        ),
    )
