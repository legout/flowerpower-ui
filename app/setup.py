from flowerpower import FlowerPowerProject
from flowerpower.fs import BaseStorageOptions, AbstractFileSystem
from sanic import Sanic

import msgspec
import msgspec.yaml


class ProjectConfig(msgspec.Struct):
    name: str
    base_dir: str
    storage_options: dict


class ProjectsConfig(msgspec.Struct):
    projects: list[ProjectConfig]


class FlowerPowerProjectManager:
    CONFIG_PATH = "./config/projects_config.yaml"
    SENSITIVE_KEYS = {
        "password",
        "secret",
        "token",
        "api_key",
        "access_key",
        "secret_key",
    }

    def __init__(self):
        self.projects = {}

    def load_configs(self):
        """Load all project configs from YAML file using msgspec."""
        import os

        if not os.path.exists(self.CONFIG_PATH):
            return ProjectsConfig(projects=[])
        with open(self.CONFIG_PATH, "rb") as f:
            return msgspec.yaml.decode(f.read(), type=ProjectsConfig)

    def save_configs(self, projects_config: ProjectsConfig):
        """Save all project configs to YAML file using msgspec."""
        import os

        os.makedirs(os.path.dirname(self.CONFIG_PATH), exist_ok=True)
        with open(self.CONFIG_PATH, "wb") as f:
            f.write(msgspec.yaml.encode(projects_config))

    def get_env_or_missing(self, project_name: str, key: str):
        """Try to get sensitive value from env, else return None (to prompt)."""
        import os

        env_key = f"{project_name.upper()}_{key.upper()}"
        return os.environ.get(env_key)

    def collect_storage_options(self, project_name: str, storage_options: dict):
        """Return storage_options with sensitive values from env or marked as missing."""
        result = {}
        missing = []
        for k, v in storage_options.items():
            if k in self.SENSITIVE_KEYS:
                env_val = self.get_env_or_missing(project_name, k)
                if env_val is not None:
                    result[k] = env_val
                else:
                    result[k] = None
                    missing.append(k)
            else:
                result[k] = v
        return result, missing
        self.projects = {}

    def get_project(self, project_id: str) -> FlowerPowerProject | None:
        """Get a project by ID"""
        return self.projects.get(project_id)

    def add_project(self, project: FlowerPowerProject):
        """Add a project to the manager"""
        self.projects[project.name] = project

    def load_project(
        self,
        base_dir: str,
        storage_options: BaseStorageOptions | dict | None = None,
        fs: AbstractFileSystem | None = None,
    ) -> FlowerPowerProject:
        """
        Load a FlowerPower project from any fsspec compatible filesystem.

        Args:
            base_dir: Base directory path for the project. Can be:
                     - Local path: "/path/to/project" or "file:///path/to/project"
                     - S3: "s3://bucket/path/to/project"
                     - GCS: "gcs://bucket/path/to/project" or "gs://bucket/path/to/project"
                     - GitHub: "github://path/to/project"
                     - HTTP: "http://example.com/path/to/project"
                     - Any other fsspec supported protocol
            storage_options: Filesystem-specific options dict. Examples:
                           - S3: {"key": "access_key", "secret": "secret_key", "endpoint_url": "https://..."}
                           - GCS: {"token": "path/to/service_account.json"}
                           - GitHub: {"org": "organization", "repo": "repository"}

        Returns:
            FlowerPowerProject: Loaded project instance

        Raises:
            FileNotFoundError: If project path doesn't exist
            ValueError: If project configuration is invalid
        """

        try:
            # Use FlowerPower's built-in load method with fsspec support
            project = FlowerPowerProject.load(
                base_dir=base_dir, storage_options=storage_options, fs=fs
            )

            # Add to manager
            self.add_project(project)

            return project

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Project not found at {base_dir}: {e}")
        except Exception as e:
            raise ValueError(f"Failed to load project from {base_dir}: {e}")

    def new_project(
        self,
        name: str,
        base_dir: str,
        storage_options: BaseStorageOptions | dict | None = None,
        fs: AbstractFileSystem | None = None,
        job_queue_type: str | None = None,
    ) -> FlowerPowerProject:
        """
        Create a new FlowerPower project on any writable filesystem.

        Args:
            name: Project name
            base_dir: Base directory path where to create the project. Can be:
                     - Local path: "/path/to/new_project" or "file:///path/to/new_project"
                     - S3: "s3://bucket/path/to/new_project"
                     - GCS: "gcs://bucket/path/to/new_project"
                     - Any other writable fsspec supported protocol
            storage_options: Filesystem-specific options dict. Examples:
                           - S3: {"key": "access_key", "secret": "secret_key", "endpoint_url": "https://..."}
                           - GCS: {"token": "path/to/service_account.json"}
            fs: Optional custom filesystem instance to use
            job_queue_type: Optional job queue type to use (e.g. "apscheduler", "rq")

        Returns:
            FlowerPowerProject: New project instance

        Raises:
            FileExistsError: If project already exists at path
            PermissionError: If filesystem is not writable
            ValueError: If parameters are invalid
        """
        try:
            project = FlowerPowerProject.init(
                name=name,
                base_dir=base_dir,
                storage_options=storage_options,
                fs=fs,
                job_queue_type=job_queue_type,  # type: ignore
            )

            # Add to manager
            self.add_project(project)

            return project

        except FileExistsError as e:
            raise FileExistsError(f"Project already exists at {base_dir}: {e}")
        except PermissionError as e:
            raise PermissionError(f"Cannot create project at {base_dir}: {e}")
        except Exception as e:
            raise ValueError(f"Failed to create project at {base_dir}: {e}")


def setup_project_manager(app: Sanic) -> Sanic:
    app.ctx.project_manager = FlowerPowerProjectManager()
    return app
