import reflex as rx


def service_card(title: str, price: str, desc: str, img: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=img,
                class_name="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-700 transform group-hover:scale-110",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-all duration-500"
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    title,
                    class_name="text-xl font-bold text-white tracking-widest uppercase mb-2",
                ),
                rx.el.span(price, class_name="text-[#D4AF37] font-bold text-lg"),
                class_name="flex justify-between items-start",
            ),
            rx.el.p(desc, class_name="text-gray-500 text-sm mt-3 leading-relaxed"),
            rx.el.button(
                "AÑADIR A RESERVA",
                class_name="mt-6 w-full py-2 border border-white/10 hover:border-[#D4AF37] text-white hover:text-[#D4AF37] text-xs font-bold tracking-widest transition-all duration-300",
            ),
            class_name="p-6 bg-[#1A1A1A] border-t-2 border-transparent group-hover:border-[#D4AF37] transition-all duration-500",
        ),
        class_name="group relative flex flex-col shadow-2xl",
    )


def services_preview() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "NUESTRO MENÚ",
                    class_name="text-[#D4AF37] tracking-[0.3em] text-[0.7rem] font-bold uppercase mb-2 block text-center",
                ),
                rx.el.h2(
                    "SERVICIOS DE AUTOR",
                    class_name="text-4xl md:text-5xl font-black text-white text-center mb-16 tracking-tighter",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                service_card(
                    "Corte Clásico",
                    "₡12,000",
                    "Corte tradicional con terminación a navaja, lavado y peinado con productos premium.",
                    "https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=2074&auto=format&fit=crop",
                ),
                service_card(
                    "Barba Premium",
                    "₡10,000",
                    "Ritual de toallas calientes, perfilado preciso y aceites hidratantes para un acabado impecable.",
                    "https://images.unsplash.com/photo-1621605815841-aa33c5ce7027?q=80&w=2070&auto=format&fit=crop",
                ),
                service_card(
                    "Facial Express",
                    "₡15,000",
                    "Limpieza profunda y exfoliación diseñada para la piel del hombre moderno. Frescura instantánea.",
                    "https://images.unsplash.com/photo-1512690118275-303966697219?q=80&w=2070&auto=format&fit=crop",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            rx.el.div(
                rx.el.a(
                    "VER TODOS LOS SERVICIOS",
                    href="#",
                    class_name="text-[#D4AF37] font-bold text-sm tracking-[0.2em] border-b border-[#D4AF37]/30 hover:border-[#D4AF37] transition-all pb-1",
                ),
                class_name="mt-16 text-center",
            ),
            class_name="max-w-7xl mx-auto px-6 py-24",
        ),
        id="servicios",
        class_name="bg-[#0A0A0A]",
    )
