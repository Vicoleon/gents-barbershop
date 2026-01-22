import reflex as rx


def feature_item(icon: str, title: str, desc: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=32, class_name="text-[#D4AF37]"), class_name="mb-6"
        ),
        rx.el.h3(
            title,
            class_name="text-xl font-bold text-white mb-3 tracking-widest uppercase",
        ),
        rx.el.p(desc, class_name="text-gray-400 leading-relaxed font-medium"),
        class_name="p-10 bg-[#1A1A1A] border border-white/5 hover:border-[#D4AF37]/30 transition-all duration-500 rounded-sm",
    )


def why_us() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                feature_item(
                    "map-pin",
                    "Ubicación Premium",
                    "En el corazón de Rohrmoser, frente al Boulevard Nunciatura. Fácil acceso y seguridad.",
                ),
                feature_item(
                    "scissors",
                    "Barberos Expertos",
                    "Nuestro equipo domina las técnicas clásicas y tendencias globales más vanguardistas.",
                ),
                feature_item(
                    "crown",
                    "Experiencia VIP",
                    "Ambiente diseñado para tu relax, con bebidas de cortesía y atención personalizada.",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-1",
            ),
            class_name="max-w-7xl mx-auto px-6 py-12",
        ),
        class_name="bg-[#0A0A0A]",
    )
