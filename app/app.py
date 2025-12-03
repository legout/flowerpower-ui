import reflex as rx
from app.pages.pipelines_view import pipelines_page
from app.states.execution_state import ExecutionState


def index() -> rx.Component:
    return rx.el.div(rx.script("window.location.href = '/pipelines'"))


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(pipelines_page, route="/pipelines", on_load=ExecutionState.clear_selection)
