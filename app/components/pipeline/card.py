import reflex as rx
from app.states.execution_state import ExecutionState, Pipeline
from app.components.pipeline.status_badge import status_badge


def pipeline_card(pipeline: Pipeline) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    pipeline.name, class_name="text-base font-semibold text-gray-900"
                ),
                status_badge(pipeline.status),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.el.p(
                pipeline.description,
                class_name="text-sm text-gray-500 mb-4 line-clamp-2 h-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("clock", class_name="h-4 w-4 text-gray-400 mr-2"),
                    rx.el.span(
                        "Last run: ",
                        pipeline.last_run,
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center mb-1",
                ),
                rx.el.div(
                    rx.icon("file-text", class_name="h-4 w-4 text-gray-400 mr-2"),
                    rx.el.span(
                        "Config: ",
                        pipeline.config_type,
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center",
                ),
                class_name="mb-4 pt-4 border-t border-gray-100",
            ),
            rx.el.div(
                rx.el.button(
                    "View Details",
                    on_click=lambda: ExecutionState.select_pipeline(pipeline.id),
                    class_name="text-sm font-medium text-violet-600 hover:text-violet-700 transition-colors cursor-pointer",
                ),
                rx.el.button(
                    "Edit",
                    class_name="text-sm font-medium text-gray-500 hover:text-gray-700 transition-colors cursor-pointer",
                ),
                class_name="flex justify-between items-center",
            ),
            class_name="h-full flex flex-col justify-between",
        ),
        class_name="bg-white p-5 rounded-xl border border-gray-200 shadow-sm hover:border-violet-200 transition-all h-full",
    )
