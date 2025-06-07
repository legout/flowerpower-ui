import htpy as h
from typing import Any, Dict
from flowerpower import FlowerPowerProject


def base_layout(title: str, content: Any) -> str:
    """Base HTML layout with navigation, Nord theme, and Datastar setup"""
    return str(
        h.html(**{"data-theme": "nord-light"})[
            h.head[
                h.meta(charset="utf-8"),
                h.meta(name="viewport", content="width=device-width, initial-scale=1"),
                h.title[f"{title} - FlowerPower"],
                # Google Fonts - Inter for modern typography
                h.link(
                    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
                    rel="stylesheet",
                ),
                # Tailwind CSS
                h.script(src="https://cdn.tailwindcss.com"),
                # Datastar
                h.script(src="https://unpkg.com/@starfederation/datastar@latest"),
                # Heroicons for modern icons
                h.script(src="https://unpkg.com/heroicons@2.0.18/24/outline/index.js", type="module"),
                # DaisyUI CDN
                h.script(src="https://cdn.jsdelivr.net/npm/daisyui@latest/dist/full.js"),
                # DaisyUI theme selector
                h.select(
                    class_="select select-bordered ml-4",
                    onchange="document.documentElement.setAttribute('data-theme', this.value)"
                )[
                    h.option(value="light")["Light"],
                    h.option(value="dark")["Dark"],
                    h.option(value="cupcake")["Cupcake"],
                    h.option(value="bumblebee")["Bumblebee"],
                    h.option(value="emerald")["Emerald"],
                    h.option(value="corporate")["Corporate"],
                ],
            ],
            h.body(**{"data-ds-stream": "/datastar/stream"})[
                # Navigation with Nord theme
                h.nav(class_="flex items-center justify-between px-6 py-4 border-b", style="background-color: var(--bg-secondary); border-color: var(--border-color);")[
                    h.div(class_="flex items-center space-x-8")[
                        h.a(class_="text-2xl font-bold text-primary hover:scale-105 transition-transform duration-200", href="/")[
                            "🌸 FlowerPower"
                        ],
                        h.div(class_="hidden md:flex items-center space-x-6")[
                            h.a(href="/dashboard", class_="px-3 py-2 rounded-lg hover:bg-opacity-20 transition-all duration-200", style="color: var(--text-secondary); hover:background-color: var(--accent-primary);")["📊 Dashboard"],
                            h.a(href="/projects", class_="px-3 py-2 rounded-lg hover:bg-opacity-20 transition-all duration-200", style="color: var(--text-secondary); hover:background-color: var(--accent-primary);")["📁 Projects"],
                            h.a(href="/projects/new", class_="px-3 py-2 rounded-lg hover:bg-opacity-20 transition-all duration-200", style="color: var(--text-secondary); hover:background-color: var(--accent-primary);")["➕ New Project"],
                            h.a(href="/pipelines", class_="px-3 py-2 rounded-lg hover:bg-opacity-20 transition-all duration-200", style="color: var(--text-secondary); hover:background-color: var(--accent-primary);")["🔗 Pipelines"],
                            h.a(href="/jobs", class_="px-3 py-2 rounded-lg hover:bg-opacity-20 transition-all duration-200", style="color: var(--text-secondary); hover:background-color: var(--accent-primary);")["⚙️ Job Queue"],
                        ],
                    ],
                    # Theme toggle button
                    h.button(
                        onclick="toggleTheme()",
                        class_="p-2 rounded-lg transition-all duration-200 hover:scale-110",
                        style="background-color: var(--bg-accent); color: var(--text-primary);",
                        title="Toggle light/dark theme"
                    )[
                        h.span(class_="text-lg")["🌓"]
                    ],
                ],
                h.main(class_="flex-1 animate-fade-in")[
                    h.div(class_="container mx-auto px-6 py-8")[content],
                ],
            ],
        ]
    )


