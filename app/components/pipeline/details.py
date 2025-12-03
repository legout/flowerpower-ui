import reflex as rx
from app.states.pipeline_state import PipelineState, Execution
from app.components.pipeline.status_badge import status_badge


def execution_row(exec: Execution) -> rx.Component:
    return rx.el.tr(
        rx.el.td(exec.id, class_name="px-4 py-3 text-sm text-gray-900"),
        rx.el.td(exec.timestamp, class_name="px-4 py-3 text-sm text-gray-500"),
        rx.el.td(status_badge(exec.status), class_name="px-4 py-3"),
        rx.el.td(exec.duration, class_name="px-4 py-3 text-sm text-gray-500"),
        class_name="border-b border-gray-100 hover:bg-gray-50",
    )


def pipeline_details_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.cond(
                PipelineState.selected_pipeline,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                PipelineState.selected_pipeline.name,
                                class_name="text-xl font-bold text-gray-900",
                            ),
                            rx.el.p(
                                PipelineState.selected_pipeline.description,
                                class_name="text-sm text-gray-500 mt-1",
                            ),
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.icon("play", class_name="h-4 w-4 mr-2"),
                                "Run Now",
                                on_click=PipelineState.run_pipeline_mock,
                                class_name="flex items-center px-3 py-1.5 bg-violet-600 text-white text-sm font-medium rounded-lg hover:bg-violet-700 transition-colors",
                            ),
                            class_name="flex gap-2",
                        ),
                        class_name="flex justify-between items-start mb-6",
                    ),
                    rx.tabs.root(
                        rx.tabs.list(
                            rx.tabs.trigger("Overview", value="overview"),
                            rx.tabs.trigger("Configuration", value="config"),
                            rx.tabs.trigger("History", value="history"),
                        ),
                        rx.el.div(
                            rx.tabs.content(
                                rx.el.div(
                                    rx.el.h3(
                                        "Last Execution",
                                        class_name="text-sm font-medium text-gray-900 mb-2",
                                    ),
                                    rx.el.div(
                                        rx.cond(
                                            PipelineState.current_executions.length()
                                            > 0,
                                            rx.el.div(
                                                rx.el.div(
                                                    rx.el.span(
                                                        "Status: ",
                                                        class_name="text-gray-500",
                                                    ),
                                                    status_badge(
                                                        PipelineState.current_executions[
                                                            0
                                                        ].status
                                                    ),
                                                    class_name="flex items-center gap-2 mb-2",
                                                ),
                                                rx.el.div(
                                                    rx.el.span(
                                                        "Logs: ",
                                                        class_name="text-gray-500 block mb-1",
                                                    ),
                                                    rx.el.pre(
                                                        PipelineState.current_executions[
                                                            0
                                                        ].logs,
                                                        class_name="bg-gray-900 text-green-400 p-4 rounded-lg text-xs font-mono overflow-x-auto",
                                                    ),
                                                ),
                                            ),
                                            rx.el.p(
                                                "No execution history available.",
                                                class_name="text-gray-500 italic",
                                            ),
                                        )
                                    ),
                                    class_name="py-4",
                                ),
                                value="overview",
                            ),
                            rx.tabs.content(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.span(
                                            PipelineState.selected_pipeline.config_type,
                                            class_name="text-xs font-mono bg-gray-100 px-2 py-1 rounded text-gray-600",
                                        ),
                                        class_name="mb-2 flex justify-end",
                                    ),
                                    rx.el.pre(
                                        rx.el.code(
                                            PipelineState.selected_pipeline.config_content
                                        ),
                                        class_name="bg-gray-50 border border-gray-200 rounded-lg p-4 text-sm font-mono overflow-auto max-h-96",
                                    ),
                                    class_name="py-4",
                                ),
                                value="config",
                            ),
                            rx.tabs.content(
                                rx.el.div(
                                    rx.el.table(
                                        rx.el.thead(
                                            rx.el.tr(
                                                rx.el.th(
                                                    "ID",
                                                    class_name="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase",
                                                ),
                                                rx.el.th(
                                                    "Time",
                                                    class_name="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase",
                                                ),
                                                rx.el.th(
                                                    "Status",
                                                    class_name="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase",
                                                ),
                                                rx.el.th(
                                                    "Duration",
                                                    class_name="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase",
                                                ),
                                            ),
                                            class_name="bg-gray-50",
                                        ),
                                        rx.el.tbody(
                                            rx.foreach(
                                                PipelineState.current_executions,
                                                execution_row,
                                            )
                                        ),
                                        class_name="min-w-full divide-y divide-gray-200",
                                    ),
                                    class_name="overflow-hidden border border-gray-200 rounded-lg mt-4",
                                ),
                                value="history",
                            ),
                            class_name="mt-4",
                        ),
                        default_value="overview",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Close",
                            on_click=PipelineState.close_modals,
                            class_name="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 font-medium text-sm",
                        ),
                        rx.el.button(
                            "Delete Pipeline",
                            on_click=PipelineState.delete_pipeline(
                                PipelineState.selected_pipeline.id
                            ),
                            class_name="px-4 py-2 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 font-medium text-sm",
                        ),
                        class_name="flex justify-between items-center mt-8 pt-4 border-t border-gray-100",
                    ),
                ),
                rx.el.div("No pipeline selected"),
            ),
            max_width="800px",
            class_name="bg-white p-6 rounded-xl shadow-xl",
        ),
        open=PipelineState.is_details_open,
        on_open_change=PipelineState.close_modals,
    )
