import reflex as rx
from app.states.pipeline_state import PipelineState


def pipeline_form_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.el.h2(
                rx.cond(
                    PipelineState.is_edit_mode, "Edit Pipeline", "Create New Pipeline"
                ),
                class_name="text-xl font-bold text-gray-900 mb-6",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Pipeline Name",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        name="name",
                        default_value=PipelineState.form_name,
                        placeholder="e.g., Data Ingestion Service",
                        required=True,
                        class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Description",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.input(
                        name="description",
                        default_value=PipelineState.form_description,
                        placeholder="What does this pipeline do?",
                        class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Configuration (YAML/JSON)",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.textarea(
                        name="config",
                        default_value=PipelineState.form_config,
                        placeholder="Paste configuration here...",
                        rows=10,
                        class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500 font-mono text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=PipelineState.close_modals,
                        class_name="px-4 py-2 bg-white border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium text-sm mr-3",
                    ),
                    rx.el.button(
                        rx.cond(
                            PipelineState.is_edit_mode,
                            "Save Changes",
                            "Create Pipeline",
                        ),
                        type="submit",
                        class_name="px-4 py-2 bg-violet-600 text-white rounded-lg hover:bg-violet-700 font-medium text-sm",
                    ),
                    class_name="flex justify-end",
                ),
                on_submit=PipelineState.save_pipeline,
            ),
            class_name="bg-white p-6 rounded-xl shadow-xl max-w-lg w-full",
        ),
        open=PipelineState.is_create_open,
        on_open_change=PipelineState.close_modals,
    )
