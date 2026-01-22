import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "GENTS",
                            class_name="text-3xl font-bold tracking-[0.2em] text-white",
                        ),
                        rx.el.span(
                            "BARBERSHOP",
                            class_name="text-[0.8rem] block tracking-[0.4em] text-[#D4AF37] -mt-1 font-semibold",
                        ),
                        class_name="flex flex-col mb-6",
                    ),
                    rx.el.p(
                        "Definiendo el estilo del hombre moderno en San José desde una perspectiva de exclusividad y maestría.",
                        class_name="text-gray-500 max-w-xs mb-8 leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("facebook", size=20),
                            href="#",
                            class_name="text-white hover:text-[#D4AF37] transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("instagram", size=20),
                            href="#",
                            class_name="text-white hover:text-[#D4AF37] transition-colors",
                        ),
                        class_name="flex gap-6",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4(
                        "CONTACTO",
                        class_name="text-white font-bold tracking-widest text-sm mb-6",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.icon("phone", size=16, class_name="text-[#D4AF37]"),
                            " +506 22XX-XXXX",
                            class_name="text-gray-500 mb-4 flex items-center gap-3",
                        ),
                        rx.el.li(
                            rx.icon("mail", size=16, class_name="text-[#D4AF37]"),
                            " info@gentsbarbershop.cr",
                            class_name="text-gray-500 mb-4 flex items-center gap-3",
                        ),
                        rx.el.li(
                            rx.icon("map-pin", size=16, class_name="text-[#D4AF37]"),
                            " Bv. Ernesto Rohrmoser, Nunciatura",
                            class_name="text-gray-500 mb-4 flex items-center gap-3",
                        ),
                        class_name="text-sm font-medium",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4(
                        "HORARIO",
                        class_name="text-white font-bold tracking-widest text-sm mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "Lunes - Viernes", class_name="text-gray-300 block"
                            ),
                            rx.el.span(
                                "10:00 AM - 8:00 PM", class_name="text-gray-500 text-xs"
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.span("Sábados", class_name="text-gray-300 block"),
                            rx.el.span(
                                "9:00 AM - 7:00 PM", class_name="text-gray-500 text-xs"
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.span("Domingos", class_name="text-gray-300 block"),
                            rx.el.span("Cerrado", class_name="text-gray-500 text-xs"),
                        ),
                        class_name="text-sm font-medium",
                    ),
                    class_name="col-span-1",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-16",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 GENTS BARBERSHOP. TODOS LOS DERECHOS RESERVADOS.",
                    class_name="text-[10px] tracking-[0.2em] text-gray-600 font-bold",
                ),
                class_name="border-t border-white/5 mt-20 pt-8 text-center",
            ),
            class_name="max-w-7xl mx-auto px-6 py-20",
        ),
        class_name="bg-[#0A0A0A] border-t border-white/5",
    )
