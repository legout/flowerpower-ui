import reflex as rx
from app.components.sidebar import sidebar
from app.states.pipeline_state import PipelineState, Pipeline
from app.components.pipeline.status_badge import status_badge
from app.components.pipeline.forms import pipeline_form_dialog
from app.components.pipeline.details import pipeline_details_modal


def pipeline_card(pipeline: Pipeline) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    pipeline.name,
                    on_click=PipelineState.open_details_modal(pipeline),
                    class_name="text-base font-semibold text-gray-900 truncate hover:text-violet-600 text-left",
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
                    rx.icon("clock", class_name="h-3.5 w-3.5 text-gray-400 mr-1.5"),
                    rx.el.span(
                        f"Last run: {pipeline.last_run}",
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center mb-1",
                ),
                rx.el.div(
                    rx.icon("file-code", class_name="h-3.5 w-3.5 text-gray-400 mr-1.5"),
                    rx.el.span(
                        f"Config: {pipeline.config_type}",
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center",
                ),
                class_name="mb-4",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.a(
                "View Details",
                href=f"/pipelines/{pipeline.id}/executions",
                class_name="text-sm font-medium text-violet-600 hover:text-violet-700 hover:underline decoration-2 underline-offset-2",
            ),
            rx.el.button(
                "Edit",
                on_click=PipelineState.open_edit_modal(pipeline),
                class_name="text-sm font-medium text-gray-500 hover:text-gray-700",
            ),
            class_name="flex justify-between items-center pt-4 border-t border-gray-100 mt-auto",
        ),
        class_name="flex flex-col p-5 bg-white rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow duration-200 h-full",
    )


def pipelines_toolbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "search",
                class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
            ),
            rx.el.input(
                placeholder="Search pipelines...",
                on_change=PipelineState.set_search_query,
                class_name="pl-10 pr-4 py-2 w-full md:w-64 bg-white border border-gray-200 rounded-lg text-sm focus:border-violet-500 focus:ring-1 focus:ring-violet-500 outline-none transition-all",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.select(
                rx.el.option("All Statuses", value="All Statuses"),
                rx.el.option("Success", value="Success"),
                rx.el.option("Failed", value="Failed"),
                rx.el.option("Running", value="Running"),
                rx.el.option("Idle", value="Idle"),
                on_change=PipelineState.set_status_filter,
                class_name="pl-3 pr-8 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:border-violet-500 focus:ring-1 focus:ring-violet-500 outline-none cursor-pointer",
            ),
            class_name="flex items-center",
        ),
        class_name="flex flex-col md:flex-row gap-4 mb-8",
    )


def pipelines_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Pipelines", class_name="text-2xl font-bold text-gray-900"
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="h-4 w-4 mr-2"),
                        "New Pipeline",
                        on_click=PipelineState.open_create_modal,
                        class_name="inline-flex items-center px-4 py-2 bg-violet-600 hover:bg-violet-700 text-white text-sm font-medium rounded-lg shadow-sm transition-colors",
                    ),
                    class_name="flex justify-between items-center mb-6",
                ),
                pipelines_toolbar(),
                rx.el.div(
                    rx.foreach(PipelineState.filtered_pipelines, pipeline_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-6 w-full",
                ),
                class_name="max-w-full w-full mx-auto",
            ),
            class_name="flex-1 p-6 md:p-8 bg-gray-50 overflow-y-auto h-screen w-full",
        ),
        pipeline_form_dialog(),
        pipeline_details_modal(),
        class_name="flex h-screen w-full overflow-hidden font-sans",
        on_mount=PipelineState.on_load,
    )
