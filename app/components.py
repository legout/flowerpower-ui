import htpy as h
from typing import Any, Dict
from flowerpower import FlowerPowerProject


def base_layout(title: str, content: Any) -> str:
    """Base HTML layout with navigation and Datastar setup"""
    return str(
        h.html[
            h.head[
                h.meta(charset="utf-8"),
                h.meta(name="viewport", content="width=device-width, initial-scale=1"),
                h.title[f"{title} - FlowerPower"],
                h.link(
                    href="https://cdn.jsdelivr.net/npm/daisyui@4.10.2/dist/full.css",
                    rel="stylesheet",
                ),
                h.script(src="https://cdn.tailwindcss.com"),
                h.script(src="https://unpkg.com/@starfederation/datastar@latest"),
            ],
            h.body(**{"data-ds-stream": "/datastar/stream"})[
                h.nav(class_="navbar bg-primary text-primary-content px-4 py-2")[
                    h.div(class_="flex-1")[
                        h.a(class_="btn btn-ghost normal-case text-xl", href="/")["FlowerPower"],
                    ],
                    h.ul(class_="menu menu-horizontal px-1")[
                        h.li()[h.a(href="/dashboard")["Dashboard"]],
                        h.li()[h.a(href="/projects")["Projects"]],
                        h.li()[h.a(href="/projects/new")["New Project"]],
                        h.li()[h.a(href="/pipelines")["Pipelines"]],
                        h.li()[h.a(href="/jobs")["Job Queue"]],
                    ],
                ],
                h.div(class_="main-content")[
                    h.div(class_="container mx-auto mt-4")[content],
                ],
            ],
        ]
    )


def project_card(project: FlowerPowerProject) -> Any:
    """Generate a project card component"""
    status = project.get("status", "Unknown")
    status_class = {
        "Active": "success",
        "Inactive": "secondary",
        "Error": "error",
    }.get(status, "secondary")

    # Count pipelines for this project
    pipelines = project.pipeline_manager.pipelines
    pipeline_count = len(pipelines)

    return h.div(class_="w-full md:w-1/2 lg:w-1/3 mb-3 px-2")[
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.h2(class_="card-title")[project["name"]],
                h.p()[project.get("description", "No description")],
                h.div(class_="flex justify-between items-center mb-2")[
                    h.span(class_=f"badge badge-{status_class}")[status],
                    h.span(class_="text-xs text-base-content/60")[
                        f"{pipeline_count} pipeline{'s' if pipeline_count != 1 else ''}"
                    ],
                ],
                h.div(class_="flex justify-between items-center mt-2")[
                    h.div(class_="flex gap-2")[
                        h.a(
                            class_="btn btn-primary btn-sm",
                            href=f"/projects/{project['id']}",
                        )["View"],
                        h.a(
                            class_="btn btn-outline btn-secondary btn-sm",
                            href=f"/projects/{project['id']}/edit",
                        )["Edit"],
                    ],
                    h.div(class_="flex gap-2")[
                        h.a(
                            class_="btn btn-outline btn-info btn-sm",
                            href=f"/projects/{project['id']}/pipelines",
                        )["Pipelines"],
                        h.a(
                            class_="btn btn-outline btn-success btn-sm",
                            href=f"/projects/{project['id']}/pipelines/new",
                        )["+ Pipeline"],
                    ],
                ],
            ]
        ]
    ]


def pipeline_card(pipeline: Dict[str, Any], project_name: str = None) -> Any:
    """Generate a pipeline card component"""
    status = pipeline.get("status", "Unknown")
    status_class = {
        "Active": "success",
        "Inactive": "secondary",
        "Error": "error",
        "Running": "primary",
        "Scheduled": "info",
    }.get(status, "secondary")

    pipeline_type = pipeline.get("type", "batch")
    type_class = {
        "batch": "secondary",
        "streaming": "info",
        "scheduled": "warning",
    }.get(pipeline_type, "secondary")

    return h.div(class_="w-full md:w-1/2 lg:w-1/3 mb-3 px-2")[
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.h2(class_="card-title")[pipeline["name"]],
                h.p()[pipeline.get("description", "No description")],
                h.div(class_="flex justify-between items-center mb-2")[
                    h.div(class_="flex gap-2")[
                        h.span(class_=f"badge badge-{status_class}")[status],
                        h.span(class_=f"badge badge-{type_class}")[pipeline_type],
                    ]
                ],
                (
                    h.div(class_="mb-2")[
                        h.span(class_="text-xs text-base-content/60")[f"Project: {project_name}"]
                    ]
                    if project_name
                    else h.div()
                ),
                h.div(class_="flex justify-between items-center mt-2")[
                    h.div(class_="flex gap-2")[
                        h.a(
                            class_="btn btn-primary btn-sm",
                            href=f"/pipelines/{pipeline['id']}",
                        )["View"],
                        h.a(
                            class_="btn btn-outline btn-secondary btn-sm",
                            href=f"/pipelines/{pipeline['id']}/edit",
                        )["Edit"],
                    ],
                    h.div(class_="flex gap-2")[
                        h.a(
                            class_="btn btn-success btn-sm",
                            href=f"/pipelines/{pipeline['id']}/run",
                        )["Run"],
                        h.a(
                            class_="btn btn-outline btn-info btn-sm",
                            href=f"/pipelines/{pipeline['id']}/visualize",
                        )["DAG"],
                        h.a(
                            class_="btn btn-outline btn-secondary btn-sm",
                            href=f"/pipelines/{pipeline['id']}/schedule",
                        )["Schedule"],
                    ],
                ],
            ]
        ]
    ]

