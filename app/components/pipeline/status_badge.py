import reflex as rx


def status_badge(status: str) -> rx.Component:
    return rx.el.span(
        rx.el.span(
            class_name=rx.match(
                status,
                ("success", "bg-green-400"),
                ("running", "bg-blue-400"),
                ("failed", "bg-red-400"),
                ("warning", "bg-yellow-400"),
                "bg-gray-400",
            ),
            style={
                "height": "0.375rem",
                "width": "0.375rem",
                "borderRadius": "9999px",
                "marginRight": "0.5rem",
                "display": "inline-block",
            },
        ),
        status,
        class_name=rx.match(
            status,
            (
                "success",
                "bg-green-50 text-green-700 border-green-200 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border capitalize",
            ),
            (
                "running",
                "bg-blue-50 text-blue-700 border-blue-200 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border capitalize",
            ),
            (
                "failed",
                "bg-red-50 text-red-700 border-red-200 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border capitalize",
            ),
            (
                "warning",
                "bg-yellow-50 text-yellow-700 border-yellow-200 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border capitalize",
            ),
            "bg-gray-50 text-gray-700 border-gray-200 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border capitalize",
        ),
    )
