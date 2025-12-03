import reflex as rx
from app.states.execution_state import ExecutionState, ExecutionLog
from app.components.pipeline.status_badge import status_badge


def control_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    rx.cond(
                        ExecutionState.pipeline_id,
                        ExecutionState.pipeline_id,
                        "Loading...",
                    ),
                    class_name="text-2xl font-bold text-gray-900 sm:truncate",
                ),
                rx.el.div(status_badge(ExecutionState.status), class_name="ml-4"),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("play", class_name="mr-2 h-4 w-4"),
                    "Start Run",
                    on_click=ExecutionState.start_pipeline,
                    disabled=ExecutionState.is_running,
                    class_name=rx.cond(
                        ExecutionState.is_running,
                        "inline-flex items-center px-4 py-2 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-gray-400 cursor-not-allowed",
                        "inline-flex items-center px-4 py-2 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-violet-600 hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500",
                    ),
                ),
                rx.el.button(
                    rx.icon("square", class_name="mr-2 h-4 w-4"),
                    "Stop",
                    on_click=ExecutionState.stop_pipeline,
                    disabled=~ExecutionState.is_running,
                    class_name=rx.cond(
                        ~ExecutionState.is_running,
                        "ml-3 inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg shadow-sm text-sm font-medium text-gray-400 bg-white cursor-not-allowed",
                        "ml-3 inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500",
                    ),
                ),
                class_name="mt-4 flex md:mt-0 md:ml-4",
            ),
            class_name="flex flex-col md:flex-row md:items-center md:justify-between",
        ),
        class_name="bg-white border-b border-gray-200 px-4 py-4 sm:px-6 rounded-t-xl mb-6",
    )


def log_entry(log: ExecutionLog) -> rx.Component:
    return rx.el.div(
        rx.el.span(log.timestamp, class_name="text-gray-500 w-20 shrink-0"),
        rx.el.span(
            log.level,
            class_name=rx.match(
                log.level,
                ("INFO", "text-blue-400 w-16 shrink-0 font-semibold"),
                ("WARNING", "text-yellow-400 w-16 shrink-0 font-semibold"),
                ("ERROR", "text-red-400 w-16 shrink-0 font-semibold"),
                "text-gray-400 w-16 shrink-0 font-semibold",
            ),
        ),
        rx.el.span(log.message, class_name="text-gray-300 flex-1"),
        class_name="flex gap-4 text-xs font-mono border-b border-gray-800/50 py-1 hover:bg-gray-800/50 px-2",
    )


def log_viewer() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Live Logs", class_name="text-sm font-semibold text-gray-900"),
            rx.el.button(
                "Clear", class_name="text-xs text-gray-500 hover:text-gray-700"
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.el.div(
            rx.foreach(ExecutionState.recent_logs, log_entry),
            rx.cond(
                ExecutionState.recent_logs.length() == 0,
                rx.el.div(
                    "No logs available. Start a pipeline run to see output.",
                    class_name="text-gray-500 text-sm text-center py-8 italic",
                ),
            ),
            class_name="bg-gray-900 rounded-lg h-64 overflow-y-auto p-4 border border-gray-800 shadow-inner",
        ),
        class_name="mb-6",
    )


def settings_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Configuration", class_name="text-lg font-semibold text-gray-900 mb-4"
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Executor Type",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.select(
                        rx.el.option("ThreadPoolExecutor", value="threadpool"),
                        rx.el.option("ProcessPoolExecutor", value="processpool"),
                        rx.el.option("Celery", value="celery"),
                        rx.el.option("Kubernetes", value="k8s"),
                        name="executor_type",
                        default_value=ExecutionState.executor_type,
                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm p-2 border",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Max Workers",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        type="number",
                        name="max_workers",
                        default_value=ExecutionState.max_workers.to_string(),
                        min="1",
                        max="16",
                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm p-2 border",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Timeout (seconds)",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        type="number",
                        name="timeout",
                        default_value=ExecutionState.timeout_seconds.to_string(),
                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm p-2 border",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Retries",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        type="number",
                        name="retries",
                        default_value=ExecutionState.retry_count.to_string(),
                        min="0",
                        max="5",
                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-violet-500 focus:ring-violet-500 sm:text-sm p-2 border",
                    ),
                    class_name="col-span-1",
                ),
                class_name="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2",
            ),
            rx.el.div(
                rx.el.button(
                    "Save Changes",
                    type="submit",
                    class_name="inline-flex justify-center rounded-md border border-transparent bg-violet-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-offset-2",
                ),
                class_name="mt-6 flex justify-end",
            ),
            on_submit=ExecutionState.update_settings,
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )
