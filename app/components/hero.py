import reflex as rx
from app.states.booking_state import BookingState


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "NUNCIATURA · ROHRMOSER",
                    class_name="text-[#D4AF37] tracking-[0.5em] text-xs font-bold mb-4 block animate-fade-in",
                ),
                rx.el.h1(
                    "MÁS QUE UN CORTE,",
                    rx.el.span("UN RITUAL", class_name="block text-[#D4AF37]"),
                    class_name="text-5xl md:text-7xl lg:text-8xl font-black text-white leading-tight mb-6 tracking-tighter",
                ),
                rx.el.p(
                    "Experiencia premium de grooming masculino en el corazón de San José. Diseñamos tu estilo con precisión y elegancia.",
                    class_name="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-10 font-medium leading-relaxed",
                ),
                rx.el.div(
                    rx.el.button(
                        "AGENDAR CITA AHORA",
                        on_click=BookingState.open_modal,
                        class_name="px-10 py-4 bg-transparent border-2 border-[#D4AF37] text-[#D4AF37] hover:bg-[#D4AF37] hover:text-black font-bold tracking-widest transition-all duration-500 rounded-sm",
                    ),
                    class_name="flex justify-center",
                ),
                class_name="relative z-10 text-center px-6",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-[#0A0A0A] z-0"
            ),
            rx.el.div(
                class_name="absolute inset-0 opacity-40 bg-[url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=2070&auto=format&fit=crop')] bg-cover bg-center grayscale"
            ),
            rx.el.div(
                rx.el.div(
                    class_name="w-[2px] h-16 bg-gradient-to-b from-[#D4AF37] to-transparent animate-bounce"
                ),
                class_name="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2",
            ),
            class_name="relative w-full h-screen flex items-center justify-center overflow-hidden",
        )
    )