def project_card(project: FlowerPowerProject) -> Any:
    """Generate a project card component with Nord styling"""
    status = project.get("status", "Unknown")
    status_class_map = {
        "Active": "badge badge-success",
        "Inactive": "badge badge-ghost",
        "Error": "badge badge-error",
    }
    status_class = status_class_map.get(status, "badge badge-secondary")

    # Count pipelines for this project
    pipelines = project.pipeline_manager.pipelines
    pipeline_count = len(pipelines)

    return h.div(class_="w-full md:w-1/2 lg:w-1/3 p-3 animate-slide-up")[
        h.div(class_="card bg-base-100 shadow-xl h-full")[
            h.div(class_="card-body flex flex-col")[
                h.div(class_="flex-1")[
                    h.h3(class_="card-title text-xl mb-3")[
                        project["name"]
                    ],
                    h.p(class_="text-base-content/70 mb-4 leading-relaxed")[
                        project.get("description", "No description available")
                    ],
                    h.div(class_="flex justify-between items-center mb-4")[
                        h.div(class_=f"badge {status_class}")[status],
                        h.span(class_="text-sm text-base-content/60")[
                            f"📊 {pipeline_count} pipeline{'s' if pipeline_count != 1 else ''}"
                        ],
                    ],
                ],
                h.div(class_="card-actions justify-end")[
                    h.div(class_="flex flex-col gap-2 w-full")[
                        h.div(class_="flex gap-2")[
                            h.a(
                                class_="btn btn-primary btn-sm flex-1",
                                href=f"/projects/{project['id']}",
                            )["👁️ View"],
                            h.a(
                                class_="btn btn-outline btn-sm flex-1",
                                href=f"/projects/{project['id']}/edit",
                            )["✏️ Edit"],
                        ],
                        h.div(class_="flex gap-2")[
                            h.a(
                                class_="btn btn-ghost btn-sm flex-1",
                                href=f"/projects/{project['id']}/pipelines",
                            )["🔗 Pipelines"],
                            h.a(
                                class_="btn btn-ghost btn-sm flex-1",
                                href=f"/projects/{project['id']}/pipelines/new",
                            )["➕ Pipeline"],
                        ],
                    ],
                ],
            ]
        ]
    ]


def pipeline_card(pipeline: Dict[str, Any], project_name: str = None) -> Any:
    """Generate a pipeline card component with Nord styling"""
    status = pipeline.get("status", "Unknown")
    status_class_map = {
        "Active": "badge badge-success",
        "Inactive": "badge badge-secondary",
        "Error": "badge badge-error",
        "Running": "badge badge-info",
        "Scheduled": "badge badge-warning",
    }
    status_class = status_class_map.get(status, "nord-badge-secondary")

    pipeline_type = pipeline.get("type", "batch")
    type_class_map = {
        "batch": "badge badge-secondary",
        "streaming": "badge badge-info",
        "scheduled": "badge badge-warning",
    }
    type_class = type_class_map.get(pipeline_type, "nord-badge-secondary")

    return h.div(class_="w-full md:w-1/2 lg:w-1/3 p-3 animate-slide-up")[
        h.div(class_="card p-6 h-full flex flex-col")[
            h.div(class_="flex-1")[
                h.h3(class_="text-xl font-semibold mb-3", style="color: var(--text-primary);")[
                    pipeline["name"]
                ],
                h.p(class_="mb-4 leading-relaxed", style="color: var(--text-secondary);")[
                    pipeline.get("description", "No description available")
                ],
                h.div(class_="flex justify-between items-center mb-2")[
                    h.div(class_="flex space-x-2")[
                        h.span(class_=status_class)[status],
                        h.span(class_=type_class)[pipeline_type.title()],
                    ]
                ],
                (
                    h.div(class_="mb-4")[
                        h.span(class_="text-sm", style="color: var(--text-muted);")[
                            f"📁 Project: {project_name}"
                        ]
                    ]
                    if project_name
                    else h.div()
                ),
            ],
            h.div(class_="flex flex-col space-y-3")[
                h.div(class_="flex space-x-2")[
                    h.a(
                        class_="btn flex-1 text-center text-sm",
                        href=f"/pipelines/{pipeline['id']}",
                    )["👁️ View"],
                    h.a(
                        class_="btn btn-secondary flex-1 text-center text-sm",
                        href=f"/pipelines/{pipeline['id']}/edit",
                    )["✏️ Edit"],
                ],
                h.div(class_="flex space-x-2")[
                    h.a(
                        class_="btn text-center text-sm",
                        href=f"/pipelines/{pipeline['id']}/run",
                        style="background-color: var(--nord-green); color: white;"
                    )["▶️ Run"],
                    h.a(
                        class_="btn btn-secondary text-center text-sm",
                        href=f"/pipelines/{pipeline['id']}/visualize",
                    )["📊 DAG"],
                ],
            ]
        ]
    ]


