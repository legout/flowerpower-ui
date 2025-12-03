import reflex as rx
import random
from datetime import datetime, timedelta
import asyncio
from pydantic import BaseModel


class ExecutionLog(BaseModel):
    timestamp: str
    level: str
    message: str


class ExecutionRecord(BaseModel):
    id: str
    status: str
    start_time: str
    end_time: str
    duration: float
    triggered_by: str


class Pipeline(BaseModel):
    id: str
    name: str
    description: str
    status: str
    last_run: str
    config_type: str


class ExecutionState(rx.State):
    pipeline_id: str = ""
    status: str = "idle"
    is_running: bool = False
    execution_history: list[ExecutionRecord] = []
    logs: list[ExecutionLog] = []
    executor_type: str = "threadpool"
    max_workers: int = 4
    retry_count: int = 3
    timeout_seconds: int = 3600
    current_run_id: str = ""
    current_run_duration: str = "00:00:00"
    pipelines: list[Pipeline] = [
        Pipeline(
            id="etl-processor",
            name="ETL Processor",
            description="Transforms raw data into analytics-ready format.",
            status="running",
            last_run="2023-10-27 09:15:00",
            config_type="JSON",
        ),
        Pipeline(
            id="ml-model-training",
            name="ML Model Training",
            description="Retrains the recommendation model.",
            status="failed",
            last_run="2023-10-26 14:30:00",
            config_type="YAML",
        ),
        Pipeline(
            id="data-ingestion",
            name="Data Ingestion Service",
            description="Ingests raw data from external APIs daily.",
            status="success",
            last_run="2023-10-27 08:00:00",
            config_type="YAML",
        ),
        Pipeline(
            id="report-generator",
            name="Monthly Report Generator",
            description="Generates PDF reports for stakeholders.",
            status="idle",
            last_run="2023-10-01 00:00:00",
            config_type="YAML",
        ),
        Pipeline(
            id="log-archiver",
            name="Log Archiver",
            description="Moves old logs to cold storage.",
            status="idle",
            last_run="2023-10-25 23:00:00",
            config_type="YAML",
        ),
        Pipeline(
            id="user-sync",
            name="User Sync",
            description="Synchronizes user data across microservices.",
            status="success",
            last_run="2023-10-27 10:00:00",
            config_type="JSON",
        ),
    ]

    @rx.event
    def select_pipeline(self, pid: str):
        self.pipeline_id = pid
        self.status = "idle"
        self.is_running = False
        self.logs = []
        self._generate_mock_history()

    @rx.event
    def clear_selection(self):
        self.pipeline_id = ""
        self.execution_history = []

    @rx.var
    def has_selected_pipeline(self) -> bool:
        return self.pipeline_id != ""

    def _generate_mock_history(self):
        """Generates some random historical data."""
        history = []
        base_time = datetime.now() - timedelta(days=7)
        statuses = ["success", "success", "success", "failed", "success", "warning"]
        for i in range(15):
            start = base_time + timedelta(hours=i * 12 + random.randint(0, 5))
            duration_secs = random.randint(45, 300)
            end = start + timedelta(seconds=duration_secs)
            status = random.choice(statuses)
            history.append(
                ExecutionRecord(
                    id=f"exec_{random.randint(10000, 99999)}",
                    status=status,
                    start_time=start.strftime("%Y-%m-%d %H:%M"),
                    end_time=end.strftime("%Y-%m-%d %H:%M"),
                    duration=float(duration_secs),
                    triggered_by="schedule" if random.random() > 0.3 else "manual",
                )
            )
        history.sort(key=lambda x: x.start_time, reverse=True)
        self.execution_history = history

    @rx.var
    def recent_logs(self) -> list[ExecutionLog]:
        return self.logs[-50:] if self.logs else []

    @rx.var
    def success_rate(self) -> float:
        if not self.execution_history:
            return 0.0
        success_count = sum(
            (1 for e in self.execution_history if e.status == "success")
        )
        return round(success_count / len(self.execution_history) * 100, 1)

    @rx.var
    def avg_duration(self) -> float:
        if not self.execution_history:
            return 0.0
        total_duration = sum((e.duration for e in self.execution_history))
        return round(total_duration / len(self.execution_history), 1)

    @rx.var
    def total_runs(self) -> int:
        return len(self.execution_history)

    @rx.var
    def chart_data(self) -> list[dict[str, str | float]]:
        data = []
        recent = self.execution_history[:10][::-1]
        for run in recent:
            name_val = run.start_time
            if " " in run.start_time:
                name_val = run.start_time.split(" ")[1]
            data.append(
                {"name": name_val, "duration": run.duration, "status": run.status}
            )
        return data

    @rx.event(background=True)
    async def start_pipeline(self):
        async with self:
            if self.is_running:
                return
            self.is_running = True
            self.status = "running"
            self.current_run_id = f"run_{random.randint(10000, 99999)}"
            self.logs = []
        stages = [
            "Initializing",
            "Loading Data",
            "Processing",
            "Validating",
            "Exporting",
            "Finalizing",
        ]
        for stage in stages:
            await asyncio.sleep(1.5)
            async with self:
                self.logs.append(
                    ExecutionLog(
                        timestamp=datetime.now().strftime("%H:%M:%S"),
                        level="INFO",
                        message=f"[{stage}] Operation completed successfully.",
                    )
                )
        async with self:
            self.is_running = False
            self.status = "success"
            new_record = ExecutionRecord(
                id=self.current_run_id,
                status="success",
                start_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
                end_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
                duration=random.randint(50, 150),
                triggered_by="manual",
            )
            self.execution_history.insert(0, new_record)

    @rx.event
    def stop_pipeline(self):
        self.is_running = False
        self.status = "stopped"
        self.logs.append(
            ExecutionLog(
                timestamp=datetime.now().strftime("%H:%M:%S"),
                level="WARNING",
                message="Pipeline execution stopped by user.",
            )
        )

    @rx.event
    def update_settings(self, form_data: dict):
        self.executor_type = form_data.get("executor_type", self.executor_type)
        self.max_workers = int(form_data.get("max_workers", self.max_workers))
        rx.toast("Settings updated successfully", duration=3000)
