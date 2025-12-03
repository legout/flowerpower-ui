import reflex as rx
from app.components.sidebar import sidebar
from app.states.execution_state import ExecutionState
from app.components.pipeline.card import pipeline_card
from app.pages.execution_details import execution_details_view


def pipelines_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Pipelines", class_name="text-2xl font-bold text-gray-900"),
            rx.el.button(
                "+ New Pipeline",
                class_name="bg-violet-600 hover:bg-violet-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors cursor-pointer",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="h-4 w-4 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                ),
                rx.el.input(
                    placeholder="Search pipelines...",
                    class_name="pl-9 pr-4 py-2 border border-gray-200 rounded-lg text-sm w-64 focus:outline-none focus:border-violet-500 focus:ring-1 focus:ring-violet-500",
                ),
                class_name="relative",
            ),
            rx.el.select(
                rx.el.option("All Statuses", value="all"),
                class_name="ml-4 px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-600 focus:outline-none focus:border-violet-500",
            ),
            class_name="flex items-center mb-8",
        ),
        rx.el.div(
            rx.foreach(ExecutionState.pipelines, pipeline_card),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6",
        ),
    )


def pipelines_page() -> rx.Component:
    return rx.el.div(
        sidebar(active_item="Pipelines"),
        rx.el.main(
            rx.el.div(
                rx.cond(
                    ExecutionState.has_selected_pipeline,
                    execution_details_view(),
                    pipelines_content(),
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="flex-1 bg-gray-50 p-8 min-h-screen overflow-y-auto",
        ),
        class_name="flex h-screen",
    )
