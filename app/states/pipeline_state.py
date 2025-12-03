import reflex as rx
from typing import Any
import random
from datetime import datetime, timedelta


class Execution(rx.Base):
    id: str
    timestamp: str
    status: str
    duration: str
    logs: str = ""


class Pipeline(rx.Base):
    id: str
    name: str
    description: str
    status: str
    last_run: str
    config_type: str
    schedule: str
    config_content: str = ""


class PipelineState(rx.State):
    pipelines: list[Pipeline] = []
    search_query: str = ""
    status_filter: str = "All Statuses"
    selected_pipeline: Pipeline | None = None
    is_details_open: bool = False
    is_create_open: bool = False
    is_edit_mode: bool = False
    form_name: str = ""
    form_description: str = ""
    form_config: str = ""
    current_executions: list[Execution] = []

    @rx.var
    def filtered_pipelines(self) -> list[Pipeline]:
        filtered = self.pipelines
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                p
                for p in filtered
                if query in p.name.lower() or query in p.description.lower()
            ]
        if self.status_filter != "All Statuses":
            filtered = [
                p for p in filtered if p.status.lower() == self.status_filter.lower()
            ]
        return filtered

    @rx.event
    def on_load(self):
        """Load initial pipeline data."""
        if not self.pipelines:
            self.pipelines = [
                Pipeline(
                    id="etl-processor",
                    name="ETL Processor",
                    description="Transforms raw data into analytics-ready format.",
                    status="running",
                    last_run="2023-10-27 09:15:00",
                    config_type="JSON",
                    schedule="Daily",
                    config_content="""{
  "source": "s3://bucket/raw",
  "dest": "snowflake.dw.fact_sales"
}""",
                ),
                Pipeline(
                    id="ml-training",
                    name="ML Model Training",
                    description="Retrains the recommendation model.",
                    status="failed",
                    last_run="2023-10-26 14:30:00",
                    config_type="YAML",
                    schedule="Weekly",
                    config_content="""model:
  type: xgboost
  hyperparams:
    max_depth: 5
    eta: 0.2""",
                ),
                Pipeline(
                    id="data-ingestion",
                    name="Data Ingestion Service",
                    description="Ingests raw data from external APIs daily.",
                    status="success",
                    last_run="2023-10-27 08:00:00",
                    config_type="YAML",
                    schedule="Daily",
                    config_content="""sources:
  - api: stripe
    endpoint: /v1/charges
  - api: shopify
    endpoint: /orders""",
                ),
                Pipeline(
                    id="report-generator",
                    name="Monthly Report Generator",
                    description="Generates PDF reports for stakeholders.",
                    status="idle",
                    last_run="2023-10-01 00:00:00",
                    config_type="YAML",
                    schedule="Monthly",
                    config_content="""report_type: financial_summary
recipients:
  - finance@company.com
  - cfo@company.com""",
                ),
                Pipeline(
                    id="log-archiver",
                    name="Log Archiver",
                    description="Moves old logs to cold storage.",
                    status="idle",
                    last_run="2023-10-25 23:00:00",
                    config_type="YAML",
                    schedule="Daily",
                    config_content="""retention_days: 30
storage_class: GLACIER""",
                ),
                Pipeline(
                    id="user-sync",
                    name="User Sync",
                    description="Synchronizes user data across microservices.",
                    status="success",
                    last_run="2023-10-27 10:00:00",
                    config_type="JSON",
                    schedule="Hourly",
                    config_content="""{
  "services": ["auth", "billing", "crm"],
  "conflict_resolution": "latest_wins"
}""",
                ),
            ]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_status_filter(self, status: str):
        self.status_filter = status

    @rx.event
    def close_modals(self):
        self.is_details_open = False
        self.is_create_open = False
        self.selected_pipeline = None

    @rx.event
    def open_create_modal(self):
        self.is_edit_mode = False
        self.form_name = ""
        self.form_description = ""
        self.form_config = ""
        self.is_create_open = True

    @rx.event
    def open_edit_modal(self, pipeline: Pipeline):
        self.selected_pipeline = pipeline
        self.is_edit_mode = True
        self.form_name = pipeline.name
        self.form_description = pipeline.description
        self.form_config = pipeline.config_content
        self.is_create_open = True

    @rx.event
    def open_details_modal(self, pipeline: Pipeline):
        self.selected_pipeline = pipeline
        self.current_executions = [
            Execution(
                id=f"exec-{random.randint(1000, 9999)}",
                timestamp=(datetime.now() - timedelta(hours=i * 2)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                status=(
                    random.choice(["success", "failed", "success", "running"])
                    if i == 0
                    else random.choice(["success", "failed"])
                ),
                duration=f"{random.randint(10, 300)}s",
                logs=f"Starting execution...\nLoading configuration...\nStep 1: Processing data...\nStep 2: Validating results...\n{('Process completed successfully.' if random.random() > 0.2 else 'Error: Connection timeout.')}",
            )
            for i in range(5)
        ]
        self.is_details_open = True

    @rx.event
    def save_pipeline(self, form_data: dict):
        if self.is_edit_mode and self.selected_pipeline:
            for i, p in enumerate(self.pipelines):
                if p.id == self.selected_pipeline.id:
                    self.pipelines[i].name = form_data["name"]
                    self.pipelines[i].description = form_data["description"]
                    self.pipelines[i].config_content = form_data["config"]
                    break
            rx.toast("Pipeline updated successfully")
        else:
            new_pipeline = Pipeline(
                id=f"new-{random.randint(1000, 9999)}",
                name=form_data["name"],
                description=form_data["description"],
                status="idle",
                last_run="Never",
                config_type="YAML",
                schedule="Manual",
                config_content=form_data["config"],
            )
            self.pipelines.append(new_pipeline)
            rx.toast("Pipeline created successfully")
        self.close_modals()

    @rx.event
    def delete_pipeline(self, id: str):
        self.pipelines = [p for p in self.pipelines if p.id != id]
        self.close_modals()
        rx.toast("Pipeline deleted")

    @rx.event
    def run_pipeline_mock(self):
        rx.toast("Pipeline execution started")
