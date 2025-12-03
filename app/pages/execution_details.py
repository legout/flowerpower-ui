import reflex as rx
from app.states.execution_state import ExecutionState
from app.components.execution.charts import duration_chart, status_pie_chart
from app.components.execution.views import control_panel, log_viewer, settings_form
from app.components.execution.history import history_table


def execution_details_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                "← Back to Pipelines",
                on_click=ExecutionState.clear_selection,
                class_name="text-violet-600 hover:text-violet-800 text-sm font-medium inline-flex items-center gap-1 cursor-pointer bg-transparent border-0 p-0",
            ),
            class_name="mb-6",
        ),
        control_panel(),
        rx.el.div(
            rx.el.div(duration_chart(), class_name="col-span-1 lg:col-span-2 h-full"),
            rx.el.div(status_pie_chart(), class_name="col-span-1 lg:col-span-1 h-full"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6",
        ),
        history_table(),
        rx.el.div(
            rx.el.div(log_viewer(), class_name="col-span-1 lg:col-span-2"),
            rx.el.div(settings_form(), class_name="col-span-1 lg:col-span-1"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="w-full",
    )