def landing_page() -> str:
    """Generate the landing page content with DaisyUI Nord styling"""
    return base_layout(
        title="Welcome",
        content=h.div(class_="hero min-h-[70vh]")[
            h.div(class_="hero-content text-center max-w-4xl animate-fade-in")[
                h.div()[
                    h.div(class_="mb-8")[
                        h.h1(class_="text-5xl md:text-6xl font-bold mb-6 text-primary")[
                            "Welcome to FlowerPower!"
                        ],
                        h.p(class_="text-xl leading-relaxed text-base-content/70 max-w-2xl mx-auto")[
                            "Your powerful platform for managing data pipelines and projects with elegance and efficiency."
                        ],
                    ],
                    h.div(class_="flex flex-col sm:flex-row justify-center gap-4 mb-16")[
                        h.a(class_="btn btn-primary btn-lg", href="/dashboard")[
                            "🚀 Get Started"
                        ],
                        h.a(class_="btn btn-outline btn-lg", href="/projects")[
                            "📁 View Projects"
                        ],
                    ],
                    h.div(class_="grid grid-cols-1 md:grid-cols-3 gap-6")[
                        h.div(class_="card bg-base-200 shadow-xl p-6 text-center card-hover")[
                            h.div(class_="text-4xl mb-4")["🔗"],
                            h.h3(class_="text-lg font-semibold mb-2 text-base-content")["Data Pipelines"],
                            h.p(class_="text-sm text-base-content/70")["Build and manage complex data workflows"],
                        ],
                        h.div(class_="card bg-base-200 shadow-xl p-6 text-center card-hover")[
                            h.div(class_="text-4xl mb-4")["📊"],
                            h.h3(class_="text-lg font-semibold mb-2 text-base-content")["Real-time Monitoring"],
                            h.p(class_="text-sm text-base-content/70")["Track pipeline status and performance"],
                        ],
                        h.div(class_="card bg-base-200 shadow-xl p-6 text-center card-hover")[
                            h.div(class_="text-4xl mb-4")["⚙️"],
                            h.h3(class_="text-lg font-semibold mb-2 text-base-content")["Easy Management"],
                            h.p(class_="text-sm text-base-content/70")["Intuitive interface for all operations"],
                        ],
                    ],
                ]
            ],
        ],
    )


def projects_page(project_manager) -> str:
    """Projects list page with DaisyUI styling"""
    projects = project_manager.projects
    
    # Header with new project button
    header = h.div(class_="flex justify-between items-center mb-12 animate-slide-up")[
        h.h1(class_="text-4xl md:text-5xl font-bold text-primary")[
            "🌸 FlowerPower Projects"
        ],
        h.div(class_="flex flex-col sm:flex-row gap-4")[
            h.a(
                href="/projects/new",
                class_="btn btn-primary text-lg"
            )[
                "➕ New Project"
            ],
            h.button(
                class_="btn btn-outline text-lg",
                onclick="loadProjectModal.showModal()"
            )[
                "📂 Load Project"
            ]
        ]
    ]
    
    # Projects grid
    if projects:
        projects_grid = h.div(class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6")[
            *[project_card(project) for project in projects.values()]
        ]
    else:
        projects_grid = h.div(class_="hero min-h-[400px] animate-fade-in")[
            h.div(class_="hero-content text-center")[
                h.div(class_="max-w-md")[
                    h.div(class_="text-8xl mb-6")["📋"],
                    h.h3(class_="text-3xl font-bold mb-4 text-base-content")["No Projects Yet"],
                    h.p(class_="mb-8 text-base-content/70")[
                        "Create your first FlowerPower project to get started with building amazing data pipelines!"
                    ],
                    h.a(
                        href="/projects/new",
                        class_="btn btn-primary btn-lg"
                    )[
                        "🚀 Create First Project"
                    ]
                ]
            ]
        ]
    
    # Load project modal with DaisyUI styling
    load_modal = h.dialog(id="loadProjectModal", class_="modal")[
        h.div(class_="modal-box max-w-lg")[
            h.form(method="dialog")[
                h.button(class_="btn btn-sm btn-circle btn-ghost absolute right-2 top-2")["✕"]
            ],
            h.h3(class_="font-bold text-2xl mb-6 text-center text-primary")[
                "📂 Load Existing Project"
            ],
            h.form(action="/projects/load", method="post", class_="space-y-6")[
                h.div()[
                    h.label(class_="label")[
                        h.span(class_="label-text text-lg font-semibold")[
                            "Project Directory Path"
                        ]
                    ],
                    h.input(
                        type="text",
                        name="base_dir",
                        placeholder="/path/to/existing/project",
                        class_="input input-bordered w-full",
                        required=True
                    ),
                    h.label(class_="label")[
                        h.span(class_="label-text-alt text-base-content/70")[
                            "Enter the full path to an existing FlowerPower project directory"
                        ]
                    ]
                ],
                h.div(class_="modal-action")[
                    h.button(
                        type="submit",
                        class_="btn btn-primary"
                    )[
                        "📂 Load Project"
                    ],
                    h.button(
                        type="button",
                        class_="btn btn-ghost",
                        onclick="loadProjectModal.close()"
                    )[
                        "Cancel"
                    ]
                ]
            ]
        ]
    ]
    
    content = h.div()[
        header,
        projects_grid,
        load_modal
    ]
    
    return base_layout("Projects", content)


