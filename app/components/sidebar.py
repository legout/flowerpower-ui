import reflex as rx


def sidebar_item(
    label: str, icon_name: str, href: str, active: bool = False
) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon_name,
            class_name=f"h-5 w-5 {('text-violet-600' if active else 'text-gray-500')}",
        ),
        rx.el.span(
            label,
            class_name=f"ml-3 {('text-violet-700 font-semibold' if active else 'text-gray-700')}",
        ),
        href=href,
        class_name=rx.cond(
            active,
            "flex items-center w-full p-3 rounded-lg bg-violet-50",
            "flex items-center w-full p-3 rounded-lg hover:bg-gray-50 transition-colors",
        ),
    )


def sidebar(active_item: str = "Pipelines") -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.icon("sprout", class_name="h-8 w-8 text-violet-600"),
            rx.el.span(
                "FlowerPower", class_name="ml-2 text-xl font-bold text-gray-900"
            ),
            class_name="flex items-center px-2 py-6 mb-6",
        ),
        rx.el.nav(
            rx.el.div(
                rx.el.p(
                    "PROJECTS",
                    class_name="px-3 mb-2 text-xs font-semibold text-gray-400 uppercase tracking-wider",
                ),
                sidebar_item(
                    "Dashboard",
                    "layout-dashboard",
                    "/",
                    active=active_item == "Dashboard",
                ),
                sidebar_item(
                    "Pipelines",
                    "workflow",
                    "/pipelines",
                    active=active_item == "Pipelines",
                ),
                sidebar_item(
                    "Settings", "settings", "#", active=active_item == "Settings"
                ),
                class_name="space-y-1",
            )
        ),
        class_name="hidden lg:flex flex-col w-64 h-screen bg-white border-r border-gray-200 px-4 sticky top-0",
    )
