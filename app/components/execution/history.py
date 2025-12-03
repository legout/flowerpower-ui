import reflex as rx
from app.states.execution_state import ExecutionState, ExecutionRecord
from app.components.pipeline.status_badge import status_badge


def history_row(record: ExecutionRecord) -> rx.Component:
    return rx.el.tr(
        rx.el.td(status_badge(record.status), class_name="px-6 py-4 whitespace-nowrap"),
        rx.el.td(
            record.id,
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            record.start_time,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(f"{record.duration}s"),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                record.triggered_by,
                class_name="px-2 py-1 text-xs font-medium rounded-full bg-gray-100 text-gray-800",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        class_name="hover:bg-gray-50 transition-colors",
    )


def history_table() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Execution History", class_name="text-lg font-semibold text-gray-900 mb-4"
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Run ID",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Start Time",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Duration",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Trigger",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50 border-b border-gray-200",
                ),
                rx.el.tbody(
                    rx.foreach(ExecutionState.execution_history, history_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="overflow-x-auto rounded-xl border border-gray-200 shadow-sm bg-white",
        ),
        class_name="mb-8",
    )