def new_project_page() -> str:
    """New project creation page with DaisyUI styling"""
    
    # Header
    header = h.div(class_="text-center mb-16 animate-slide-up")[
        h.h1(class_="text-5xl md:text-6xl font-bold mb-6 text-primary")[
            "🌟 Create New Project"
        ],
        h.p(class_="text-xl text-base-content/70")[
            "Set up a new FlowerPower project to manage your data pipelines with style"
        ]
    ]
    
    # Form
    form_content = h.form(
        action="/projects/create",
        method="post",
        class_="max-w-3xl mx-auto space-y-8 animate-fade-in"
    )[
        # Project Name
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.div(class_="form-control")[
                    h.label(class_="label")[
                        h.span(class_="label-text text-xl font-semibold")[
                            "🏷️ Project Name"
                        ]
                    ],
                    h.input(
                        type="text",
                        name="name",
                        placeholder="My Awesome Data Project",
                        class_="input input-bordered input-lg w-full",
                        required=True
                    ),
                    h.label(class_="label")[
                        h.span(class_="label-text-alt text-base-content/70")[
                            "Choose a descriptive name that reflects your project's purpose"
                        ]
                    ]
                ]
            ]
        ],
        
        # Base Directory
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.div(class_="form-control")[
                    h.label(class_="label")[
                        h.span(class_="label-text text-xl font-semibold")[
                            "📁 Project Directory"
                        ]
                    ],
                    h.input(
                        type="text",
                        name="base_dir",
                        placeholder="/path/to/new/project",
                        class_="input input-bordered input-lg w-full",
                        required=True
                    ),
                    h.label(class_="label")[
                        h.span(class_="label-text-alt text-base-content/70")[
                            "Full path where the project will be created (directory must not exist)"
                        ]
                    ]
                ]
            ]
        ],
        
        # Job Queue Type
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.div(class_="form-control")[
                    h.label(class_="label")[
                        h.span(class_="label-text text-xl font-semibold")[
                            "⚙️ Job Queue Type (Optional)"
                        ]
                    ],
                    h.select(
                        name="job_queue_type",
                        class_="select select-bordered select-lg w-full"
                    )[
                        h.option(value="", selected=True)["Default (No specific queue)"],
                        h.option(value="apscheduler")["APScheduler"],
                        h.option(value="rq")["RQ (Redis Queue)"],
                        h.option(value="celery")["Celery"]
                    ],
                    h.label(class_="label")[
                        h.span(class_="label-text-alt text-base-content/70")[
                            "Choose a job queue system for pipeline execution"
                        ]
                    ]
                ]
            ]
        ],
        
        # Action buttons
        h.div(class_="flex flex-col sm:flex-row gap-4 pt-8")[
            h.button(
                type="submit",
                class_="btn btn-primary btn-lg flex-1"
            )[
                "🚀 Create Project"
            ],
            h.a(
                href="/projects",
                class_="btn btn-outline btn-lg flex-1"
            )[
                "← Back to Projects"
            ]
        ]
    ]
    
    # Tips section
    tips = h.div(class_="max-w-3xl mx-auto mt-16 animate-slide-up")[
        h.div(class_="card bg-base-100 shadow-xl")[
            h.div(class_="card-body")[
                h.h3(class_="card-title text-2xl mb-6")[
                    h.span(class_="text-3xl mr-3")["💡"],
                    "Quick Tips"
                ],
                h.div(class_="grid md:grid-cols-2 gap-4")[
                    h.div(class_="flex items-start space-x-3")[
                        h.span(class_="text-success")["✓"],
                        h.span(class_="text-base-content/70")["Make sure the project directory doesn't already exist"]
                    ],
                    h.div(class_="flex items-start space-x-3")[
                        h.span(class_="text-success")["✓"],
                        h.span(class_="text-base-content/70")["Choose a meaningful name that describes your project's purpose"]
                    ],
                    h.div(class_="flex items-start space-x-3")[
                        h.span(class_="text-success")["✓"],
                        h.span(class_="text-base-content/70")["The job queue type can be changed later in project settings"]
                    ],
                    h.div(class_="flex items-start space-x-3")[
                        h.span(class_="text-success")["✓"],
                        h.span(class_="text-base-content/70")["You can load existing projects from the Projects page"]
                    ],
                ]
            ]
        ]
    ]
    
    content = h.div()[
        header,
        form_content,
        tips
    ]
    
    return base_layout("New Project", content)
