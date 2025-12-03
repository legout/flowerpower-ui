import reflex as rx
from app.states.execution_state import ExecutionState


def duration_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Execution Duration Trend",
            class_name="text-sm font-semibold text-gray-700 mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
            rx.recharts.x_axis(data_key="name", font_size=10),
            rx.recharts.y_axis(font_size=10),
            rx.recharts.tooltip(
                cursor=False,
                content_style={
                    "borderRadius": "8px",
                    "border": "none",
                    "boxShadow": "0 4px 6px -1px rgb(0 0 0 / 0.1)",
                },
            ),
            rx.recharts.bar(
                data_key="duration", fill="#8b5cf6", radius=[4, 4, 0, 0], bar_size=30
            ),
            data=ExecutionState.chart_data,
            height=250,
            width="100%",
        ),
        class_name="p-4 bg-white rounded-xl border border-gray-200 shadow-sm h-full",
    )


def status_pie_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Success Rate", class_name="text-sm font-semibold text-gray-700 mb-2"),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    ExecutionState.success_rate.to_string() + "%",
                    class_name="text-3xl font-bold text-gray-900",
                ),
                rx.el.span("Success", class_name="text-sm text-gray-500 ml-2"),
                class_name="flex items-baseline mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-green-500 rounded-full",
                    style={"width": ExecutionState.success_rate.to_string() + "%"},
                ),
                class_name="w-full h-3 bg-gray-100 rounded-full overflow-hidden",
            ),
            rx.el.p(
                "Total Runs: ",
                ExecutionState.total_runs,
                class_name="text-xs text-gray-400 mt-4",
            ),
        ),
        class_name="p-4 bg-white rounded-xl border border-gray-200 shadow-sm h-full",
    )
