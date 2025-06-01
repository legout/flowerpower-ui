from sanic import Sanic
from sanic.response import json, html
from flowerpower import FlowerPowerProject
import htpy as h
from typing import Any, Optional, Dict

app = Sanic("FlowerPowerUI")


class FlowerPowerProjectManager:
    def __init__(self):
        self.projects = {}

    def get_project(self, project_id: str) -> FlowerPowerProject | None:
        """Get a project by ID"""
        return self.projects.get(project_id)

    def add_project(self, project: FlowerPowerProject):
        """Add a project to the manager"""
        self.projects[project.id] = project

    def load_project(
        self,
        base_dir: str,
        storage_options: Optional[Dict[str, Any]] = None
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
        storage_options = storage_options or {}
        
        try:
            # Use FlowerPower's built-in load method with fsspec support
            project = FlowerPowerProject.load(
                base_dir=base_dir,
                storage_options=storage_options
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
        storage_options: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        template: Optional[str] = None
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
            description: Optional project description
            template: Optional project template to use (if supported by FlowerPower)
                     
        Returns:
            FlowerPowerProject: New project instance
            
        Raises:
            FileExistsError: If project already exists at path
            PermissionError: If filesystem is not writable
            ValueError: If parameters are invalid
        """
        storage_options = storage_options or {}
        
        # Validate parameters
        if not name:
            raise ValueError("Project name cannot be empty")
        if not base_dir:
            raise ValueError("Base directory cannot be empty")
        
        # Check for read-only protocols
        if base_dir.startswith('github://'):
            raise ValueError("GitHub filesystem is typically read-only. Use a different protocol for creating projects.")
        
        try:
            # Use FlowerPower's built-in init method with fsspec support
            project = FlowerPowerProject.init(
                name=name,
                base_dir=base_dir,
                storage_options=storage_options
            )
            
            # Add additional configuration if provided
            if description:
                # Set description if FlowerPower supports it
                if hasattr(project, 'description'):
                    project.description = description
                elif hasattr(project, 'config') and hasattr(project.config, 'description'):
                    project.config.description = description
            
            # Apply template if specified and supported
            if template:
                self._apply_project_template(project, template)
            
            # Add to manager
            self.add_project(project)
            
            return project
            
        except FileExistsError as e:
            raise FileExistsError(f"Project already exists at {base_dir}: {e}")
        except PermissionError as e:
            raise PermissionError(f"Cannot create project at {base_dir}: {e}")
        except Exception as e:
            raise ValueError(f"Failed to create project at {base_dir}: {e}")

    def _apply_project_template(self, project: FlowerPowerProject, template: str):
        """
        Apply a project template configuration to a newly created project.
        
        Args:
            project: FlowerPower project instance
            template: Template name to apply
        """
        # Define available templates
        templates = {
            'basic': {
                'description': 'Basic FlowerPower project with essential structure'
            },
            'ml_pipeline': {
                'description': 'Machine Learning pipeline template with ML-specific directories and configs'
            },
            'data_processing': {
                'description': 'Data processing pipeline template optimized for ETL workflows'
            },
            'batch_processing': {
                'description': 'Batch processing template for scheduled data workflows'
            },
            'streaming': {
                'description': 'Real-time streaming data pipeline template'
            }
        }
        
        if template not in templates:
            available_templates = ', '.join(templates.keys())
            raise ValueError(f"Unknown template '{template}'. Available templates: {available_templates}")
        
        template_config = templates[template]
        
        # Apply template configuration if the project supports it
        # This will depend on FlowerPower's specific API for configuration
        try:
            if hasattr(project, 'config'):
                if hasattr(project.config, 'template'):
                    project.config.template = template
                if hasattr(project.config, 'description') and not project.config.description:
                    project.config.description = template_config['description']
            
            # Note: Additional template-specific setup would depend on
            # FlowerPower's specific template system implementation
            
        except Exception as e:
            # Template application is optional, so we log the error but don't fail
            print(f"Warning: Could not apply template '{template}': {e}")
